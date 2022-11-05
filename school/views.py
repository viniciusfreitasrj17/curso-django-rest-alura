from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Course, Student, Matriculation
from .serializer import (
    StudentSerializer,
    CourseSerializer,
    MatriculationSerializer,
    ListMatriculationStudentSerializer,
    ListMatriculationCourseSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    """CRUD students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """CRUD courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculationViewSet(viewsets.ModelViewSet):
    """CRUD matriculations"""
    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListMatriculationStudent(generics.ListAPIView):
    """List Matriculation of Student"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListMatriculationStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListMatriculationCourse(generics.ListAPIView):
    """List Matriculation of Course"""

    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListMatriculationCourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
