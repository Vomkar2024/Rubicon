from django.contrib import admin
from django.urls import path
from main import views


admin.site.site_header = "Musafir Cafe Admin"
admin.site.site_title = "Musafir Cafe Admin Portal"
admin.site.index_title = "Welcome to Musafir Cafe Researcher Portal"

urlpatterns = [
    path("",views.index,name="main"),
    path("menu",views.Menu,name="menu"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact")
]
