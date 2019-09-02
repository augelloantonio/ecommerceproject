from django.urls import path, include
from .views import logout, login, register, profile
from . import url_reset

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('reset-password/', include(url_reset))
]
