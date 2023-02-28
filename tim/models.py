from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    dept_1 = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    day_in = models.DateField(null=True, blank=True)
    time_in =models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Date: {self.day_in} Time: {self.time_in} - {self.dept_1.first_name.title()} {self.dept_1.last_name.title()}"
    
class Department2(models.Model):
    dept_2 = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    day_in = models.DateField(null=True, blank=True)
    time_in =models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Date: {self.day_in} Time: {self.time_in} - {self.dept_2.first_name.title()} {self.dept_2.last_name.title()}"

class Department3(models.Model):
    dept_3 = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    day_in = models.DateField(null=True, blank=True)
    time_in =models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Date: {self.day_in} Time: {self.time_in} - {self.dept_3.first_name.title()} {self.dept_3.last_name.title()}"
    

    
