from django.contrib import admin
from .models import Course, Student, Matriculation

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_day')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page: int = 20


admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'cod', 'description')
    list_display_links = ('id', 'cod')
    search_fields = ('cod',)


admin.site.register(Course, CourseAdmin)


class MatriculationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)


admin.site.register(Matriculation, MatriculationAdmin)
