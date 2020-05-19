from django.db import models

# Create your models here.


# class Foo(models.Model):
#     name = models.CharField(max_length=1)


class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    #可加上默认值 code = models.CharField(max_length=32,null=True,default="SA")


    # fk = models.ForeignKey('Foo',on_delete=models.CASCADE)   #如果没有写字段的话，默认是跟自增的字段关联

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business",to_field='id',on_delete=models.CASCADE)



class Application(models.Model):
    name = models.CharField(max_length=32)

    r = models.ManyToManyField("Host")  #和下面的 HostToApp表发挥的作用一样
    #自动创建关系表
    # HostToApp表的生成内容一样
    #无法直接对第三张表进行操作



# class HostToApp(models.Model):
#     hobj = models.ForeignKey(to="Host",to_field="nid",on_delete=models.CASCADE)
#     aobj = models.ForeignKey(to="Application",to_field="id",on_delete=models.CASCADE)


#多对多创建表： 自定义创建关系表： HostToApp