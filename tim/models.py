from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    dept_1 = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    day_in = models.DateField(auto_now_add=True)
    time_in = models.TimeField(max_length=8, auto_now_add=True)
    logout = models.TimeField(max_length=8, auto_now=True)
    
    def __str__(self):
        return f"Date: {self.day_in} Time: {self.time_in} Logout: {self.logout} - {self.dept_1.first_name.title()} {self.dept_1.last_name.title()}"
    
class Department2(models.Model):
    dept_2 = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    day_in = models.DateField(auto_now_add=True)
    time_in = models.TimeField(max_length=8, auto_now_add=True)
    logout = models.TimeField(max_length=8, auto_now=True)
    
    def __str__(self):
        return f"Date: {self.day_in} Time: {self.time_in} Logout: {self.logout} - {self.dept_2.first_name.title()} {self.dept_2.last_name.title()}"

class Department3(models.Model):
    dept_3 = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    day_in = models.DateField(auto_now_add=True)
    time_in = models.TimeField(max_length=8, auto_now_add=True)
    logout = models.TimeField(max_length=8, auto_now=True)
    
    def __str__(self):
        return f"Date: {self.day_in} Login: {self.time_in} Logout: {self.logout} - {self.dept_3.first_name.title()} {self.dept_3.last_name.title()}"
    

    
