from django.urls import path
from core import views

urlpatterns = [
    path('categoria/', views.CategoriasList.as_view(), name='get-list'),
    path('categoria/<int:id>/', views.CategoriaDetail.as_view(), name='get-id'),   
]