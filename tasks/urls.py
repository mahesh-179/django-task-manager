from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('changestatus/<int:id>/',views.change_status,name="change")

]
