from django import forms 
from .models import Department, Department2, Department3
from django.forms import ModelForm

class Dept1_EntryForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_1', 'day_in', 'time_in']
        widgets = {
            'dept_1': forms.Select(attrs={'class':'form-control'}),
            'day_in': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD',}),
            'time_in': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'HH:MM:SS',}),
        }
        
class Dept2_EntryForm(forms.ModelForm):
    class Meta:
        model = Department2
        fields = ['dept_2', 'day_in', 'time_in']
        widgets = {
            'dept_2': forms.Select(attrs={'class':'form-control'}),
            'day_in': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD',}),
            'time_in': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'HH:MM:SS',}),
        }
        
class Dept3_EntryForm(forms.ModelForm):
    class Meta:
        model = Department3
        fields = ['dept_3', 'day_in', 'time_in']
        widgets = {
            'dept_3': forms.Select(attrs={'class':'form-control'}),
            'day_in': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD',}),
            'time_in': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'HH:MM:SS',}),
        }