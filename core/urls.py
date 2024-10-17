from django.conf import settings
from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('item/<int:item_id>/', views.item, name='item'),
    path('authorize/', views.AuthorizeView.as_view(), name='authorize'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile')
]
