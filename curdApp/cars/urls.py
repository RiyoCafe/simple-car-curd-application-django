from django.urls import path
# import the CarViewSet from views
from cars import views

urlpatterns = [
    path('cars/', views.list_cars, name='list_cars'),
    path('cars/add/',views.add_car, name='add_car'),
    path('cars/<int:id>/', views.get_car_by_id, name='get_car_by_id'),
    path('cars/update/<int:id>/', views.update_car, name='update_car'),
    path('cars/delete/<int:id>/', views.delete_car, name='delete_car'),
]