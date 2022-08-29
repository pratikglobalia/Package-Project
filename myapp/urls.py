from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('myactivity/', views.MyActivityView.as_view(), name='myactivity'),
    path('allactivity/', views.AllActivityView.as_view(), name='allactivity'),
    path('purchase/', views.PurchasePackageView.as_view(), name='purchase'),
]