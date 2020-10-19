from django.db import models


# Create your models here.
class news_data(models.Model):
    pass



class User_info(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_phone_num = models.CharField(max_length=50)
    user_major = models.CharField(max_length=50)

    user_id = models.CharField(max_length=50)
    user_pw = models.CharField(max_length=50)
    user_pw_check = models.CharField(max_length=50)




