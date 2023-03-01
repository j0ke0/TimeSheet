from .models import Department, Department2, Department3
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render, redirect
from .forms import Dept1_EntryForm, Dept2_EntryForm, Dept3_EntryForm
from django.contrib import messages


def home(request):
    return render(request, 'tim/home.html')
"""
def dept1(request):
   
    perm = 0
    for i in request.user.groups.all():
        if i.name == "department 1" : perm = 1
    if perm == 0:
        messages.success(request, "You don't have access to department 1")
        return redirect('tim:home')
    
    form = Dept1_EntryForm()
    if request.method == 'POST':
        form = Dept1_EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful data entry on department 1')
            return redirect('tim:dept1')
    context = {'form': form}
    return render(request, 'tim/dept1.html', context)

def dept2(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == "department 2" : perm = 1
    if perm == 0:
        messages.success(request, "You don't have access to department 2")
        return redirect('tim:home')
    form = Dept2_EntryForm()
    if request.method == 'POST':
        form = Dept2_EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful data entry on department 2')
            return redirect('tim:dept2')
    context = {'form': form}
    return render(request, 'tim/dept2.html', context)

def dept3(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == "department 3" : perm = 1
    if perm == 0:
        messages.success(request, "You don't have access to department 3")
        return redirect('tim:home')
    form = Dept3_EntryForm()
    if request.method == 'POST':
        form = Dept3_EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful data entry on department 3')
            return redirect('tim:dept3')
    context = {'form': form}
    return render(request, 'tim/dept3.html', context)"""


def dept_activate(request):
    """code for permissions on groups"""
    perm = 0
    for i in request.user.groups.all():
        if i.name == "department 1" : 
            perm = 1
            form = Dept1_EntryForm()
            if request.method == 'POST':
                form = Dept1_EntryForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successful data entry on department 1')
                    return redirect('tim:dept_activate')
            context = {'form': form}
            return render(request, 'tim/dept1.html', context)
        
        elif i.name == "department 2" : 
            perm = 1
            form = Dept2_EntryForm()
            if request.method == 'POST':
                form = Dept2_EntryForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successful data entry on department 2')
                    return redirect('tim:dept_activate')
            context = {'form': form}
            return render(request, 'tim/dept1.html', context)
        
        elif i.name == "department 3" : 
            perm = 1
            form = Dept3_EntryForm()
            if request.method == 'POST':
                form = Dept3_EntryForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successful data entry on department 3')
                    return redirect('tim:dept_activate')
            context = {'form': form}
            return render(request, 'tim/dept1.html', context)
            
    if perm == 0:
        messages.success(request, "You don't have access to department")
        return redirect('tim:home')
    
def out(request, pk):
    """code for permissions on groups"""
    perm = 0
    for i in request.user.groups.all():
        if i.name == "department 1" : 
            perm = 1
            fork = Department.objects.get(dept_1_id= pk)
            form = Dept1_EntryForm(instance=fork)
            if request.method == 'POST':
                form = Dept1_EntryForm(request.POST, instance=fork)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successful data entry on department 1')
                    return redirect('tim:dept_activate')
            context = {'form': form}
            return render(request, 'tim/dept2.html', context)
        
        elif i.name == "department 2" : 
            perm = 1
            fork = Department2.objects.get(dept_2_id= pk)
            form = Dept2_EntryForm(instance=fork)
            if request.method == 'POST':
                form = Dept2_EntryForm(request.POST, instance=fork)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successful data entry on department 2')
                    return redirect('tim:dept_activate')
            context = {'form': form}
            return render(request, 'tim/dept2.html', context)
        
        elif i.name == "department 3" : 
            perm = 1
            fork = Department3.objects.get(dept_3_id= pk)
            form = Dept3_EntryForm(instance=fork)
            if request.method == 'POST':
                form = Dept3_EntryForm(request.POST, instance=fork)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Successful data entry on department 3')
                    return redirect('tim:dept_activate')
            context = {'form': form, 'fork': fork}
            return render(request, 'tim/dept2.html', context)
            
    if perm == 0:
        messages.success(request, "You don't have access to department")
        return redirect('tim:home')