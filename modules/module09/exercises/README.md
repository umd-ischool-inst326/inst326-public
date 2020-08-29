---
title: "Module 9 Exercises"
css: ../../../css/page.css
permalink: index.html
---

## Using SQL for querying

The data in the CSV file, [energy.csv](energy.csv), should look familiar to you, it’s the data that we were working with in module 4. Remember how we had to iterate through the file to determine the largest wind and solar producing state?

This time the CSV has been cleaned up a bit by removing the total rows which we had to ignore the last time. We’re going to use it as a way of explore why SQL, databases and Python are useful tools to use together.

create a program that can read in the CSV data and load it into a database
query the database to see what the maximum solar and wind producers are
determine the total solar and wind production in the US by year

## Populating a database programmatically

The data in this CSV file ([books.csv](books.csv)) consists of a list of titles, authors, and dates of important works of fiction. The data are similar to the data used in the above examples.

The first task is to create a program that can read the data in the attached file and load it into a database.

## Challenge: Design and modeling practice

Consider again the bibliographic database, note that there are multiple titles in the attached file written by a single author. In order to normalize this data, the author names should be moved into their own table and related to the book data through a relationship.

How can the authors data be related to the book titles? Can you create a program that will manage the normalization process at load time?
