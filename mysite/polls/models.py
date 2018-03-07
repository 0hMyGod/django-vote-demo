# -*- coding:utf-8 -*-
from django.db import models
import datetime
# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(u'内容', max_length=200)
    pub_date = models.DateTimeField(u'发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '是否最近发布'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 级联删除
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)# 表决结果

    def __str__(self):
        return self.choice_text