from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="Home"),
    path('login/',views.login,name="Studentlogin"),
    path('register/',views.register,name="studentregister"),
    path('contactus/',views.contactus,name="contactus")
]