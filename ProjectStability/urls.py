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
from employer.views import EmployerCandidateSignUpView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ProjectStability'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EmployerCandidateSignUpView.as_view(), name='home'),
    path('candidate/', include('candidate.urls')),  # include candidate app URLs
    path('employer/', include('employer.urls')),  # include employer app URLs
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

