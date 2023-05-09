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
    path('interested_detail/<int:job_id>/', views.int_detail, name='interested_detail'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    path('apply_interested/<int:job_id>/', views.apply_interested, name='apply_interested'),
    path('save/<int:job_id>/', views.save, name='save'),
    path('save_interested/<int:job_id>/', views.save_interested, name='save_interested'),
    path('application_confirmation/<int:job_id>/', views.apply_confirm, name='application_confirmation'),
    path('job_pipeline/', views.job_pipeline, name='job_pipeline'),
    path('interested/', views.interested, name='interested'),
    path('in_review/', views.in_review, name='in_review'),
    path('approved/', views.approved, name='approved'),
    path('dormant/', views.dormant, name='dormant'),
    path('declined/', views.declined, name='declined'),
    path('signup/', CandidateSignUpView.as_view(), name='candidate_signup'),
    path('signin/', candidate_views.candidate_signin, name='candidate_signin'),
    path('candidate_home/', views.candidate_home, name='candidate_home'),
    path('logout/', views.candidate_logout, name='candidate_logout'),
    path('update0/<int:application_id>', views.update0, name='update0'),
    # other URL patterns go here
]
