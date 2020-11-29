# Reference : https://realpython.com/python-sets/


# NOTE: | operator or other operator only work with a declared set, i.e. x1 works, {'baz', 'qux', 'quux'} doesn't 
### UNION
### x1 | x2 both return the set of all elements in either x1 or x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print("Union: " + str(x1 | x2)) # same output as x1.union(x2)
# Union: {'qux', 'quux', 'foo', 'baz', 'bar'}
# Can specify 1 or more sets e.g. a.union(b, c, d)  a | b | c | d

### INTERSECTION
### x1 & x2 return the set of elements common to both x1 and x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print("Intersection: " + str(x1 & x2)) # same output as x1.intersection(x2)
# Intersection: {'baz'}
# Can specify 1 or more sets e.g. a.intersection(b, c, d)  a & b & c & d

### DIFFERENCE
### x1 - x2 return the set of all elements that are in x1 but not in x2
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print("Difference: " + str(x1 - x2)) # same output as x1.difference(x2)
# Difference: {'foo', 'bar'}
# Can specify 1 or more sets e.g. a.difference(b, c)  a - b - c



### UPDATING SETS
# UPDATE 
# Update the set by adding elements from an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.update(R)
print("Update: " + str(H))
# Update: {'a', 'k', 'H', 'R', 'r', 'e', 'c', 'n'}

# INTERSECTION UPDATE
# Update the set by keeping only the elements found in it and an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print("Intersection Update: " + str(H))
# Intersection Update: {'k', 'a'}

# DIFFERENCE UPDATE
# Update the set by removing elements found in an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print("Difference Update: " + str(H))
# Difference Update: {'c', 'e', 'r', 'H'}

# SYMMETRIC DIFFERENCE UPDATE
# Update the set by only keeping the elements found in either set, but not in both.
H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print("Symmetric Difference Update: " + str(H))
# Symmetric Difference Update: {'c', 'n', 'R', 'H', 'e', 'r'}