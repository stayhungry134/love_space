import datetime
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class BaseModel(models.Model):
    visible = models.BooleanField(default=True, verbose_name='是否公开')

    class Meta:
        abstract = True


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='用户密码')
    profile_img = models.ImageField(upload_to='user_img', blank=True, verbose_name='用户头像')
    qq_id = models.CharField(blank=True, null=True, max_length=10, verbose_name='用户QQ号')
    phone = models.CharField(blank=True, null=True, max_length=16, verbose_name='用户手机号')
    wechat = models.CharField(blank=True, null=True, max_length=32, verbose_name='用户微信')
    birthday = models.DateField(blank=True, null=True, verbose_name='用户生日')
    location = models.CharField(blank=True, null=True, max_length=256, verbose_name='用户地址')
    remark = models.TextField(blank=True, null=True, verbose_name='用户简介')

    class Meta:
        db_table = 'user'


class ChatRecord(BaseModel):
    chat_time = models.DateTimeField(verbose_name='聊天时间')
    sender = models.CharField(max_length=10, verbose_name='聊天对象')
    replay = models.BooleanField(default=False, verbose_name='是否为回复')
    content = models.TextField(blank=True, null=True, verbose_name='聊天内容')
    chat_img = models.ImageField(upload_to='chat_image/%Y/%m', name='', verbose_name='聊天图片')

    class Meta:
        db_table = 'chat_record'
        ordering = ['-id']
        index_together = ['sender', 'chat_time']


class OurStory(BaseModel):
    story_time = models.DateTimeField(db_index=True, verbose_name='故事时间')
    story_img = models.ImageField(upload_to='story_image/%Y/%m', verbose_name='事件封面')
    content = MDTextField()

    class Meta:
        db_table = 'our_story'


class OurBlog(BaseModel):
    blog_time = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='blog 时间')
    blog_img = models.ImageField(upload_to='blog_image/%Y/%m', name='', verbose_name='blog 封面')
    content = MDTextField()

    class Meta:
        db_table = 'out_blog'
        ordering = ['-id']


class OurGallery(BaseModel):
    img_time = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='图片上传时间')
    img = models.ImageField(upload_to='gallery/%Y/%m', name='', verbose_name='图片')
    img_info = models.TextField(blank=True, null=True, verbose_name='图片简介')

    class Meta:
        db_table = 'our_gallery'
        ordering = ['-id']


class LeaveBlessing(BaseModel):
    blessing_time = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='留言时间')
    writer = models.CharField(max_length=32, verbose_name='留言者')
    qq_id = models.CharField(max_length=10, blank=True, null=True, verbose_name='留言者QQ号码')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='用户邮箱')

    class Meta:
        db_table = 'blessing'
        ordering = ['-id']
