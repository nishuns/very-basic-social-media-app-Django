from django.urls import path


# Write your Code Here
from . import views


#Adding Routes to the applications
urlpatterns=[
    path('',views.index, name="index"),   #default route
    path('signin',views.sign_in,name="signin"), #signin page route
    path('login',views.login_acc, name="login"), #signin route
    path('online',views.online,name="online"), #online
    path('logout',views.logout_acc,name="logout"), #signout routed
    path('create',views.create_acc,name="create"),#create account route
    path('signup',views.signup,name="signup"),#create account route
    path('<int:user_id>',views.visit,name="visitme")#profile visiting account 
]