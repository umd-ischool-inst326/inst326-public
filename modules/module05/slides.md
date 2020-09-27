---
title: "Data Structures"
subtitle:
revealjs-url: "../../lib/reveal.js.4.0.2"
theme: "inst326_gabriel"
transition: "slide"
---

#

## Tuples


#

## Tuples Structure

::: incremental

- What we know
    - Collection of objects that are ordered and immutable
    - Tuples are sequences
    - Tuples use parentheses to enclose sequences


:::

#

## Creating Tuples

### What we know:

~~~~ {.python .numberLines}
my_tuple = tuple([1,2,3])
my_tuple = (1, “string”, 5.8)
~~~~

#

## Creating Tuples

### What is new:

~~~~ {.python .numberLines}
my_tuple =  1, “string”, 5.8 
my_tuple = “string”, 
my_tuple = ()
~~~~

The comma is what allows python to recognize the tuple

#

## Accessing Values in a Tuple

We can use square brackets to slice at the indices just like other secuence datatypes.

~~~~ {.python .numberLines}
my_tuple = (1, “string”, 5.8)

my_tuple[1]    # "string"
my_tuple[:1]   # (1,)
my_tuple[:3]   # (1, “string”, 5.8)
~~~~

#

## Important Tuple Operations
| Python Expression         | Results                   | Description   |
|---------------------------|---------------------------|---------------|
| len((1,2,3))              | 3                         | Length        |
| (1,2,3) + (4,5,6)         | (1,2,3,4,5,6)             | Concatenation |
| ("Hi!",) * 4              | ("Hi!","Hi!","Hi!","Hi!") | Repetition    |
| 3 in (1,2,3)              | True                      | Membership    |
| for x in (1,2,3): print x | 1 2 3                     | Iteration     |

#

## Recap
- Tuples are sequences, ordered and immutable collections of objects.
- Tuples are enclosed with parentheses, items are separated with commas.
- Items in tuples can be accessed using square bracket notation.
- We can perform a variety of operations on tuples.


#

## Returning Tuples

::: incremental

- Sometimes it might be a good idea to return multiple items using a function.
- Typically, if these items are different data types its good practice to return a tuple.
    - For example, a function that returns a list of unique words, and a dictionary of an index of those words to files.

:::

#

~~~~ {.python .numberLines}
class book:
    def __init__(self, path):
        self.f = open(path).read()
    
    def meta_data(self):
        """ Method that will return two variables
        Returns:
            unique_words (list): list of unique words in the file
            word_counts (dict): a dictionary where the keys are 
            the words and the values are the number of times that 
            the word appears in the file
        """

        return unique_words, word_counts

my_path = "my_file.txt"
results = book(my_path).meta_data()
~~~~

#

## Tuples as Sequences

#

## Tuples are Sequence Datatypes
This means that we can...

#

## Find Min and Max Values

~~~~ {.python .numberLines}
max(tuple)
min(tuple)
~~~~ 

#

## Perform Sequence Unpacking
~~~~ {.python .numberLines}
class book:
    def __init__(self, path):
        self.f = open(path).read()
    
    def meta_data(self):
        """ Method that will return two variables
        Returns:
            unique_words (list): list of unique words in the file
            word_counts (dict): a dictionary where the keys are 
            the words and the values are the number of times that 
            the word appears in the file
        """

        return unique_words, word_counts

my_path = "my_file.txt"
words, counts = book(my_path).meta_data()
~~~~

#

## Iterate over the Tuple

~~~~ {.python .numberLines}
class book:
    def __init__(self, path):
        self.f = open(path).read()
    
    def meta_data(self):
        """ Method that will return two variables
        Returns:
            unique_words (list): list of unique words in the file
            word_counts (dict): a dictionary where the keys are 
            the words and the values are the number of times that 
            the word appears in the file
        """

        return unique_words, word_counts

my_path = "my_file.txt"
results = book(my_path).meta_data()

for item in results:
    print(item)
~~~~

#

## Perform Sequence Operations
| Python Expression         | Results                   | Description   |
|---------------------------|---------------------------|---------------|
| len((1,2,3))              | 3                         | Length        |
| (1,2,3) + (4,5,6)         | (1,2,3,4,5,6)             | Concatenation |
| ("Hi!",) * 4              | ("Hi!","Hi!","Hi!","Hi!") | Repetition    |
| 3 in (1,2,3)              | True                      | Membership    |
| for x in (1,2,3): print x | 1 2 3                     | Iteration     |


#

## Sets 

#

## Structure of Sets

::: incremental

- Collection of objects that are un-ordered and mutable
- Contain no duplicate elements
- Sets use curly braces to enclose sequences

:::

#

## Frozen Sets

::: incremental

- Collection of objects that are un-ordered and immutable
- Contain no duplicate elements
- Frozensets use curly braces to enclose sequences


:::

#

## Recap

::: incremental

- Sets are collections of unique items that are mutable and unordered.
- Frozen sets are collections of unique items that are immutable and unordered.

:::

#

## Creating Sets

#

~~~~ {.python .numberLines}
myset = {"a", "b", "c"}
myset = set(["a", "b", "c"])
myset = set([ "a", "a" , "b" , "c" , "c" ])
~~~~

#

~~~~ {.python .numberLines}
myset = frozenset({"a", "b", "c"})
myset = frozenset(["a", "b", "c"])
myset = frozenset([ "a", "a" , "b" , "c" , "c" ])
~~~~

#

## Removing Elements from Sets

~~~~ {.python .numberLines}
myset.remove(“a”)
~~~~

#

## Adding Elements from Sets

~~~~ {.python .numberLines}
myset.add(“a”)
~~~~

#

## A Note About Sets

::: incremental

- Items in sets must be “hashable” (think immutable) otherwise you will raise an error.
    - Frozen sets are immutable and therefor hashable, so frozensets can be items in a set without a problem. 

:::

#

## Hash Tables
- In Python, sets and dictionaries are implemented using hashtables
    - Hash tables: Data structures where items are passed through a “hash function” to compute a “hash code”. 
        - Optimized for data retrieval where we might not care about member order.



#

## Why do Hash Tables matter?

::: incremental

- Implimentation helps guide decision making:
    - If we care about member order in relation to other members:
        - strings, lists, tuples
    - If we prioritize membership or value pairing over "order":
        - sets, dictionaries

:::

#

## Consider the following

::: incremental

- Is "morse" in "the morse code"?
    - Yes
- Are the letters m,o,r,s, and e in "here come the dots"?
    - Yes
- Is "morse" in "here come the dots"?
    - No

:::

#

## Recap

- We can create sets using set literals ({}) or by using the set() function.
- We can remove or add items from sets using the add() and remove() methods of set objects.
- Items in sets must be hashable (immutable).

#

## Working with sets

#

## Set operations
::: incremental

- We can use sets to solve unique challenges (or trivial challenges in unique ways)
- In order to do this we need to perform operations using sets.
- The ones you need to be aware of are…
    - in (membership) & not in (membership)
    - is subset & is superset 
    - union, intersection, difference

:::

#

## In & Not In

- Testing for membership
- Example:
    - x in f (where “x” is an item that may or may not be in set “f”)
    - x not in f (where “x” is an item that may or may not be in set “f”)

#

## Is Subset & Is Superset
- Testing whether all elements in one set are in another set
- Example:
    - x.issubset(f)  (where “x” is a set that may or may not contain the same elements that are in set “f”)
        - Alternative syntax: x <= f
    - x.issuperset(f)  (where “f” is a set that may or may not contain the same elements that are in set “x”)
        - Alternative syntax: x >= f

#

## Union

**Union, Intersection and Difference all evaluate to new sets.**

- Union
    - New set with elements of two sets
    - Example Syntax:
        - x.union(f)

#

## Intersection

**Union, Intersection and Difference all evaluate to new sets.**

- Intersection
    - New set with elements that are common to both sets
    - Example Syntax:
        - x.intersection(f)

#

## Difference

**Union, Intersection and Difference all evaluate to new sets.**

- Difference
    - New set with elements in the first set but not the second set
    - Example Syntax:
        - x.difference(f)

#

## Example Using Sets
~~~~ {.python .numberLines}
list1 = [1,1,2,2,3,3,4,5]
list2 = [3,3,4,4,5,5,6,6,7,8,9]

set1, set2 = set(list1), set(list2)
set3 = set1.intersection(set2) 

print(len(set3)) #Result = 3
~~~~

#

