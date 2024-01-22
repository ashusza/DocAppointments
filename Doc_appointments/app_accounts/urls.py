from django.urls import path
from app_accounts.views import loginview  ,logoutview ,RegisterView

urlpatterns = [
    path('login/',loginview.as_view(),name='login'),
     path('logout/', logoutview.as_view(), name='logout'),
     path('register',RegisterView.as_view(),name='register')
     
]
