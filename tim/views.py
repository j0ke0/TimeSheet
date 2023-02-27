from .models import Department, Department2, Department3
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import Dept1_EntryForm
from django.contrib import messages


def home(request):
    return render(request, 'tim/home.html')

def dept1(request):
    form = Dept1_EntryForm()
    if request.method == 'POST':
        form = Dept1_EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Succcessful login')
            return redirect('tim:home')
    context = {'form': form}
    return render(request, 'tim/home.html', context)