# data structures in python
# set
# set is a collection of unordered and unindexed elements
# it is mutable and does not allow duplicate elements
my_set = {1, 2, 3, 4, 5}
# you can create a set using curly braces or the set() constructor
my_set2 = set([1, 2, 3, 4, 5])
# you can add elements to a set using the add() method
my_set.add(6)

# you can remove elements from a set using the remove() method
my_set.remove(1)
# if you try to remove an element that does not exist, it will raise a KeyError
# you can use the discard() method to remove an element without raising an error

my_set.discard(2)  # does not raise an error if 2 is not in the set