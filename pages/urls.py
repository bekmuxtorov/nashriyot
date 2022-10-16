from django.urls import path, include
from . import views


urlpatterns = [
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    path('article/edit/<int:pk>', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('add_article/', views.ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>', views.ArticleDetailView, name='article_detail'),
    path('category/<str:pk>', views.ArticleCategoryListView, name='categories'),
    path('base/', views.MainPagesView, name='main'),
    path('', views.AllPagesView, name='all'),
]