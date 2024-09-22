from django.urls import path
from users.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    
    path('users/login/refresh/', TokenRefreshView.as_view()),
    path('users/login/verify/', TokenVerifyView.as_view()),


    path('users/login/', TokenObtainPairView.as_view()),
    path('users/register/', RegisterView.as_view()),
    path("users/logout_user/", logout_user.as_view()),
    path('users/me/', RetrieveUserView.as_view()),
    path('users/updateOrdeleted/<int:pk>/', UserAcccountAPIViewUpdateOrDelete.as_view()),
    path('users/', UserAccountAPIView.as_view()),

]