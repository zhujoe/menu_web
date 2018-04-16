from django.db import models

# Create your models here.


class cookbook(models.Model):
    name = models.CharField('名称', max_length=15)
    img_url = models.CharField('图片源', max_length=200)
    makings = models.CharField('材料', max_length=800)
    work = models.CharField('做法', max_length=2000)
    knack = models.CharField('诀窍', max_length=500)
    family = models.CharField('类别', max_length=100)
    pub_date = models.DateTimeField('时间')

    def __str__(self):
        return self.name
