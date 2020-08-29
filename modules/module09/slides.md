---
title: "Relational Databases"
subtitle:
revealjs-url: "../../lib/reveal"
theme: "inst326"
transition: "slide"
---
#

<a title="Daderot [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Cuneiform_tablet_with_bread_and_flour_distributions,_Ur_III_Period,_c._2100-2000_BC_-_Harvard_Semitic_Museum_-_Cambridge,_MA_-_DSC06146.jpg"><img width="450" alt="Cuneiform tablet with bread and flour distributions, Ur III Period, c. 2100-2000 BC - Harvard Semitic Museum - Cambridge, MA - DSC06146" src="images/cuneiform.jpg"></a>

::: notes

This example of a cuneiform (wedge-shaped) writing tablet dates from the 3rd millennium BCE and records the distribution of bread and flour. It is shown here as an example of early record keeping. Writing systems developed first and foremost as a means of keeping track of legal agreements and business transactions, even before they were used for literary purposes.

Image in public domain; original in Harvard Semitic Museum (Cambridge, MA).

:::

#

## Tools

For our work with databases, we'll be using three tools:

- **SQLite** (database)
- **sqlite3** (Python module)
- **DB Browser** (GUI application)

#

## Tools: SQLite

::: incremental

- lightweight relational database (RDBMS)
- runs locally and stores data in files
- no separate database server required
- already installed on your system (as part of Python)
- project website: [https://www.sqlite.org](https://sqlite.org/mostdeployed.html)

:::

#

## Tools: sqlite3

::: incremental

- module in the standard library
- facilitates interaction with the database by:
    1. managing connections
    2. passing queries to the database system
    3. making results of queries accessible to Python

:::

#

## Tools: DB Browser for SQLite

::: incremental

- graphical application (GUI)
- allows you to view the contents of a SQLite database
- an optional convenience for this course
- downloadable from [https://sqlitebrowser.org](https://sqlitebrowser.org)

:::

# Databases

#

<a title="Washington, D.C. Jewal Mazique [i.e. Jewel] cataloging in the Library of Congress (1942)" href="https://www.loc.gov/pictures/item/2017828941/"><img width="600" alt="Image of a woman working with the card catalog in the Library of Congress, 1942" src="images/cardcatalog.jpg"></a>

::: notes

This image of Jewell Mazique (https://en.wikipedia.org/wiki/Jewell_Mazique) working with the card catalog in the Library of Congress is included here to illustrate the more general meaning of the term 'database' as any large collection of structured information.

:::

#

## The Relational Model

::: incremental

- Invented by E. F. Codd in the 1970s
- Data stored in tables (relations)
- Relations consist of rows (tuples)
- Tuples have columns (attributes) that hold values
- The term "database" now often connotes this type of relational database

:::

#

## Other DB Systems

::: left

Database design/theory is a much larger topic. In fact it is an entire course (INST 327)! Here are a just a few database systems you may encounter:

- **Relational**:
    - mySQL/MariaDB
    - PostgreSQL
- **Non-relational** ("NoSQL"):
    - Document: MongoDB (JSON), BaseX (XML)
    - Graph: Neo4j, Fuseki

:::

#

## 'Normalization'

::: incremental

- Through a design process, data are "normalized"
- Normalization means applying a set of rules (called "normal forms") to increase efficiency and reduce redundancy
- Many specifics of database design and normalization are outside the scope of this course

:::

#

## SQL

::: incremental

- a standardized language is used to interact with a relational database
- this is known as the Structured Query Language (SQL)
- SQL has different flavors but generally works the same way across database systems

:::

#

## CRUD

::: left

Basic database operations are called "CRUD":

:::

::: incremental

- CREATE: add data to the database
- READ: retrive data from one or more tables
- UPDATE: make changes to the data
- DELETE: remove rows from a table (potentially with a cascade effect)

:::

# Using a Database with Python

#

## Connecting to a database: in-memory

~~~~ {.python .numberLines}
# import the sqlite3 module
>>> import sqlite3

# '::memory::' is special sqlite3 syntax
>>> conn = sqlite3.connect(':memory:')
>>> conn
<sqlite3.Connection object at 0x10507b110>
~~~~

#

## Connecting to a database: database file

~~~~ {.python .numberLines}
# connect to an in-memory database
>>> conn2 = sqlite3.connect('test.sqlite')
>>> conn2
<sqlite3.Connection object at 0x10507b030>
# a file will appear in the working directory
~~~~

#

## The connection object

- This object manages the database connection
- In addition, we need a cursor to manage state
- The cursor sends queries and contains results

~~~~ {.python .numberLines}
# imagine we are creating a bibliographic db
conn = sqlite3.connect('biblio.sqlite')
# to query this db we must create a cursor
cursor = conn.cursor()
~~~~

#

## Setting up the database

~~~~ {.python .numberLines}
# create a table to hold some data with CREATE
# docstrings are commonly used for queries
cq = '''CREATE TABLE books (
        title TEXT, author TEXT, date INTEGER
        )'''
cursor.execute(cq)
~~~~

::: notes

Docstrings are triple-quoted strings (with ' or "), and allow internal line breaks. Line breaks, which are insignificant in SQL, are often used to format queries for readability.

:::

#

## Create entries

~~~~ {.python .numberLines}
# Next add a row to the table with INSERT
iq = '''INSERT INTO books VALUES (
     '2001: A Space Odyssey',
     'Arthur C. Clarke', '1951'
     )'''
cursor.execute(iq)
~~~~

#

## Scaling up

- This works fine, but can be impractical at scale
- Larger numbers of records can be created with executemany()

~~~~ {.python .numberLines}
# First, create some data
# (in real life you might read this from a file)
# Structure it as a list of tuples
data = [("I, Robot", "Isaac Asimov", 1950),
        ("The Martian", "Andy Weir", 2012),
        ("The Left Hand Of Darkness",
            "Ursula K. Le Guin",1969)]
~~~~

#

## Scaling up (continued)

~~~~ {.python .numberLines}
# Next, create a query with placeholders
imq = '''INSERT INTO books VALUES (?,?,?)'''

# Finally, pass query & data to executemany()
cursor.executemany(imq, data)
~~~~

#

## Read

~~~~ {.python .numberLines}
# Next, to view the data, use a SELECT query
sq = '''SELECT title FROM books'''
# Execute the query as before, appending fetchall()
# which assigns results to 'books' variable
books = cursor.execute(sq).fetchall()
print(books)
[('2001: A Space Odyssey',),
    ('I, Robot',),
    ('The Martian',),
    ('The Left Hand Of Darkness',)]
~~~~

#

## Update

- Now, imagine we need to update some data.
- _The Martian_ was in fact published in 2011, so let's make that correction.

~~~~ {.python .numberLines}
uq = '''UPDATE books
        SET year=2011
        WHERE title="The Martian"'''
cursor.execute(uq)
~~~~

#

## Verify Update

~~~~ {.python .numberLines}
# now query just that row to verify
vq = '''SELECT * FROM books
        WHERE title="The Martian"'''
cursor.execute(vq)
print(cursor.fetchall())
[('The Martian', 'Andy Weir', 2011)]
~~~~

#

## Delete

::: left

- Now, let's look at deleting data
- This works much as you would expect

:::

~~~~ {.python .numberLines}
dq = '''DELETE FROM books
        WHERE author="Isaac Asimov"'''
cursor.execute(dq)
~~~~

#

## Committing Changes

- So far, what we have done has occurred in-memory
- To persist, changes must be committed (saved)

~~~~ {.python .numberLines}
# Normally you do this after completing each change
conn.commit()
# With changes saved, the connection can be closed
conn.close()
~~~~

#

## Summary

::: incremental

- We have just covered a lot of ground
- Connections, cursors, queries, CRUD
- There is also a lot we have not touched
- Next time we will look at normalization
- Specifically: _primary keys_, _foreign keys_, and _joins_

:::

# Exercise

#

## Exercise 1: Load a large dataset

::: left

The data in this CSV file ([books.csv](books.csv)) consists of a list of titles, authors, and dates of important works of fiction. The data are similar to the data used in the above examples.

The first task is to create a program that can read the data in the attached file and load it into a database.

:::

# Normalizing and Joining Data

#

## Why Normalize?

::: incremental

- There are many reasons related to optimization
- But the simplest way to think about it is this:
    1. Consider that one author can write many books
    2. Conversely one book can have many authors
    3. To model such relationships effectively, author data should be stored apart from book data

:::

#

## Identifiers (Keys)

::: incremental

- The first requirement for modeling relationships between tables is to have unambiguous identifiers
- These identifiers, called keys, allow data to be looked up
- The unique id for a particular row in a table is called a primary key

:::

#

## Using Keys to Create Joins

::: incremental

- Rows can also reference rows in other tables -- this cross-reference is called a foreign key
- For example, the row "Hamlet" in the plays table might reference "William Shakespeare" in the authors table

:::

#

## Creating Normalized Data

::: incremental

- When designing a database, before doing any coding tables and their relationships should be mapped out
- The diagram created during this mapping process is called an ERD
- This stands for Entity-Relationship Diagram
- In addition to mapping out relationships, you need to create code to analyze the data and write it to the correct locations

:::

#

## Creating Normalized Data (continued)

::: incremental

- For example, in working with our list of books and authors, you might:
    1. Store the authors names in a separate table
    2. As you read the data file, lookup the author
    3. If the author is present already, get the id
    4. If the author is not present, add the author and get the id
    5. Add the book to the books table, referencing the author's id

:::

#

## Flat Data

<table>
<tr>
    <th>title</th>
    <th>author</th>
    <th>year</th>
</tr>
<tr>
    <td>Things Fall Apart</td>
    <td>Chinua Achebe</td>
    <td>1958</td>
</tr>
<tr>
    <td>Chimera</td>
    <td>John Barth</td>
    <td>1972</td>
</tr>
<tr>
    <td>The Sot-Weed Factor</td>
    <td>John Barth</td>
    <td>1960</td>
</tr>
<tr>
    <td>Under the Volcano</td>
    <td>Malcolm Lowery</td>
    <td>1947</td>
</tr>
</table>

#

## Add Primary Keys

<table>
<tr>
    <th>id</th>
    <th>title</th>
    <th>author</th>
    <th>year</th>
</tr>
<tr>
    <td>1</td>
    <td>Things Fall Apart</td>
    <td>Chinua Achebe</td>
    <td>1958</td>
</tr>
<tr>
    <td>2</td>
    <td>Chimera</td>
    <td>John Barth</td>
    <td>1972</td>
</tr>
<tr>
    <td>3</td>
    <td>The Sot-Weed Factor</td>
    <td>John Barth</td>
    <td>1960</td>
</tr>
<tr>
    <td>4</td>
    <td>Under the Volcano</td>
    <td>Malcolm Lowry</td>
    <td>1947</td>
</tr>
</table>

#

## Move Authors to Own Table

<table>
<tr>
    <th>id</th>
    <th>title</th>
    <th>author_id</th>
    <th>year</th>
</tr>
<tr>
    <td>1</td>
    <td>Things Fall Apart</td>
    <td>1</td>
    <td>1958</td>
</tr>
<tr>
    <td>2</td>
    <td>Chimera</td>
    <td>2</td>
    <td>1972</td>
</tr>
<tr>
    <td>3</td>
    <td>The Sot-Weed Factor</td>
    <td>2</td>
    <td>1960</td>
</tr>
<tr>
    <td>4</td>
    <td>Under the Volcano</td>
    <td>3</td>
    <td>1947</td>
</tr>
</table>


<table>
<tr>
    <th>id</th>
    <th>name</th>
</tr>
<tr>
    <td>1</td>
    <td>Chinua Achebe</td>
</tr>
<tr>
    <td>2</td>
    <td>John Barth</td>
</tr>
<tr>
    <td>3</td>
    <td>Malcolm Lowry</td>
</tr>
</table>


#

## Selecting Normalized Data

::: incremental

- To lookup normalized data, you can use SQL's JOIN syntax
- You specify the fields to match on (linking foreign key to primary key)

~~~~ {.python .numberLines}
jq = '''SELECT authors.name, books.title, books.year
        FROM books JOIN authors
        ON books.author_id=authors.id'''
books = cursor.execute(join_query, filter).fetchall()
~~~~

:::

#

## Deleting Normalized Data

::: incremental

- Normalizing data introduces some additional complications
- Consider our authors and books examples
- If you remove a row from the authors table, what happens to the author's books?
- There is a danger that orphaned rows will clutter the database

:::

#

## Deleting Normalized Data (continued)

::: incremental

- In order to control the creation of bad data, SQL allows you to specify constraints in your database schema
- Among the constraints is one called CASCADE DELETE
- In essence, by specifying this constraint, you would force SQLite to remove books that were written by a deleted author when removing the author

:::

#

## Exercise 2: Normalization in action

::: left

Consider again the bibliographic database, note that there are multiple titles in the attached file written by a single author. In order to normalize this data, the author names should be moved into their own table and related to the book data through a relationship.

How can the authors data be related to the book titles? Can you create a program that will manage the normalization process at load time?

:::
