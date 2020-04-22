from django.shortcuts import render
from datetime import datetime


sec = {'方向': '安全',
       '摘要':'主要讲解网络安全知识',
       '授课老师': '现任明教教主',
       '授课方式': '在线,网真,本地',
       '课程特色': '加入黑客技术',
       '是否提供实验环境': '提供VPN访问云试验台',
       '具体课程': ['FW', 'VPN', 'IDS', 'Hacker']}

dc = {'方向': '数据中心',
      '摘要': '主要讲解数据中心知识',
      '授课老师': '马海波',
      '授课方式': '在线,网真,本地',
      '是否提供实验环境': '不提供分解试验台',
      '具体课程': ['Nexus', 'UCS', 'Storage']}


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



def qyt_sec(request):
    return render(request, 'course.html', {'courseinfo': sec})

def qyt_dc(request):
    return render(request, 'course.html', {'courseinfo': dc})
