from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('question/<int:id>/', views.question, name="question"),
    path('check_answer/', views.check_answer, name="check_answer"),
    path('login/', views.Login, name="Login"),
    path('logout/', views.Logout, name="Logout"),
    path('signup/', views.signup, name="signup")
]
