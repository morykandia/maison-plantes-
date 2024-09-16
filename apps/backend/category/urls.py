from django.urls import path
from category.views import *

urlpatterns = [

    path('categoriesAll/',CategoriesViewsAll.as_view()),
    path('categoriesPost/', CategoryViewsPost.as_view()),
    path('categoriesById/<int:pk>/',CategoriesViewsId.as_view()),
    path('categoriesUpdate/<int:pk>/', CategoryViewsUpdate.as_view()),
    path('categoriesDeleted/<int:pk>/',CategoryViewsDeleted.as_view()),
   
]
