from django import forms 
from .models import Department, Department2, Department3
from django.forms import ModelForm

class Dept1_EntryForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_1']
        widgets = {
            'dept_1': forms.Select(attrs={'class':'form-control'}),       
        }        
        
class Dept2_EntryForm(forms.ModelForm):
    class Meta:
        model = Department2
        fields = ['dept_2']
        widgets = {
            'dept_2': forms.Select(attrs={'class':'form-control'}),        
        }
        
class Dept3_EntryForm(forms.ModelForm):
    class Meta:
        model = Department3
        fields = ['dept_3']
        widgets = {
            'dept_3': forms.Select(attrs={'class':'form-control'}),
            
        }