# similar_books
recommend 10 similar_books isbn

ex) %python3 src/similar.py data/embedding_books_1.csv data/similar_1_test.csv 

embedding.csv must contain ['isbn','embedding'] columns

Macbook Pro M1 chip:
100 books -> 20 sec
10000 books -> 30 min
1000000 books -> 5 hours
