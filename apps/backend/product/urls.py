from django.urls import path
from product.views import *

urlpatterns = [

    path('productsAll/',ProductsViewsAll.as_view()),
    path('productsPost/', ProductsViewsPost.as_view()),
    path('productsById/<int:pk>/',ProductsViewsId.as_view()),
    path('productsUpdate/<int:pk>/', ProductsViewsUpdate.as_view()),
    path('productsDeleted/<int:pk>/',ProductsViewsDeleted.as_view()),
   
]
