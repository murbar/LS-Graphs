from social import SocialGraph
import statistics

sg = SocialGraph()
sg.populateGraph(20, 3)
lens = [len(f) for u, f in sg.friendships.items()]
print(sg.friendships)
print(f"Mean friendships is {statistics.mean(lens)}")
