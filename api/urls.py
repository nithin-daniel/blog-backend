from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Sample.as_view(),name='sample')
]