from social import SocialGraph
import statistics

sg = SocialGraph()
sg.populateGraph(1000, 10)
for u, f in sg.friendships.items():
    print(len(f))
lens = [len(f) for u, f in sg.friendships.items()]
print(f"Mean friendships is {statistics.mean(lens)}")
