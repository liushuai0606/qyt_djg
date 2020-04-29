from django.contrib import admin

from qyt_db.models import StudentsDB
from qyt_db.models import Courses
from qyt_db.models import CoursesList
from qyt_db.models import CoursesTeacher


admin.site.register(StudentsDB)
admin.site.register(Courses)
admin.site.register(CoursesList)
admin.site.register(CoursesTeacher)
