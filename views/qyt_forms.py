# Come on! boy!

from qyt_db.models import StudentsDB
from django.http import HttpResponseRedirect
from django.shortcuts import render
from qyt_db.forms import StudentsForm

def addstudent(request):
    if request.method == 'POST':
        pass
        # form = StudentsForm(request.POST)
        # # 如果请求为POST，并且Form校验通过，把新添加的学员信息写入数据库
        # if form.is_valid():
        #     s1 = StudentsDB(name=request.POST.get('name'),
        #                     phone_number=request.POST.get('phone_number'),
        #                     qq_number=request.POST.get('qq_number'),
        #                     mail=request.POST.get('mail'),
        #                     direction=request.POST.get('direction'),
        #                     class_adviser=request.POST.get('class_adviser'),
        #                     payed=request.POST.get('payed'))
        #     s1.save()
        #     # 写入成功后，重定向返回展示所有学员信息的页面
        #     return HttpResponseRedirect('/showstudents/')
        # else:  # 如果Form校验失败，返回客户在Form中输入的内容和报错信息
        #     # 如果检查到错误，会添加错误内容到Form内，例如：<ul class="errorlist"><li>(X)号码已经存在</li></ul>
        #     return render(request, 'addstudent.html', {'form': form})
    else:  # 如果不是POST，就是GET，表示为初始访问，显示表单内容给客户
        form = StudentsForm()
        return render(request, 'addstudent.html', {'form': form})
