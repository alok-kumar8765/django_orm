from django.shortcuts import render

# Create your views here.

# q- Find Employee with the highest salary
#ans -> from employee.models import Employee
#    -> Employee.objects.aggregate(max('esal'))  or 
#    -> Employee.objects.filter(esal=90000)   or
#    -> Employee.objects.order_by('esal') display lower to higher
#    -> Employee.objects.order_by('-esal')  higher to lower
#    -> Employee.objects.order_by('-esal')[0]  display highest value person

#first step from employee.models import Employee
#Calculate average salary of all employee

#update name Employee.objects.filter(ename="shayam").update(ename="rakesh")
#ans Employee.objects.aggregate(Avg('esal')) 

#find employee whose salary grater than 3000
#ans Employee.objects.filter(esal__gt=3000)  

#find all emp whose dont have salary 3000 or 3500
#ans Employee.objects.exclude(esal=3000) or
    # -> Employee.objects.filter(-Q(esal=3000))) 

