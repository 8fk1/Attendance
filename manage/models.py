from django.db import models

# Create your models here.
class User(models.Model):
    """ ユーザー
    """
    name = models.CharField("名前", max_length=50)
    email = models.EmailField("Email")

class Attendance(models.Model):
    """ 出退勤記録
    """
    datetime = models.DateTimeField("日時", auto_now=False, auto_now_add=True)
    # user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    user_name = models.CharField("名前", max_length=50)
    def to_dict(self):
        return {
            "id": self.id,
            # "day": f"{self.day:%Y-%m-%d}",
            "datetime": self.datetime,
            # "user": self.user,  
            "user_name": self.user_name,
        }
    class Meta:
        db_table = "attendance"
        verbose_name = "勤怠"
        ordering = ('-id',)
        #  ordering = ("-datetime",)