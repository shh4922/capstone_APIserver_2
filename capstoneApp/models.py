from django.db import models


class userinfo(models.Model):
    username = models.CharField(max_length=30, null=False)
    userid = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)


    class Meta:
        #정렬
        #ordering = ('userid',)
        db_table = 'userinfo'

    def __str__(self):
        return self.userid
