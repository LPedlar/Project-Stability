from django.urls import path
from . import views
from candidate import views as candidate_views
from employer import views as employer_views
from .views import EmployerSignUpView

app_name = 'employer'

urlpatterns = [
    #path('signup/', employer_views.employer_signup, name='employer_signup'),
    #path('signup/', employer_views.employer_signup, name='employer_signup'),
    path('signup/', EmployerSignUpView.as_view(), name='employer_signup'),
    path('signin/', employer_views.employer_signin, name='employer_signin'),
    path('employer_home/', views.employer_home, name='employer_home'),
    path('employer_profile/', views.employer_profile, name='profile'),
    path('job_post/', views.job_post, name='job_post'),
    path('job_list/', views.job_list, name='job_list'),
    path('profile/', views.employer_profile, name='employer_profile'),
    path('logout/', views.employer_logout, name='employer_logout'),
    # other paths for employer app viewsCandidateSignUpView.as_view()
]