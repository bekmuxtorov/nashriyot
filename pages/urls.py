from unicodedata import name
from django.urls import path, include
from . import views


urlpatterns = [
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('add_article/', views.ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>', views.ArticleDetailView, name='article_detail'),
    path('category/<str:pk>', views.ArticleCategoryListView, name='categories'),
    path('base/', views.MainPagesView, name='main'),
    path('', views.AllPagesView, name='all'),
]