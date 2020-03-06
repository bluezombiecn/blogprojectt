from django.urls import path
from blog.feeds import  AllPostsRssFeed
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
 #   path('search/',views.search,name='search'),
    path('search/',include('haystack.urls')),
]
