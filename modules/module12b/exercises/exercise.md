---
title: "Module 9: Web Data"
css: ../../css/page.css
---

In this exercise we will use the Python [requests] library to interact with the
[ProPublica Congress API]. Web APIs are specialized websites that make data
available for many purposes, often for use in mobile applications, and
business-to-business data workflows. 

1. Install the [requests] Python library with pip.
1. Obtain the ProPublica Congress API key (from ELMS or register for your own)
1. Write a program that uses the [Get Current Members by State/District](https://projects.propublica.org/api-docs/congress-api/members/#get-current-members-by-statedistrict) to get the members of the House of Representatives for the state of Maryland.
1. For each representative use the [Get Recent Bills by a Specific Member](https://projects.propublica.org/api-docs/congress-api/bills/#get-recent-bills-by-a-specific-member) to get the bills they have introduced.
1. List only the bills from the current Congress (116) that they have introduced. 

[requests]: http://docs.python-requests.org/
[ProPublica Congress API]: https://www.propublica.org/datastore/api/propublica-congress-api

