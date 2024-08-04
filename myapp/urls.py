from django.urls import path
from . import views



urlpatterns = [


    path('home/',views.home),
    path('info/',views.information),
    path('home1/',views.home1),
    path('home2/',views.home2),



    path('students/',views.students),   # All urls to students management
    path('update/',views.update),
    path('addstudent/',views.addstudent),
    path('submitstudent/',views.submitstudent),
    path('allstudents/',views.allstudents),




    path('library/',views.library),      # All urls to library management 
    path('addbook/',views.addbook),
    path('updatebook/',views.updatebook),
    path('deletebook/',views.deletebook),
    path('seeallbook/',views.seeallbook),
    path('addmember/',views.addmember),
    path('updatemember/',views.updatemember),
    path('deletemember/',views.deletemember),
    path('seeallmember/',views.seeallmember),
    path('addrecord/',views.addrecord),
    path('updaterecord/',views.updaterecord),
    path('deleterecord/',views.deleterecord),
    path('seeallrecord/',views.seeallrecord),







    path('usersignup/',views.usersignup),    # All urls to Authenticate/Authentication
    path('handlesignup/',views.handlesignup),
    path('userlogin/',views.userlogin),
    path('handlelogin/',views.handlelogin),
    path('userlogout/',views.userlogout)


    
    
]