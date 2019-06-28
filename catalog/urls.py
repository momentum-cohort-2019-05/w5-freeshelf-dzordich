from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('categories/<pk>/books_by_category', views.books_by_category, name='books-by-category'),
    path('book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('favorites/', views.user_favorites, name='user-favorites'),
    path('<pk>/successful-add', views.add_to_favorites, name='success'),
]
