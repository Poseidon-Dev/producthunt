from django.urls import path

from .views import signin, signout, signup

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
]
