from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import *


urlpatterns = [
    # path('', home_view, name='home'),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    url('accounts/logout/', Logout.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('create/', CreateView.as_view()),
    path('read/', ReadView.as_view()),
    path('read/<int:pk>', ReadIndividualView.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('delete/<int:pk>', DeleteView.as_view()),
    path('accounts/register/', RegisterView.as_view(), name='register'),
 ]