
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


# %%
# get relted books to selected one
def getReltedBooks(book_name):
    # get book's readers , example The Hunger Games
    book = books.loc[books['original_title'] == book_name]
    book_readers = ratings.loc[ratings['book_id']
                               == book['id'][0]].sort_values('rating', ascending=False)
    # get users  books
    all_readers_books = {}
    for index, reader in book_readers.iterrows():
        # get all realted books
        reader_books = ratings.loc[ratings['user_id']
                                   == reader['user_id']]
        # group books by id and get its average rating and count
        for index, book in reader_books.iterrows():
            if book['book_id'] in all_readers_books.keys():
                all_readers_books[book['book_id']
                                  ]['count'] = all_readers_books[book['book_id']]['count'] + 1
            else:
                book_data = books.loc[books['book_id'] == book['book_id']]
                all_readers_books[book['book_id']] = {
                    "count": 1,
                    "book_id": int(book['book_id']),
                    "average_rating": int(reviews_per_book[book['book_id']]),
                    "book_name": str(book_data['original_title'])
                }
    # sort books to get high priority first
    sorted_books = sorted(all_readers_books.values(),
                          key=lambda y: (y['count'] + y['average_rating']),  reverse=True)

    return sorted_books


# %%
# create api with flask
