from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-cordinates (movies), heights (num oscars)
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies") # title of the bar graph
plt.ylabel("# of Academy Awards") # y-axis label

# label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)

plt.show()