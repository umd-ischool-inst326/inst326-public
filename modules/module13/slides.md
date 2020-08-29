---
title: "Data Analysis"
subtitle:
revealjs-url: "../../lib/reveal"
theme: "inst326"
transition: "slide"
---
#
::: notes 

This is a notes class on Pandas.

:::
#

## What is Pandas?
::: incremental

- Open source library meant for data analysis and data manipulation.
- Lets you create DataFrames from different data types that you may already be working with (csv, text, Excel, etc). 
- Lends itself to data manipulation (data wrangling) and data analysis purposes. 

:::

#

## DataFrames
::: incremental
- 2-dimensional labeled data structure with columns of potentially different types.
- You can think of them like a spreadsheet containing data
- They have indexes (row labels) and headers (column labels)

:::

#

<a title="Pandas DataFrame Example" href="https://www.geeksforgeeks.org/python-pandas-dataframe/"><img width="700" src="images/df.png"></a>

#

## Getting Basic Information from a DataFrame

The functions you need to know are:

::: incremental

- .head()
    - Will print the first 5 rows of the dataframe by default
    - Takes an optional argument for number of rows to print
- .tail()
    - Will print the last 5 rows of the dataframe by default
    - Takes an optional argument for number of rows to print

:::

#

## Getting Basic Information from a DataFrame

The functions you need to know are:

::: incremental
- .info()
    - Returns information on the columns present in the dataframe, the amount of rows in the dataframe, and the datatypes.
- .describe()
    - Will return basic descriptive statistics such as counts, mean, standard deviation, min, max and quartiles.
:::

#

## Pandas GroupBy

- It is important to understand how to navigate documentation.
- There are way too many methods with way too many arguments to memorize.
- GroupBy Method
    - [Group By Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

#

## Subseting and Other Methods
- There are simply too many Pandas methods to memorize.
- Luckily we have a very helpful resource.
- [Additional Pandas Functions](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

#

## Scenario 1
- What if someone says:
    - “I need a dataframe containing the mean cases for each county in Florida at each month so far in 2020.”
- Dataset:
    - [US Counties](https://www.kaggle.com/fireballbyedimyrnmom/us-counties-covid-19-dataset)

#

## Scenario 2

::: incremental

- Let's say that someone comes up to us and asks:
    - “Is there any way that I can get a dataset where I can see the mean budget, profit, and popularities for action movies per each production company that played a secondary role in production?”
- Dataset:
    - [Movies Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)
    - Contains data on production company, budgets, and genres for 5000 movies.

:::

#

## Data Visualizations

::: incremental

- Pandas convinently has methods that we can use in order to plot data that we might be interested in seeing.
- Under the hood, Pandas is using a library called Matplotlib
    - Matplotlib is a library specifically made for data visualizations. 
    - Can be difficult to use.

:::
#

## The Important Methods

- Scatter
- Bar Graph
- Histograms

#

## Seaborn

::: incremental

- We have been using methods built into pandas in order to create data visualizations.
- These methods are based on matplotlib, however, matplotlib can get complicated to use for more complicated visualizations.
- Seaborn tries to fix that issue by simplifying the process for making complex visualizations that look good.

:::

#

## SciPy

- Package used for scientific computing
- Part of the code packages that make up the "SciPy" ecosystem. 
    - Exosystem of packages that are particularly useful in science applications
    - These packages include matplotlib, pandas, and numpy

#

## The Important Statistical Tests

- Correlation Testing
- Z-Score
- T-Test
- ANOVA

#

## Correlation Testing

- [Correlation Testing](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)
    - Used to evaluate the association between two or more variables.

#

## Z Score

- [Z Score](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm)
    - Z tests are used to determine if two sample means are different
    - Z scores is a number representing how many standard deviations a datapoint is from the sample mean.
        - We can use [Z Score Tables](http://www.z-table.com/) to manually convert Z-Scores to find the percentage of observations that we expect to see to the left of the curve.
        - We can also use scipy to do this for us.

#

## T Test

- [T Test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
    - Used to determine if the means of two sample groups are different.

#

## ANOVA

- [ANOVA](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)
    - Tests if two or more groups have the same population mean.

#

## Statsmodels

[Statsmodels](https://www.statsmodels.org/stable/index.html) is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration.

#

## Linear Regression
::: incremental

- Modeling of the relationship between a dependent variable and one or more independent variables. 
- We are interested in using statsmodels to create linear regression models. 

:::