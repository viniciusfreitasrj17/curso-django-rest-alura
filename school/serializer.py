from rest_framework import serializers
from .models import Student, Course, Matriculation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_day']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class MatriculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculation
        exclude = []  # like: fields = '__all__'


class ListMatriculationStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Matriculation
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class ListMatriculationCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    student_id = serializers.ReadOnlyField(source='student.id')

    class Meta:
        model = Matriculation
        fields = ['student_id', 'student_name']


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'phone', 'rg', 'cpf', 'birth_day']
