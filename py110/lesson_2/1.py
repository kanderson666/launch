# sort the following list of dictionaries based on the year of publication 
# of each book, from the earliest to the most recent
from pprint import pp

def get_year(my_dict):
    return int(my_dict['published'])
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
books.sort(key=get_year)
pp(books)
