from django.urls import path
from .views import home,courses,bootcamp,signin

app_name='app1'

urlpatterns = [
    path('',home),
    path('courses/',courses,name='courses'),
    path('kodr/',bootcamp,name='kodr'),
    path('signin/',signin,name='signin')
]
