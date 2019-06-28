from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic

from catalog.models import Book, Category, Favorites

def index(request):

    latest_book = Book.objects.latest('date')

    context = {
        'latest_book': latest_book,
    }

    return render(request, 'index.html', context=context)


class CategoryList(generic.ListView):
    model = Category


class BookDetailView(generic.DetailView):
    model = Book

class BookListView(generic.ListView):
    model = Book


def books_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    books_in_category = Book.objects.filter(category=category)

    context = {
        'category': category,
        'books_in_category': books_in_category
    }

    return render(request, 'catalog/books_by_category.html', context)


@login_required
def user_favorites(request):
    favorites = Favorites.objects.filter(owner=request.user)

    favorites_list = []

    for favorite in favorites:
        favorites_list.append(favorite.book)

    context = {
        'favorites': favorites,
        'favorites_list': favorites_list,
    }

    return render(request, 'catalog/favorites.html', context)


@login_required
def add_to_favorites(request, pk):
    book = get_object_or_404(Book, pk=pk)

    new_favorite = Favorites.objects.create(book=book, owner=request.user)

    context = {
        'book': book,
        'new_favorite': new_favorite,
    }

    return render(request, 'catalog/add_favorite_success.html', context)
