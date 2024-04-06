from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_city=models.CharField(max_length=50)


    class Meta:
        db_table = 'student'
        verbose_name_plural ="student"
    def __str__(self):
        return(self.stu_name)



    

