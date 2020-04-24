# Come on! boy!

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()


course_list = {'安全', '数据中心', '路由', 'Python'}
teacher_list = [{'courses': '安全', 'teacher': '现任明教教主'},
                {'courses': '数据中心', 'teacher': '马海波'},
                {'courses': '路由', 'teacher': '安德'},
                {'courses': 'Python', 'teacher': '现任明教教主'},
                ]


from qyt_db.models import CoursesList, CoursesTeacher

# for x in course_list:
#     s = CoursesList(courses_name=x)
#     s.save()

# for y in teacher_list:
#     try:
#         course_info = CoursesList.objects.get(courses_name=y.get('courses'))
#         s = CoursesTeacher(course=course_info,
#                            teacher=y.get('teacher'))
#         s.save()
#     except CoursesList.DoesNotExist:
#         continue

for x in CoursesList.objects.all():
    print(x.teacher.teacher)


# sec = {'方向': '安全',
#        '摘要':'主要讲解网络安全知识',
#        '授课老师': '现任明教教主',
#        '授课方式': '在线,网真,本地',
#        '课程特色': '加入黑客技术',
#        '是否提供实验环境': '提供VPN访问云试验台',
#        '具体课程': ['FW', 'VPN', 'IDS', 'Hacker']}
#
# dc = {'方向': '数据中心',
#       '摘要': '主要讲解数据中心知识',
#       '授课老师': '马海波',
#       '授课方式': '在线,网真,本地',
#       '是否提供实验环境': '不提供分解试验台',
#       '具体课程': ['Nexus', 'UCS', 'Storage']}
#
# course_list = [sec, dc]
#
# from qyt_db.models import Courses
# import json
#
# for x in course_list:
#     s = Courses(courses_name=x.get('方向'),
#                 courses_summary=x.get('摘要'),
#                 courses_teacher=x.get('授课老师'),
#                 courses_method=x.get('授课方式'),
#                 courses_provide_lab=x.get('是否提供实验环境'),
#                 courses_detail=json.dumps(x.get('具体课程')),
#                 )
#     s.save()

# try:
#     sec_info = Courses.objects.get(courses_name='安全')
#     # sec_info.delete()
#     sec_info.courses_characteristic = '加入黑客技术'
#     sec_info.save()
# except Courses.DoesNotExist:
#     pass
# except Courses.MultipleObjectsReturned:
#     pass


# sec_info = Courses.objects.get(courses_name='安全')
# sec_info.courses_characteristic = '加入黑客技术'
# sec_info.save()
#
# # print(sec_info.courses_teacher)
# # for x in sec_info:
# #     print(x.courses_teacher)
# sec_info.delete()