from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('create/', views.UserView.as_view(), name='create-user'),
    path('login/', views.AuthToken.as_view(), name='login'),
    path('me/', views.UpdateUserView.as_view(), name='update')
]
