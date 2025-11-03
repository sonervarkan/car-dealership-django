from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add-car/', views.add_car, name='add_car'),
    path('get_models_by_brand/', views.get_models_by_brand, name='get_models_by_brand'),
    path('get_gear_type_by_model_brand/', views.get_gear_type_by_model_brand, name='get_gear_type_by_model_brand'),
    path('get_fuel_type_by_brand_model_gear_type/', views.get_fuel_type_by_brand_model_gear_type, name='get_fuel_type_by_brand_model_gear_type'),
    path('get_filter_results/', views.get_filter_results, name='get_filter_results'),
]