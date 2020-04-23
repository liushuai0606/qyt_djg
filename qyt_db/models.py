from django.db import models


class Courses(models.Model):
    courses_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='课程名')
    courses_summary = models.CharField(max_length=10000, blank=False)
    courses_teacher = models.CharField(max_length=100, blank=False)
    courses_method = models.CharField(max_length=100, blank=False)
    courses_characteristic = models.CharField(max_length=100, blank=True)
    courses_provide_lab = models.CharField(max_length=100, blank=False)
    courses_detail = models.CharField(max_length=10000, blank=False)
    courses_datetime = models.DateTimeField(auto_now_add=True)
