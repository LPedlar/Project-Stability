# from django.urls import include, path
# from courses import views

# app_name = 'courses'

# urlpatterns = [
#     path('', views.courses_view, name = 'courses'),
#     path('<int:pk>/', views.course_detail, name='course_detail'),
# ]

from django.urls import path
from . import views
from candidate import views as candidate_views
from employer import views as employer_views

app_name = 'employer'

urlpatterns = [
    path('signup/', views.employer_signup, name='employer_signup'),
    #path('signup/', employer_views.employer_signup, name='employer_signup'),
    path('signin/', views.employer_signin, name='employer_signin'),
    path('employer_home/', views.employer_home, name='employer_home'),
    path('employer_profile/', views.employer_profile, name='profile'),
    path('job_post/', views.job_post, name='job_post'),
    path('job_list/', views.job_list, name='job_list'),
    # other paths for employer app views
]