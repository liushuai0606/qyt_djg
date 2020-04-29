# Come on! boy!

from django import forms
from django.core.validators import RegexValidator
from qyt_db.models import StudentsDB


class StudentsForm(forms.Form):
    # 为了添加必须选项前面的星号
    # 下面是模板内的内容
    """"
    < style type = "text/css" >
    label.required::before
    {
        content: "*";
    color:red;
    }
    < / style >
    """
    required_css_class = 'required' # 这是Form.required_css_class属性， use to add class attributes to required rows
    # 添加效果如下
    # <label class="required" for = "id_name">学员姓名；</label>
    # 不添加效果如下
    # <label for="id_name">学员姓名；</label>

    # 学员姓名，最小长度2，最大长度10
    # label后面填写的内容，在表单中显示为名字，
    # 必选（required = True 其实是默认值）
    # attrs="class":"form-control") 主要作用是style it in Bootstrap
    name = forms.CharField(max_length=10,
                           min_length=2,
                           label='学员姓名',
                           required=True,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    # 对电话号码进行交易，交易以1开头的11位数字
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="手机号码需要使用11位数字，例如:'13911153335'")
    phone_number = forms.CharField(validators=[phone_regex],
                                   min_length=11,
                                   max_length=11,
                                   label='手机号码',
                                   required=True,
                                   widget=forms.NumberInput(attrs={"class": "form-control"}))
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ号码需要使用5到20位数字，例如:'605658506'")
    qq_number = forms.CharField(validators=[qq_regex],
                                min_length=5,
                                max_length=20,
                                label='QQ号码',
                                required=True,
                                widget=forms.NumberInput(attrs={"class": "form-control"}))
    mail = forms.EmailField(required=False,
                            label='Email地址',
                            error_messages={'invalid': '请输入正确格式的电子邮件地址'},
                            widget=forms.EmailInput(attrs={"class": "form-control"}))
    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = forms.CharField(max_length=10,
                                label='学习方向',
                                widget=forms.Select(choices=direction_choices,
                                                    attrs={"class": "form-control"}))
    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = forms.CharField(max_length=10,
                                    label='班主任',
                                    widget=forms.Select(choices=class_adviser_choices,
                                                        attrs={"class": "form-control"}))
    payed_choices = (('已缴费', '已缴费'), ('未交费', '未交费'))
    payed = forms.CharField(max_length=10,
                            label='缴费情况',
                            widget=forms.Select(choices=payed_choices,
                                                attrs={"class": "form-control"}))

    def clean_phone_number(self):  # 对电话号码的唯一性进行校验，注意格式为clean+校验遍历
        phone_number = self.cleaned_data['phone_number']  # 提取客户输入的电话号码
        # 在数据库中查找是否存在这个电话号
        existing = StudentsDB.objects.filter(
            phone_number=phone_number
        ).exists()
        # 如果存在就显示校验错误信息
        if existing:
            raise forms.ValidationError("电话号码已经存在")
        # 如果校验成功就返回电话号码
        return phone_number

    def clean_qq_number(self):
        qq_number = self.cleaned_data['qq_number']
        existing = StudentsDB.objects.filter(
            qq_number=qq_number
        ).exists()

        if existing:
            raise forms.ValidationError("QQ号码已经存在")
        return qq_number

class EditStudents(forms.Form):
    required_css_class = 'required'
    # 会给编辑账号人员显示客户唯一ID（数据库的唯一ID)，但是这个ID为制度'readonly'：True
    id = forms.CharField(label='学员唯一ID',
                         widget=forms.TextInput(attrs={"class": "form-control", 'readonly': True}))
    name = forms.CharField(max_length=50,
                           min_length=2,
                           label='学员姓名',
                           required=True,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="手机号码需要使用11位数字，例如：“13911153335”")
    phone_number = forms.CharField(validators=[phone_regex],
                                   min_length=11,
                                   max_length=11,
                                   label="手机号码",
                                   required=True,
                                   widget=forms.NumberInput(attrs={"class": "form-control"}))
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ号码需要使用5到20位数字，例如：“0605658506”")
    qq_number = forms.CharField(validators=[qq_regex],
                                min_length=5,
                                max_length=20,
                                label='QQ号码',
                                required=True,
                                widget=forms.NumberInput(attrs={"class": "form-control"}))
    mail = forms.EmailField(required=False,
                            label='Email地址',
                            error_messages={'invalid': '请输入正确格式的电子邮件地址'},
                            widget=forms.EmailInput(attrs={"class": "form-control"}))
    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = forms.CharField(max_length=10,
                                label='学习方向',
                                widget=forms.Select(choices=direction_choices,
                                                    attrs={"class": "form-control"}))
    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = forms.CharField(max_length=10,
                                    label='班主任',
                                    widget=forms.Select(choices=class_adviser_choices,
                                                        attrs={"class": "form-control"}))
    payed_choices = (('已缴费', '已缴费'), ('未交费', '未交费'))
    payed = forms.CharField(max_length=10,
                            label='缴费情况',
                            widget=forms.Select(choices=payed_choices,
                                                attrs={"class": "form-control"}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # 在编辑的时候，校验电话号码与创建不通，因为其实数据库里边已经有一个自己这个条目的电话号码了！
        # 所以要排除自己ID禅道的电话号码，如果其他ID已让存在形同的电话号码，就校验失败
        count = 0
        for i in StudentsDB.objects.filter(phone_number=phone_number):
            if int(i.id) != int(self.cleaned_data['id']):
                count += 1

        if count >= 1:
            raise forms.ValidationError("电话号码已经存在")
        # 如果校验成功就返回电话号码
        return phone_number

    def clean_qq_number(self):
        qq_number = self.cleaned_data['qq_number']

        count = 0
        for i in StudentsDB.objects.filter(qq_number=qq_number):
            if int(i.id) != int(self.cleaned_data['id']):
                count += 1

        if count >=1:
            raise forms.ValidationError("QQ号码已经存在")
        return qq_number


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
                               )
    password = forms.CharField(label='密码',
                               max_length=100,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"})
                               )
