from django.urls import path
from . import views
from candidate import views as candidate_views

app_name = 'candidate'

urlpatterns = [
    path('', views.candidate_home, name='home'),
    path('candidate_profile/', views.candidate_profile, name='profile'),
    #path('signup/', views.candidate_signup, name='candidate_signup'),
    path('signup/', candidate_views.candidate_signup, name='candidate_signup'),
    path('candidate_home/', views.candidate_home, name='candidate_home'),
    # other URL patterns go here
]
