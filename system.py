# check list
# 1- get book ratings average
# 2- get relation with all books
# 3- sort related book by relations then rating
# %%
import pandas as pd
import numpy as np
import matplotlib as plt
# %%
# import data
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
# reviews_per_book.head(100)
# %%
# get book's readers , example The Hunger Games
Hunger_Games = books.loc[books['original_title'] == 'The Hunger Games']
Hunger_Games_readers = ratings.loc[ratings['book_id']
                                   == Hunger_Games['id'][0]].sort_values('rating', ascending=False)
# get users  books
all_readers_books = {}
for index, reader in Hunger_Games_readers.iterrows():
    # get all realted books
    reader_books = ratings.loc[ratings['user_id']
                               == reader['user_id']]
    # group books by id and get its average rating and count
    for index, book in reader_books.iterrows():
        if book['book_id'] in all_readers_books.keys():
            all_readers_books[book['book_id']
                              ]['count'] = all_readers_books[book['book_id']]['count'] + 1
        else:
            all_readers_books[book['book_id']] = {
                "count": 1,
                "book_id": book['book_id'],
                "average_rating": reviews_per_book[book['book_id']]
            }


print(all_readers_books)

# %%
