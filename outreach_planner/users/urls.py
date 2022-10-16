from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
<<<<<<< HEAD
    #path('register_user', views.register_user, name="register")
=======
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register")
>>>>>>> 133e148aaad43b30af45617fb6f879225871eb13
]
