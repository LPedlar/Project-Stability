from django.urls import path
from . import views
from candidate import views as candidate_views
from .views import CandidateSignUpView

app_name = 'candidate'

urlpatterns = [
    path('', views.candidate_home, name='home'),
    path('profile/', views.candidate_profile, name='candidate_profile'),
    #path('signup/', views.candidate_signup, name='candidate_signup'),
    #path('signup/', candidate_views.candidate_signup, name='candidate_signup'),
    path('signup/', CandidateSignUpView.as_view(), name='candidate_signup'),
    path('signin/', candidate_views.candidate_signin, name='candidate_signin'),
    path('candidate_home/', views.candidate_home, name='candidate_home'),
    path('logout/', views.candidate_logout, name='candidate_logout'),
    # other URL patterns go here
]
