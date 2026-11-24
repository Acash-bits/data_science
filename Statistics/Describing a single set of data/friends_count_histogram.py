# Creating a histogram to count friends

from collections import Counter
import matplotlib.pyplot as plt
import random

num_friends = []

while len(num_friends) <= 100:
    friend_count = random.randrange(1,101)
    num_friends.append(friend_count)

friend_counts = Counter(num_friends)
xs = range(101) # Largest value is 100
ys = [friend_counts[x] for x in xs] # Height is # of friends
plt.bar(xs, ys)
plt.axis([0,101,0,25])
plt.title("Histogram of Friend counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()