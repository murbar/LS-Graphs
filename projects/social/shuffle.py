import random

def fisher_yates_shuffle(l):
    for i in range(len(l)):
        j = random.randint(0, len(l) - 1)
        l[i], l[j] = l[j], l[i]