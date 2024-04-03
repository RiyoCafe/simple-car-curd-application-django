from django.urls import path
# import the CarViewSet from views
from .views import CarsViewset

urlpatterns = [
    path('cars/', CarsViewset.as_view()),
    path('cars/<int:id>/', CarsViewset.as_view()),
]