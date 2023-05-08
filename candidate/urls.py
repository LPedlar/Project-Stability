from django.urls import path
from . import views
from candidate import views as candidate_views
from .views import CandidateSignUpView

app_name = 'candidate'

urlpatterns = [
    path('', views.candidate_home, name='home'),
    path('profile/', views.candidate_profile, name='candidate_profile'),
    path('job_list/', views.job_list, name='job_list'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job_pipeline/', views.job_pipeline, name='job_pipeline'),
    path('signup/', CandidateSignUpView.as_view(), name='candidate_signup'),
    path('signin/', candidate_views.candidate_signin, name='candidate_signin'),
    path('candidate_home/', views.candidate_home, name='candidate_home'),
    path('logout/', views.candidate_logout, name='candidate_logout'),
    # other URL patterns go here
]
