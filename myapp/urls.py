from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    
    # Auto CRUD
    path('autos/', views.auto_list, name='auto-list'),
    path('autos/create/', views.auto_create, name='auto-create'),
    path('autos/<int:pk>/', views.auto_detail, name='auto-detail'),
    path('autos/<int:pk>/edit/', views.auto_update, name='auto-update'),
    path('autos/<int:pk>/delete/', views.auto_delete, name='auto-delete'),
]
