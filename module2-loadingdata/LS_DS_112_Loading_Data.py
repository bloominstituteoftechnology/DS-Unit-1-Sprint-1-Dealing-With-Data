# TODO your work here!
# And note you should write comments, descriptions, and add new

#First things first...find a dataset to use
#We will import this data by copying the link
#But first, we have to import the libraries that we will be using

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#let's name the data we are loading something descriptive

student_data_url = 'https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv' #paste the link to the data
student_data = pd.read_csv(student_data_url)#this is loading the data using the pandas library function

#we can visualize the first few lines of the data by doing the following
student_data.head()
#Great! it worked. Let's look at what we have...and see what we may be able to visualize.
#Looks like there are plenty of things that we are able to look at.


# %%
#Let's figure out which columns have NaN values and work to fix those errors
student_data.isnull().sum()
student_data
# %%
x = student_data.PCTFLOAN.dropna()
y = student_data.PCTPELL.dropna()
# %%
plt.scatter(x, y)
plt.title('Students with Pell and Loans')
plt.xlabel('Percent of students with loans')
plt.ylabel('Percent of studetns with Pell')
# %%
plt.hist(x,20) #histogram with 20 bins
plt.xlabel('Percent of students')
plt.ylabel('# of Students')
plt.title('Histogram of Students with Loans')

# %%
plt.hist(y, 20)
plt.xlabel('Percent of students')
plt.ylabel('# of Students')
plt.title('Histogram of Students with Pell')
# %%
import seaborn as sns
sns.distplot(student_data['PCTFLOAN'], hist=False, color='r')
# %%
sns.distplot(student_data['PCTPELL'], hist=False, color='g')
# %%
# Seaborn Pairplot
sns.set(style='ticks', color_codes=True)
sns.pairplot(student_data)
# %%
from pandas.plotting import scatter_matrix

scatter_matrix(student_data)
plt.show()
# %% markdown
# ## Stretch Goals - Other types and sources of data
#
# Not all data comes in a nice single file - for example, image classification involves handling lots of image files. You still will probably want labels for them, so you may have tabular data in addition to the image blobs - and the images may be reduced in resolution and even fit in a regular csv as a bunch of numbers.
#
# If you're interested in natural language processing and analyzing text, that is another example where, while it can be put in a csv, you may end up loading much larger raw data and generating features that can then be thought of in a more standard tabular fashion.
#
# Overall you will in the course of learning data science deal with loading data in a variety of ways. Another common way to get data is from a database - most modern applications are backed by one or more databases, which you can query to get data to analyze. We'll cover this more in our data engineering unit.
#
# How does data get in the database? Most applications generate logs - text files with lots and lots of records of each use of the application. Databases are often populated based on these files, but in some situations you may directly analyze log files. The usual way to do this is with command line (Unix) tools - command lines are intimidating, so don't expect to learn them all at once, but depending on your interests it can be useful to practice.
#
# One last major source of data is APIs: https://github.com/toddmotto/public-apis
#
# API stands for Application Programming Interface, and while originally meant e.g. the way an application interfaced with the GUI or other aspects of an operating system, now it largely refers to online services that let you query and retrieve data. You can essentially think of most of them as "somebody else's database" - you have (usually limited) access.
#
# *Stretch goal* - research one of the above extended forms of data/data loading. See if you can get a basic example working in a notebook. Image, text, or (public) APIs are probably more tractable - databases are interesting, but there aren't many publicly accessible and they require a great deal of setup.
# %%
