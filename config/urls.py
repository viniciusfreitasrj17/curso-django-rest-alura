"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from school.views import (
    StudentViewSet,
    CourseViewSet,
    MatriculationViewSet,
    ListMatriculationStudent,
    ListMatriculationCourse
)

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('matriculations', MatriculationViewSet,
                basename='Matriculations')

urlpatterns = [
    # trap
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # change route, security
    path('administrator/', admin.site.urls),

    path('', include(router.urls)),
    path('students/<int:pk>/matriculations/',
         ListMatriculationStudent.as_view()),
    path('courses/<int:pk>/matriculations/',
         ListMatriculationCourse.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
