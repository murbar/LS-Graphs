import random
from collections import deque


def walk_map(world, player, debug=False):
    traversal_path = []
    world_map = {}

    def init_room(room):
        if room not in world_map:
            exits = {direction: '?' for direction in player.currentRoom.getExits()}
            world_map[room] = exits

    def get_exits(room):
        return world_map[room]

    def get_next_direction(room):
        exits = get_exits(room)
        unexplored = [d for d, rm in exits.items() if rm == '?']
        # using a random direction is 988 moves, on average
        # using the first direction is 1007 moves
        # using the last direction is 997 moves
        # return random.choice(unexplored) if unexplored else None
        # return unexplored[0] if unexplored else None
        return unexplored[-1] if unexplored else None

    def invert_direction(direction):
        inverted = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
        return inverted[direction]

    def log_move(room, previous_room):
        if previous_room is None:
            return

        last_direction = traversal_path[-1]
        world_map[previous_room][last_direction] = room
        world_map[room][invert_direction(last_direction)] = previous_room

    def print_debug(room, world_map, traversal_path, previous_room, next_direction):
        if debug:
            print()
            print('in room:', room)
            print('map:', world_map)
            print('traversal path:', traversal_path)
            print('last room:', previous_room)
            print('next move:', next_direction)
            if not next_direction:
                print('dead end')

    def find_directional_path_through_rooms(room_sequence):
        path = []
        # skip the destination
        for i in range(len(room_sequence) - 1):
            cur, nxt = room_sequence[i], room_sequence[i+1]
            exits = world_map[cur]
            for d, rm in exits.items():
                if rm == nxt:
                    path.append(d)
        return path

    def backtrack(start_room):
        visited = set()
        paths_queue = deque()
        paths_queue.append([start_room])

        while paths_queue:
            path = paths_queue.popleft()
            last_room = path[-1]
            unexplored_exits = get_next_direction(last_room)
            if unexplored_exits:
                return find_directional_path_through_rooms(path)
            if last_room not in visited:
                visited.add(last_room)
                adjacent_rooms = [rm for d, rm in world_map[last_room].items()]
                for r in adjacent_rooms:
                    next_path = path.copy()
                    next_path.append(r)
                    paths_queue.append(next_path)

        return None

    # main loop
    previous_room = None
    while len(world_map) < len(world.rooms):
        current_room = player.currentRoom.id

        init_room(current_room)
        log_move(current_room, previous_room)

        next_direction = get_next_direction(current_room)

        print_debug(current_room, world_map, traversal_path,
                    previous_room, next_direction)

        if not next_direction:
            path_to_last_unexplored = backtrack(current_room)
            if path_to_last_unexplored:
                for direction in path_to_last_unexplored:
                    traversal_path.append(direction)
                    player.travel(direction)
                previous_room = None
        else:
            previous_room = current_room
            traversal_path.append(next_direction)
            player.travel(next_direction)

    return traversal_path
