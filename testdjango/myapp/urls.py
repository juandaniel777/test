from django.urls import path
#from .views import update_user
from .views import *
#from .views import register_view
urlpatterns = [
    
     path('user_model/', user_model, name='user_model'),
    
     path('',home,name='home')
]