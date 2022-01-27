
from django.urls import path

from .views import ArticleView




# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view(),name='articles'),
    path('articles/<int:pk>', ArticleView.as_view())

]
