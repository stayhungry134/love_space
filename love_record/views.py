import markdown
import datetime
from django.shortcuts import render, get_object_or_404
from love_space.settings import BASE_DIR
from love_record.models import User, OurStory, OurGallery
from love_record.form import OurStoryForm


# Create your views here.
# TODO Our Story 我们的故事，用时间线，故事内容，图片来展示（markdown）
# TODO Our Blog 我们的博客，主要用于记录一些东西
# TODO Gallery 用于上传我们的相册
# TODO wedding even 婚礼事件（结婚还早）显示日期和地点
# TODO RSVP 用于用户留言（关键字屏蔽）

# TODO 编辑内容，每个字段显示是否公开，如果不公开，那么只有登录才能显示


def index(request):
    """主页"""
    # 定义遇见和在一起的时间
    met_list = [2022, 10, 27, 19, 26]  # JavaScript 上面月份是 0 - 11
    together_list = [2023, 1, 17, 20, 15]
    # 定义相遇时间
    met_time = datetime.datetime(2022, 11, 27, 19, 26)
    boyfriend = User.objects.filter(tag=User.BOYFRIEND).first()
    girlfriend = User.objects.filter(tag=User.GIRLFRIEND).first()
    met_year = met_time.strftime("%Y")
    met_month = met_time.strftime("%B")
    met_weekday = met_time.strftime("%A")
    met_day = met_time.strftime("%d")
    # 我们的相遇
    met_words = markdown.Markdown().convert(open(f'{BASE_DIR}/static/files/met_words.md').read())
    # 我们的故事
    stories = OurStory.objects.filter()[:4]
    # 我们的相册
    albums = OurGallery.objects.filter()[:8]
    return render(request, 'love_record/index.html', locals())


def our_story(request):
    """查看我们的故事"""
    stories = OurStory.objects.filter(visible=True)
    return render(request, 'love_record/story/our_story.html', locals())


def story_detail(request, story_id: int):
    """故事详情"""
    story = get_object_or_404(OurStory, id=story_id)
    story_content = markdown.Markdown().convert(story.content)
    return render(request, 'love_record/story/story_detail.html', locals())


def add_edit_story(request, story_id):
    """添加或编辑故事"""
    if request.method == 'POST':
        print('-------------------------')
        print(request.POST)
    story_form = OurStoryForm
    return render(request, 'love_record/story/story_form.html', locals())
