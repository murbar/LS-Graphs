from social import SocialGraph
import random
import statistics


def get_sample_users(n):
    one_percent = n * 0.01
    minimum = 5 if 5 < n else n
    sample_size = one_percent if one_percent > minimum else minimum
    samples = []
    while len(samples) < sample_size:
        user = random.randint(1, n)
        if user not in samples:
            samples.append(user)
    return samples


num_users = 1000
avg_friendships = 5
sg = SocialGraph()
sg.populateGraph(num_users, avg_friendships)
lens = [len(f) for u, f in sg.friendships.items()]
# print(sg.friendships)
print(f"Average friendships is {statistics.mean(lens)}")

# connections = sg.getAllSocialPaths(1)
# print("User 1's connections with shortest path: ", connections)

samples = get_sample_users(num_users)
ratios = []
average_serperations = []
for user in samples:
    connections = sg.getAllSocialPaths(user)
    ratio_of_graph = len(connections) / num_users
    ratios.append(ratio_of_graph)
    percentage = "{:.1%}".format(ratio_of_graph)
    print(
        f"Percentage of graph in user {user}'s extended network:", percentage)
    degrees = [(len(c) - 1) for u, c in connections.items()]
    average = statistics.mean(degrees)
    average_serperations.append(average)
    print(f"Average degree of seperatation between user and connections:", average)
total_average = statistics.mean(ratios)
print("")
print(f"Average percentage of graph for all users in sample:",
      "{:.1%}".format(total_average))
print(f"Average degree of seperation for all users in sample:",
      statistics.mean(average_serperations))
