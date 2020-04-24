from django.shortcuts import render
from datetime import datetime
from qyt_db.models import Courses, CoursesList
import json


def qyt_summary(request):
    mytime = int(datetime.now().strftime("%w"))
    courses_list = []
    teacher_list = []
    for c in CoursesList.objects.all():
        courses_list.append(c.courses_name)
        teacher_list.append({'courses': c.courses_name, 'teacher': c.teacher.teacher})
    print(courses_list)
    print(teacher_list)
    return render(request, 'summary.html', locals())


def qyt_sec(request):
    c_info = Courses.objects.get(courses_name='安全')
    sec = {'方向': c_info.courses_name,
           '摘要': c_info.courses_summary,
           '授课老师': c_info.courses_teacher,
           '授课方式': c_info.courses_method,
           '课程特色': c_info.courses_characteristic,
           '是否提供实验环境': c_info.courses_provide_lab,
           '具体课程': json.loads(c_info.courses_detail)}
    return render(request, 'course.html', {'courseinfo': sec, 'datetime': datetime.now()})


def qyt_dc(request):
    c_info = Courses.objects.get(courses_name='数据中心')
    dc = {'方向': c_info.courses_name,
          '摘要': c_info.courses_summary,
          '授课老师': c_info.courses_teacher,
          '授课方式': c_info.courses_method,
          '课程特色': c_info.courses_characteristic,
          '是否提供实验环境': c_info.courses_provide_lab,
          '具体课程': json.loads(c_info.courses_detail)}
    return render(request, 'course.html', {'courseinfo': dc})

# def qyt_sec(request):
#     # sec_info = courses.objects.get(coureses)
#     return render(request, 'course.html', {'courseinfo': sec, 'datetime': datetime.now()})
#
#
# def qyt_dc(request):
#     return render(request, 'course.html', {'courseinfo': dc})