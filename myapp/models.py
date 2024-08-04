from django.db import models

# Create your models here.

# class Student(models.Model):
#     std_id = models.IntegerField(primary_key=True)
#     std_name = models.CharField(max_length = 255)
#     std_age = models.IntegerField()


class Book(models.Model):
    B_id = models.IntegerField(primary_key = True)
    B_name = models.CharField(max_length = 300)
    Subject = models.CharField(max_length = 300)
    Description = models.CharField(max_length = 300)
    Semester = models.IntegerField()
    Quantity = models.IntegerField()
    Price = models.IntegerField()



class Members(models.Model):
    M_id = models.IntegerField(primary_key = True)
    M_name = models.CharField(max_length = 300)
    Mobile_number = models.IntegerField()
    Semester = models.IntegerField()
    Branch = models.CharField(max_length = 300)




class Records(models.Model):
    R_id = models.IntegerField(primary_key =True)
    Member_id = models.ForeignKey(Members,on_delete=models.SET_NULL,null=True )
    Member_Name = models.CharField(max_length = 300)
    Book_id = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    Book_name = models.CharField(max_length = 300)
    B_issue_date = models.DateField()
    B_return_date = models.DateField()
    Status = models.CharField(max_length = 300)


