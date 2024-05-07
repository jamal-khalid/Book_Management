from django.urls import path
from .views import UserRegistrationView, UserLoginView , UserProfileView ,BookView,BookDetailView 
from .views import (ReadingListCreateAPIView , ReadingListDetailView,
                    ReadingListAddBookView  , ReadingListRemoveBookView)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('books/' , BookView.as_view()),
    path('books/<int:pk>/' , BookDetailView.as_view()),
    path('reading-lists/' ,ReadingListCreateAPIView.as_view()),
    path('reading-lists/<int:pk>/' ,ReadingListDetailView.as_view() ),
    path('reading-lists/<int:pk>/add-book/', ReadingListAddBookView.as_view(), name='reading-list-add-book'),
    path('reading-lists/<int:pk>/remove-book/', ReadingListRemoveBookView.as_view(), name='reading-list-remove-book'),
]
