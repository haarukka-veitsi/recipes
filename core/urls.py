from django.conf import settings
from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.CatalogueView.as_view(), name='catalogue'),
    path('item/<int:item_id>/', views.ItemView.as_view(), name='item'),
    path('authorize/', views.AuthorizeView.as_view(), name='authorize'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('add_item', views.AddItemView.as_view(), name='add_item'),
]
