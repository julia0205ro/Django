from datetime import datetime

from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def book_list(request):
    template = 'books/books_catalog.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def book_date(request, pub_date):
    pub_date = datetime.strptime(pub_date, "%Y-%m-%d").date()
    book = Book.objects.get(pub_date=pub_date)
    all_books = list(Book.objects.order_by('pub_date'))
    current_book_index = all_books.index(book)

    paginator = Paginator(all_books, 1)
    current_page = current_book_index + 1
    previous_page = current_book_index - 1
    previous_book = (list(Book.objects.order_by('pub_date').values())[previous_page]
                     .get('pub_date')).strftime('%Y-%m-%d')
    next_page = current_book_index + 1
    try:
        next_book = (list(Book.objects.order_by('pub_date').values())[next_page]
                     .get('pub_date')).strftime('%Y-%m-%d')
    except IndexError:
        next_book = (list(Book.objects.order_by('pub_date').values())[current_book_index]
                     .get('pub_date')).strftime('%Y-%m-%d')

    page = paginator.get_page(current_page)

    template = 'books/new_template.html'

    context = {'books': page.object_list,
               'my_book': book,
               'page': page,
               'previous_book': previous_book,
               'next_book': next_book}

    return render(request, template, context)
