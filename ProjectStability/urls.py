"""ProjectStability URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include
# from courses import urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('courses.urls', namespace='courses')),
# ]

from django.contrib import admin
from django.urls import path
from candidate import views
from django.urls import path
from employer import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from candidate import views as candidate_views
from employer import views as employer_views
from candidate.views import CandidateSignUpView
from employer.views import EmployerSignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('candidate_signup/', candidate_views.candidate_signup, name='candidate_signup'),
    path('employer_signup/', employer_views.employer_signup, name='employer_signup'),
    # path('candidate/signup/', CandidateSignUpView.as_view(), name='candidate_signup'),
    # path('employer/signup/', EmployerSignUpView.as_view(), name='employer_signup'),
    path('', include('candidate.urls')),  # include candidate app URLs
    path('', include('employer.urls')),  # include employer app URLs
]

