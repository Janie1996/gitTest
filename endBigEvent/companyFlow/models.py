from django.db import models

# Create your models here.
from django.db import models


class CompanyFlow(models.Model):
    # 时间字段，使用DateField存储日期
    time_column = models.DateField(verbose_name='时间')
    # 流向字段，使用IntegerField并设置 choices 来限定值为0或1
    flow_direction = models.IntegerField(verbose_name='流向', choices=[(0, '流向0'), (1, '流向1')])
    # 专业公司字段，使用CharField存储字符串
    professional_company = models.CharField(max_length=255, verbose_name='专业公司')
    # 业务类型字段，使用CharField存储字符串
    business_type = models.CharField(max_length=100, verbose_name='业务类型')
    # 字节数字段，使用BigIntegerField存储较大整数
    byte_count = models.BigIntegerField(verbose_name='字节数')

    class Meta:
        # 设置模型对应的数据库表名，这里按照之前假设的表名示例
        db_table = 'companyflow'
        # 可以添加其他元数据，比如模型的复数名称等，以下是示例
        verbose_name_plural = '专业公司'

    def __str__(self):
        # 返回一个有代表性的字符串表示该模型实例，这里简单返回专业公司名称
        return self.professional_company