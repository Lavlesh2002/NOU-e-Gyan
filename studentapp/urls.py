from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="dash"),
    path('logout/',views.logout,name="logout"),
    path('studymaterial/',views.studymaterial,name="studymaterial"),
    path('givefeedback/',views.givefeedback,name="feedback"), 
    path('complaint/',views.complaint,name="complaint"),
    path('delcomplaint/<id>',views.delcomplaint,name="delcomplaint"),
    path('viewnews/',views.viewnews,name="viewnews"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('addquestions',views.addquestions,name="addquestions"),
    path('delques/<id>',views.delques,name="delques"),
    path('disforum/',views.disforum,name="disforum"),
    path('uploadanswer/<id>',views.uploadanswer,name="uploadanswer")
]