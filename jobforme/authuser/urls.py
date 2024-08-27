from django.urls import path
from authuser import views
urlpatterns = [
    path('candidate-register/',views.register_candidate,name='registerCandidate'),
    path('hr-register/',views.register_hr,name='registerHR'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logoutUser,name='logout')
]