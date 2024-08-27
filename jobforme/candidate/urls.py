from django.urls import path
from candidate import views
urlpatterns = [
    path('candidate-dashboard/',views.candidate_dashboard,name='candidate_dashboard'),
    path('my-job-list/',views.myJobListViews,name='myJobListViews'),
    path('apply-for-job/<int:pk>/',views.applyforjobs,name='applyforjob')
]