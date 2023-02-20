from django.shortcuts import render
from .form import OurStoryForm

# Create your views here.
# TODO 首页，展示相识时间，在一起时间（两个时间的计时效果）
# TODO Our Story 我们的故事，用时间线，故事内容，图片来展示（markdown）
# TODO Our Blog 我们的博客，主要用于记录一些东西
# TODO Gallery 用于上传我们的相册
# TODO wedding even 婚礼事件（结婚还早）显示日期和地点
# TODO RSVP 用于用户留言（关键字屏蔽）

# TODO 编辑内容，每个字段显示是否公开，如果不公开，那么只有登录才能显示


def index(request):
    if request.method == 'POST':
        print(request.FILES)
    else:
        form = OurStoryForm()
    return render(request, 'index.html', {'form': form})
