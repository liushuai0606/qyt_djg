from django.shortcuts import render
from datetime import datetime
from qyt_db.models import Courses
import json


def qyt_summery(request):
    mytime = int(datetime.now().strftime("%w"))
    # mytime = int(datetime.strptime('2018-08-05','%Y-%m-%d').strftime("%w"))

    course_list = {'安全', '数据中心', '路由', 'Python'}
    teacher_list = [{'courses': '安全', 'teacher': '现任明教教主'},
                    {'courses': '数据中心', 'teacher': '马海波'},
                    {'courses': '路由交换', 'teacher': '安德'},
                    {'courses': '教主VIP', 'teacher': '现任明教教主'},
                    ]

    return render(request, 'summery.html', locals())


# def qyt_sec(request):
#     # sec_info = courses.objects.get(coureses)
#     return render(request, 'course.html', {'courseinfo': sec, 'datetime': datetime.now()})
#
#
# def qyt_dc(request):
#     return render(request, 'course.html', {'courseinfo': dc})


def qyt_sec(request):
    c_info = Courses.objects.get(coureses_name='安全')
    sec = {'方向': c_info.courses_name,
           '摘要': c_info.courses_summary,
           '授课老师': c_info.courses_teacher,
           '授课方式': c_info.courses_method,
           '课程特色': c_info.courses_characteristic,
           '是否提供实验环境': c_info.courses_provide_lab,
           '具体课程': json.loads(c_info.courses_detail)}
    return render(request, 'course.html', {'courseinfo': sec, 'datetime': datetime.now()})


def qyt_dc(request):
    c_info = Courses.objects.get(coureses_name='数据中心')
    dc = {'方向': c_info.courses_name,
          '摘要': c_info.courses_summary,
          '授课老师': c_info.courses_teacher,
          '授课方式': c_info.courses_method,
          '课程特色': c_info.courses_characteristic,
          '是否提供实验环境': c_info.courses_provide_lab,
          '具体课程': json.loads(c_info.courses_detail)}
    return render(request, 'course.html', {'courseinfo': dc})
