from django.urls import path
# from news.API.views import article_list_create_api_view, article_detail_api_view
from news.API.views import  ArticleDetailAPIView,ArticleListCreateAPIView


urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail')
]