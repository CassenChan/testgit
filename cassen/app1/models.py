from django.db import models

# Create your models here.
class Db(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    content = models.TextField()