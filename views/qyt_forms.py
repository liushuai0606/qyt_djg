# Come on! boy!

from qyt_db.models import StudentsDB
from django.http import HttpResponseRedirect
from django.shortcuts import render
from qyt_db.forms import StudentsForm
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