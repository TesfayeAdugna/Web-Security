from django.urls import path
from login_app import views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("register/", views.render_register, name="render_register")
]
