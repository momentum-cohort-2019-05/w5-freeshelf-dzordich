from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from catalog.forms import CommentForm
from catalog.models import Book, Category, Favorites, Comment

def index(request):

    latest_book = Book.objects.latest('date')

    context = {
        'latest_book': latest_book,
    }

    return render(request, 'index.html', context=context)


class CategoryList(generic.ListView):
    model = Category



def book_detail_page(request, pk):
    book = Book.objects.get(pk=pk)
    is_favorited = False
    if request.user.is_authenticated:
        if Favorites.objects.filter(owner=request.user, book=book).exists():
            is_favorited = True

    num_favorites = Favorites.objects.filter(book=book).count()

    context = {
        'book': book, 
        'is_favorited': is_favorited,
        'num_favorites': num_favorites,
    }

    return render(request, 'catalog/book_detail.html', context)


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

    new_favorite, created = Favorites.objects.get_or_create(book=book, owner=request.user)
    if not created:
        new_favorite.delete()
    
    context = {
        'book': book,
        'new_favorite': new_favorite,
        'created': created,
    }

    return render(request, 'catalog/add_favorite_success.html', context)


@login_required
def add_comment(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment.objects.create(content=form.cleaned_data['user_comment'], commenter=get_user(request), book=book)
            comment.save()

            return HttpResponseRedirect(reverse('book-detail', args=pk))

    # If this is a GET (or any other method) create the default form.
    else:
        form = CommentForm()

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'catalog/add_comment.html', context)
