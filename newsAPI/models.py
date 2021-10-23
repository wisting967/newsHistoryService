from django.db import models
from django.utils.translation import ugettext_lazy as _
from userProfile.models import UserProfile

'''
说明：
  1. 对于使用ForeignKey引用的外部模型，on_delete建议还是设置为models.CASCADE。因为如果不删除，则处理模型时，需要对引用的外部模型不存在的异常做处理
  2. 鉴于以上原因，对于模型的操作，不建议提供真实的物理删除，都采用软删除的模式，仅将数据置为无效，不显示即可
'''
# Create your models here.
# 热点无尾旧闻表
class News(models.Model):
  newsTitle = models.CharField(_('newsTitle'), max_length=128)
  newsThumbnail = models.URLField(_('newsThumbnail'), null=True)  # 没有标题图片时，统一使用业务Logo
  loadTime = models.DateTimeField(_('loadTime'), auto_now_add=True)  # 录入时间
  newsOutline = models.CharField(_('newsOutline'), max_length=1024)  # 用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表132*132正方形头像），用户没有头像时该项为空。若用户更换头像，原有头像URL将失效。
  newsNote = models.CharField(_('newsNote'), max_length=128, null=True)  # 用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
  newsLoader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # 不删数据，仅标记为destroy软删除
  lastModifyTime = models.DateTimeField(_('lastModifyTime'), auto_now=True)
  class Meta:
    db_table = 't_news'
    indexes = [
        models.Index(
            fields=['newsTitle'],
            name='newsTitle_idx',
        ),
        models.Index(
            fields=['newsLoader'],
            name='newsLoader_idx',
        ),
        models.Index(
            fields=['loadTime'],
            name='newsLoadTime_idx',
        ),
    ]

# 热点无尾旧闻表
class NewsHistory(models.Model):
  news = models.ForeignKey(News, on_delete=models.CASCADE)  # 不删数据，仅标记为destroy软删除
  historyOutline = models.CharField(_('historyOutline'), max_length=1024)
  historySpan = models.CharField(_('historySpan'), max_length=32)  # 用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表132*132正方形头像），用户没有头像时该项为空。若用户更换头像，原有头像URL将失效。
  historyLink = models.URLField(_('historyLink'))  # 必须有来源
  historyTime = models.DateTimeField(_('historyTime'), auto_now_add=True)  # 录入时间
  historyLoader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Team表不删数据，仅标记为destroy软删除
  lastModifyTime = models.DateTimeField(_('lastModifyTime'), auto_now=True)
  class Meta:
    db_table = 't_newshistory'
    indexes = [
        models.Index(
            fields=['historyTime'],
            name='historyTime_idx',
        ),
    ]