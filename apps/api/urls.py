from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hello-world'),
    # path('hello/', views.HelloWorld.as_view(), name='hello'),
]
