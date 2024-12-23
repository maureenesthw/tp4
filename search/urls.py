from django.urls import path
from search.views import *

app_name = 'search'

urlpatterns = [
   path('', search, name='search'),
   path('home', home, name='search'),
   path('hi', hi, name='search')

]