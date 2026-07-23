from . import views
from django.urls import path

urlpatterns = [
    path('', views.welcome,name="welcome"),
    path('home/',views.home,name="home"),
    path('changestatus/<int:id>/',views.change_status,name="change"),
    path('create/',views.create_task,name="create_task"),
    path('update/<int:id>/',views.update_task,name="update",),
    path('create_profile/',views.profile_pic,name="profile_pic"),
    path('profile/<int:id>/',views.profile_display,name="profile"),

]
