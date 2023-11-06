from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(verbose_name="カテゴリー",max_length=20)
def  str (self):
    return self.title

class photoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(Category,verbose_name='カテゴリ',on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=200)
    comment = models.TextField(verbose_name='コメント',)
    image1 = models.ImageField(verbose_name='イメージ１',upload_to= 'photos')
    image2 = models.ImageField(verbose_name='イメージ２',upload_to='photos',blank=True,null=True)
    posted_at = models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)
    def str (self):
        return self.title

