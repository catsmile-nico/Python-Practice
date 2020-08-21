### UPDATING SETS
# Update the set by adding elements from an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.update(R)
print("Update: " + str(H))
# Update: {'a', 'k', 'H', 'R', 'r', 'e', 'c', 'n'}

# Update the set by keeping only the elements found in it and an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print("Intersection Update: " + str(H))
# Intersection Update: {'k', 'a'}

# Update the set by removing elements found in an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print("Difference Update: " + str(H))
# Difference Update: {'c', 'e', 'r', 'H'}

# Update the set by only keeping the elements found in either set, but not in both.
H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print("Symmetric Difference Update: " + str(H))
# Symmetric Difference Update: {'c', 'n', 'R', 'H', 'e', 'r'}