from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('item/<int:item_id>/', views.item, name='item'),
]
