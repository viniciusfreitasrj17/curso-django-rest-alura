from typing import List

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, response, status, viewsets

from .models import Course, Matriculation, Student
from .serializer import (CourseSerializer, ListMatriculationCourseSerializer,
                         ListMatriculationStudentSerializer,
                         MatriculationSerializer, StudentSerializer,
                         StudentSerializerV2)


class StudentViewSet(viewsets.ModelViewSet):
    """CRUD students"""
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """CRUD courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names: List[str] = ['get', 'post', 'put', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = response.Response(
                serializer.data, status=status.HTTP_201_CREATED)
            data_id = str(serializer.data['id'])
            res['Location'] = request.build_absolute_uri() + data_id
            return res


class MatriculationViewSet(viewsets.ModelViewSet):
    """CRUD matriculations"""
    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer
    http_method_names: List[str] = ['get', 'post',
                                    'put', 'patch']  # exclude method delete

    @method_decorator(cache_page(20))  # cache for 20 seconds
    def dispatch(self, *args, **kwargs):
        return super(MatriculationViewSet, self).dispatch(*args, **kwargs)


class ListMatriculationStudent(generics.ListAPIView):
    """List Matriculation of Student"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListMatriculationStudentSerializer


class ListMatriculationCourse(generics.ListAPIView):
    """List Matriculation of Course"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListMatriculationCourseSerializer
