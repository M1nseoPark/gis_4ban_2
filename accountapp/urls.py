from django.urls import path

from accountapp.views import bye_world

app_name = 'accountapp'

urlpatterns = [
    path('bye_world/', bye_world, name='bye_world'),
]