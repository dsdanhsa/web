from django.urls import path

from login import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('register',views.register, name="register"),
    path('process_login', views.process_login, name="process_login"),
    path('process_regis', views.process_regis, name="process_regis"),
]