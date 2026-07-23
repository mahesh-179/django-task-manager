from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome,name="welcome"),
    path('home/',views.home,name="home"),
    path('changestatus/<int:id>/',views.change_status,name="change"),
    path('create/',views.create_task,name="create_task"),
    path('update/',views.update_task,name="update",)

]
