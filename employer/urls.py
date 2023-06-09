from django.urls import path
from . import views
from candidate import views as candidate_views
from employer import views as employer_views
from .views import EmployerSignUpView

app_name = 'employer'

urlpatterns = [
    path('signup/', EmployerSignUpView.as_view(), name='employer_signup'),
    path('signin/', employer_views.employer_signin, name='employer_signin'),
    path('employer_home/', views.employer_home, name='employer_home'),
    path('employer_profile/', views.employer_profile, name='profile'),
    path('job_post/', views.job_post, name='job_post'),
    path('job_list/', views.job_list, name='job_list'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('profile/', views.employer_profile, name='employer_profile'),
    path('logout/', views.employer_logout, name='employer_logout'),
    # other paths for employer app viewsCandidateSignUpView.as_view()
    path('user_pipeline/', views.user_pipeline, name='user_pipeline'),
    path('applications/', views.applications, name='applications'),
    path('interview/', views.interview, name='interview'),
    path('approved/', views.approved, name='approved'),
    path('position_requests/', views.position_request, name='position_requests'),
    path('hired/', views.hired, name='hired'),
    path('update1/<int:application_id>', views.update1, name='update1'),
    path('update2/<int:application_id>', views.update2, name='update2'),
    path('hire/<int:application_id>', views.hire, name='hire'),
    path('decline/<int:application_id>', views.decline, name='decline'),
    path('fire/<int:application_id>', views.fire, name='fire'),
]