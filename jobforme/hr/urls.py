from django.urls import path
from hr import views
urlpatterns = [
    path('hrdash/',views.hrHome,name='hrdash'),
    path('postjob/',views.post_job,name='postjob'),    
    path('candidate/<int:pk>/',views.candidate_view,name='candidate-details'),
    path('select-candidate/',views.selectCandidate,name='selectCandidate'),
    path('delete-candidate/',views.deleteCandidate,name='deleteCandidate')
]