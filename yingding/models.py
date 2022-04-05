from django.db import models


class Admissions_data(models.Model):
    major_group_code = models.IntegerField("专业组代码",blank=True,null=True)
    major_group_name = models.CharField("专业组名称",max_length=200,default='')
    preferred_subject = models.CharField("首选科目",max_length=2,default='')
    recleaning_subject = models.CharField("再选科目",max_length=20,default='')
    annual_target = models.IntegerField("计划数",null=True)
    plan_change = models.IntegerField("计划增减",null=True)
    provinces = models.CharField("所在省份",max_length=10,default='')
    region = models.CharField("所在地区",max_length=10,default='')
    college_property = models.CharField("院校性质",max_length=4,default='')
    college_state = models.CharField("院校说明",max_length=20,blank=True,null=True)
    line_2019 = models.IntegerField("2019录取线",blank=True,null=True)
    line_2020 = models.IntegerField("2020录取线",blank=True,null=True)
    line_2021 = models.IntegerField("2021录取线",blank=True,null=True)
    ranking_2019 = models.IntegerField("2019位次",blank=True,null=True)
    ranking_2020 = models.IntegerField("2020位次",blank=True,null=True)
    ranking_2021 = models.IntegerField("2021位次",blank=True,null=True)


    def __str__(self):
        return self.major_group_name
