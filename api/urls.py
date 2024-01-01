# in this we will map all the views created 
from django.urls import path
from api import views

urlpatterns=[
    path('',views.Notelist.as_view(),name='Notelist'),
    path('<int:pk>/',views.Notedetail.as_view(),name='Notedetail'),
]
# in this we are going to include the result of and it will get displayed in the screen