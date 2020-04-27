# Come on! boy!

from qyt_db.models import StudentsDB
from django.http import HttpResponseRedirect
from django.shortcuts import render
from qyt_db.forms import StudentsForm, EditStudents
from pprint import pprint

def addstudent(request):
    if request.method == 'POST':
        # pass
        form = StudentsForm(request.POST)
        # 如果请求为POST，并且Form校验通过，把新添加的学员信息写入数据库
        if form.is_valid():
            s1 = StudentsDB(name=request.POST.get('name'),
                            phone_number=request.POST.get('phone_number'),
                            qq_number=request.POST.get('qq_number'),
                            mail=request.POST.get('mail'),
                            direction=request.POST.get('direction'),
                            class_adviser=request.POST.get('class_adviser'),
                            payed=request.POST.get('payed'))
            s1.save()
            # 写入成功后，重定向返回展示所有学员信息的页面
            # return HttpResponseRedirect('/showstudents/')
            form = StudentsForm()
            return render(request, 'addstudent.html', {'form': form, 'successmessage': '添加学员成功！'})
        else:  # 如果Form校验失败，返回客户在Form中输入的内容和报错信息
            # 如果检查到错误，会添加错误内容到Form内，例如：<ul class="errorlist"><li>(X)号码已经存在</li></ul>
            return render(request, 'addstudent.html', {'form': form})
    else:  # 如果不是POST，就是GET，表示为初始访问，显示表单内容给客户
        form = StudentsForm()
        return render(request, 'addstudent.html', {'form': form})


def showstudents(request):
    # 查询整个数据库的信息，object.all()
    result = StudentsDB.objects.all()
    # 最终得到学员清单students_list,清淡内部是每个学员信息的字典
    students_list = []
    for x in result:
        # 产生学员信息的字典
        students_dict= {}
        # 为了不再模板中拼接字符串，提前为删除和编辑页面产生URL
        students_dict['id_delete'] = "/deletestudent/" + str(x.id)
        students_dict['id_edit'] = "/editstudent/" + str(x.id)

        # 提取学员详细信息，并写入字典
        students_dict['id'] = x.id
        students_dict['name'] = x.name
        students_dict['phone_number'] = x.phone_number
        students_dict['qq_number'] = x.qq_number
        students_dict['mail'] = x.mail
        students_dict['direction'] = x.direction
        students_dict['class_adviser'] = x.class_adviser
        students_dict['payed'] = x.payed
        students_dict['date'] = x.date.strftime('%Y-%m-%d')
        students_list.append(students_dict)
    # pprint(students_list, indent=4)

    return render(request, 'showstudents.html', {'students_list': students_list})


def deletestudent(request, id):
    # 获取对应ID的学员
    try:
        m = StudentsDB.objects.get(id=id)
        # 从数据库中删除学员条目
        m.delete()

        result = StudentsDB.objects.all()
        # 最终得到学员清单students_list,清淡内部是每个学员信息的字典
        students_list = []
        for x in result:
            # 产生学员信息的字典
            students_dict = {}
            # 为了不再模板中拼接字符串，提前为删除和编辑页面产生URL
            students_dict['id_delete'] = "/deletestudent/" + str(x.id)
            students_dict['id_edit'] = "/editstudent/" + str(x.id)

            # 提取学员详细信息，并写入字典
            students_dict['id'] = x.id
            students_dict['name'] = x.name
            students_dict['phone_number'] = x.phone_number
            students_dict['qq_number'] = x.qq_number
            students_dict['mail'] = x.mail
            students_dict['direction'] = x.direction
            students_dict['class_adviser'] = x.class_adviser
            students_dict['payed'] = x.payed
            students_dict['date'] = x.date.strftime('%Y-%m-%d')
            students_list.append(students_dict)
        # pprint(students_list, indent=4)

        return render(request, 'showstudents.html', {'students_list': students_list,'successmessage':'删除学员成功！'})

    except StudentsDB.DoesNotExist:
        result = StudentsDB.objects.all()
        # 最终得到学员清单students_list,清淡内部是每个学员信息的字典
        students_list = []
        for x in result:
            # 产生学员信息的字典
            students_dict = {}
            # 为了不再模板中拼接字符串，提前为删除和编辑页面产生URL
            students_dict['id_delete'] = "/deletestudent/" + str(x.id)
            students_dict['id_edit'] = "/editstudent/" + str(x.id)

            # 提取学员详细信息，并写入字典
            students_dict['id'] = x.id
            students_dict['name'] = x.name
            students_dict['phone_number'] = x.phone_number
            students_dict['qq_number'] = x.qq_number
            students_dict['mail'] = x.mail
            students_dict['direction'] = x.direction
            students_dict['class_adviser'] = x.class_adviser
            students_dict['payed'] = x.payed
            students_dict['date'] = x.date.strftime('%Y-%m-%d')
            students_list.append(students_dict)
        # pprint(students_list, indent=4)

        return render(request, 'showstudents.html', {'students_list': students_list, 'errormessage':'没有找到指定学员！'})


def getstudentinfo(id):
    # 设置过滤条件，获取特定学员信息，objects.get(id=id）
    result = StudentsDB.objects.get(id=id)
    students_dict = {}
    students_dict['id'] = result.id
    students_dict['name'] = result.name
    students_dict['phone_number'] = result.phone_number
    students_dict['qq_number'] = result.qq_number
    students_dict['mail'] = result.mail
    students_dict['direction'] = result.direction
    students_dict['class_adviser'] = result.class_adviser
    students_dict['payed'] = result.payed
    students_dict['date'] = result.date
    # 返回特定学员详细信息
    return students_dict

def editstudent(request, id):
    # 首先获取特定ID学员详细信息
    infodict = getstudentinfo(id)
    if request.method == 'POST':
        form = EditStudents(request.POST)
        # 如果请求为POST，并且Form校验通过，把修改的学员信息写入数据库
        if form.is_valid():
            m = StudentsDB.objects.get(id=id)
            m.name = request.POST.get('name')
            m.phone_number = request.POST.get('phone_number')
            m.qq_number = request.POST.get('qq_number')
            m.mail = request.POST.get('mail')
            m.direction = request.POST.get('direction')
            m.class_adviser = request.POST.get('class_adviser')
            m.payed = request.POST.get('payed')
            m.save()
            # 写入成功后，重定向返回展示所有学员信息的页面
            infodict = getstudentinfo(id)
            form = EditStudents(initial={'id': infodict['id'],  # initial填写初始值
                                         'name': infodict['name'],
                                         'phone_number': infodict['phone_number'],
                                         'qq_number': infodict['qq_number'],
                                         'mail': infodict['mail'],
                                         'direction': infodict['direction'],
                                         'class_adviser': infodict['class_adviser'],
                                         'payed': infodict['payed']})
            return render(request, 'editstudent.html', {'form': form,
                                                        'successmessage': '修改成功！'})

        else:  # 如果Form校验失败，返回客户在Form中输入的内容和报错信息
            return  render(request, 'editstudent.html', {'form': form})
    else:   # 如果不是POST，就是GET，表示为初始访问，吧特定ID客户在数据库中的值，通过初始值的方式展现给客户看
        form = EditStudents(initial={'id': infodict['id'],  #  initial填写初始值
                                     'name': infodict['name'],
                                     'phone_number': infodict['phone_number'],
                                     'qq_number': infodict['qq_number'],
                                     'mail': infodict['mail'],
                                     'direction': infodict['direction'],
                                     'class_adviser': infodict['class_adviser'],
                                     'payed': infodict['payed']})
        return render(request, 'editstudent.html', {'form': form})