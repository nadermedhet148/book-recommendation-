# check list
# 1- get book ratings average
# 2- get relation with all books
# 3- sort related book by relations then rating
# %%
import pandas as pd
import numpy as np
import matplotlib as plt
# %%
#import data
books = pd.read_csv('./samples/books.csv')
tags = pd.read_csv('./samples/tags.csv')
ratings = pd.read_csv('./samples/ratings.csv')
book_tags = pd.read_csv('./samples/book_tags.csv')
# books.head(1000)
# tags.head()
# ratings.head(1000)
# book_tags.head()
# %%
# get rating average per book
reviews_per_book = ratings.groupby(['book_id'])[
    'rating'].mean()
reviews_per_book.head(100)

# %%
