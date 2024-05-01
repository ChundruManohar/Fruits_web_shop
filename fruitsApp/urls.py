from django.urls import path
from fruitsApp.views import add_fruit,list_fruits,update_fruit,fruits_delete

urlpatterns = [
    path('add/',add_fruit),
    path('listFruits/',list_fruits),
    path('update/<int:id>/',update_fruit),
    path('delete/<int:id>/',fruits_delete),
]