## Compared to No Sets
~~~~ {.python .numberLines}
list1 = [1,1,2,2,3,3,4,5]
list2 = [3,3,4,4,5,5,6,6,7,8,9]

resulting_list = []
for num in list1:
    if num in resulting_list:
        continue
    else:
        if num in list2:
            resulting_list.append(num)

print(len(resulting_list)) #Result = 3
~~~~

#

## Lists

#

## Stacks and Queues
::: incremental

- By this point you should feel comfortable using lists in your code.
- You should also be comfortable in understanding how the way that we think about lists guides the manner in which we utilize those lists in our code. 

:::

#

## Stacks

::: incremental

- Lists that contain objects that are added and removed using the LIFO principle (Last in, first out). 
    - Theoretically speaking we “push” things to the end/top of a list and then “pop” the items off the end/top of the list.
    - Ex. A stack of plates

:::

#

## Stacks Continued

::: incremental

- We can simulate stacks by using the append and pop methods of list objects
- Uses:
    - Holding and using most recent data elements for use in algorithms where that may be important. 

:::

#

## Queues

::: incremental

- Lists that contain objects that are added and removed using the FIFO principle (First in, first out). 
    - Theoretically speaking we “enqueue” things to the top/end of a list and then “dequeue” the items off the beginning of the list.
    - Ex. A line of people waiting at the DMV.

:::

#

## Queues Continued

::: incremental

- We can simulate stacks by using the append and pop(0) methods of list objects
- Uses:
    - Using collections where the order of the item has something to do with the FIFO principle such as algorithms for determining wait times.

:::

#

## List Comprehensions

#

## What are List Comprehensions?
- List comprehensions are expressions that evaluate to lists 
- Often are faster than iterating over one list to build another list

~~~~ {.python .numberLines}
numbers = [1,2,3,4]
squares = [n**2 for n in numbers]

print(squares) # Output: [1,4,9,16]
~~~~

#

## Syntax
- A list comprehension consists of 
    1. brackets containing an expression 
    2. followed by a for clause (iterating over some iterable)
    3. then zero or more for or if clauses.

~~~~ {.python .numberLines}
list_a = [1,2,3]
cube_list = [ [a**2, a**3] for a in list_a]

print(cube_list) # Output: [[1,1], [4,8], [9,27]]
~~~~

#

## List Comprehensions - Concise Lists
- List comprehensions can help make code shorter and more concise
- Consider the following example:

~~~~ {.python .numberLines}
[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
~~~~

#

## Dictionaries

#

## What we know

::: incremental

- Dictionaries are unordered collections of key/value pairs
- We can create dictionaries with:
    - dict() 
    - curly braces

:::

#

## What we know - Accessing Data

#### We can access data in dictionaries:
- By referencing the a key
    - dictionary[key]
- Using built in methods
    - keys() - returns list of all keys in dictionary
    - values() - returns a list of all values in dictionary
    - items() - returns a list of tuples containing key value pairs

#

## What We Know - Removing Data

#### We can remove data from the dictionary using:
- pop() method
    - returns dictionary
- del() built in function

#

## Dictionary Items

::: incremental

- Similar to sets, dictionaries in Python are implemented using hash tables.
    - In this case the keys are hashed and those corresponding hash codes then point to an unhashed object (the value)
- Only hashable (immutable) objects can be keys.
- Values can be either mutable or immutable.

:::

#

## Important Things to Know

**1) Dictionaries Can Be Values in Other Dictionaries**

::: incremental

- Remember that when you use bracket notation to access the value of a key in a dictionary, the expression evaluates to the value itself.
- This means that if I evaluate to a value that is a dictionary, I can access the values of the keys to the inner dictionary.
    - And so on and so forth.


:::

#

## Here is an Example

~~~~ {.python .numberLines}
Dict = { 'Dict1': {"1": 'G', "2": 'F', "3": 'G'},
         'Dict2': {'Name': 'INST326', "1": ["1", "2"]} }

~~~~

~~~~ {.python .numberLines}
Dict[“Dict1”] #{1: 'G', 2: 'F', 3: 'G'}
Dict[“Dict1”]["2"] #“F”

~~~~


#

## Important Things to Know

**2) One common use for dictionaries is to use them to count unique values in a sequence data type.**

#

## Important Things to Know

**3) One common use for dictionaries is to use them to index data.**
