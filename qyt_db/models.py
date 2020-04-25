from django.db import models
from django.core.validators import RegexValidator


class Courses(models.Model):
    courses_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='课程名')
    courses_summary = models.CharField(max_length=10000, blank=False)
    courses_teacher = models.CharField(max_length=100, blank=False)
    courses_method = models.CharField(max_length=100, blank=False)
    courses_characteristic = models.CharField(max_length=100, blank=True)
    courses_provide_lab = models.CharField(max_length=100, blank=False)
    courses_detail = models.CharField(max_length=10000, blank=False)
    courses_datetime = models.DateTimeField(auto_now_add=True)


class CoursesList(models.Model):
    courses_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='课程名')


class CoursesTeacher(models.Model):
    course = models.OneToOneField(CoursesList, related_name='teacher', blank=True, null=True, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=100, blank=False)


class StudentsDB(models.Model):
    # 名字，最大长度50，可以为空（注意：病没有min_length这个控制字段）
    name = models.CharField(max_length=50, blank=False, null=True, verbose_name='姓名')

    # 电话号码，校验以1开头的11位数字，最大长度为11，不可以为空，唯一键（注意，并没有min_length这个控制字段）
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="Phone number must be entered in the format: '13911153335'.11 digits allow.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=False, unique=True)

    # QQ号，校验5到20位的数字，最大长度位20，不可以为空，唯一键（注意：并没有min_length这个控制字段）
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ number must be entered in the format:'605658506'. 5-20 digits allowed.")
    qq_number = models.CharField(validators=[qq_regex], max_length=20, blank=False, unique=True)

    # 邮件，EmailField会校验邮件格式，最大长度50，可以为空（注意：并没有min_leng这个控制字段）
    mail = models.EmailField(max_length=50, blank=True)

    # 学习方向，后面的为选择内容，前面为写入数据库的值，注意max_length必须配置
    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = models.CharField(max_length=5, choices=direction_choices)

    # 班主任，后面的为选择内容，前面为写入数据库的值，注意max_length必须配置
    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = models.CharField(max_length=2, choices=class_adviser_choices)

    # 缴费情况，后面的为选择内容，前面的为写入数据库的值，注意max_l必须配置
    payed_choices = (('已缴费', '已缴费'), ('未交费', '未交费'))
    payed = models.CharField(max_length=3, choices=payed_choices)

    # 报名日期，自动添加日期项
    date = models.DateField(auto_now_add=True)
