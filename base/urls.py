from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('submitQuery',views.submitquery,name='submitquery')
]
