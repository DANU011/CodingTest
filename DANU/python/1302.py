import sys

book_count = dict()
num_of_books = int(input())

for _ in range(num_of_books):
    book_name = sys.stdin.readline().rstrip()
    if book_name in book_count:
        book_count[book_name] += 1
    else:
        book_count[book_name] = 1

max_count = 0
max_book_name = ''

sorted_book_count = dict(sorted(book_count.items()))

for book_name in sorted_book_count:
    if sorted_book_count[book_name] > max_count:
        max_count = sorted_book_count[book_name]
        max_book_name = book_name

print(max_book_name)
