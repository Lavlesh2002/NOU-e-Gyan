from django.urls import path
from . import views
urlpatterns = [
    path('',views.addash,name="dash"),
    path('news/',views.news,name="news"),
    path('news/<id>',views.delnews,name="delnews"),
    path('editnews/<id>',views.editnews,name="editnews"),
    path('program/',views.program,name="program"),
    path('editprogram/<id>',views.editprogram,name="editprogram"),
    path('program/<id>',views.delprogram,name="delprogram"),
    path('branch/',views.branch,name="branch"),
    path('editbranch/<id>',views.editbranch,name="editbranch"),
    path('branch/<id>',views.delbranch,name="delbranch"),
    path('year/',views.year,name="year"),
    path('edityear/<id>',views.edityear,name="edityear"),
    path('year/<id>',views.delyear,name="delyear"),
    path('logout/',views.logout,name="logout"),
    path('viewstudent/', views.viewstudent, name="viewstudent"),
    path('studymaterial/',views.studymaterial,name="studymaterial"),
    path('editstudent/<email>',views.editstudent,name="editstudent"),
    path('delstudent/<email>',views.delstudent,name="delstudent"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('delfeedback/<id>',views.delfeedback,name="delfeedback"),
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('viewenquiry',views.viewenquiry,name="viewenquiry"),
    path('delenquiry/<id>',views.delenquiry,name="delenquiry"),
    path('delstudy/<id>',views.delstudy,name="delstudy")

]