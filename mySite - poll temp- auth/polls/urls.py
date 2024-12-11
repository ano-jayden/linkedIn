

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('poll/<int:poll_id>/', views.detail, name='detail'),
    path('poll/<int:poll_id>/vote/', views.vote, name='vote'),
    path('poll/<int:poll_id>/results/', views.results, name='results'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
