from django.shortcuts import render
from django.db import connection
from django.db.models import Q
from app.models import Student, Teacher

# Create your views here.
def student_list(request):
    posts=Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

##----- OR/Q/Filter/likes/startswith
def student_list_filter(request):
    # posts=Student.objects.filter(surname__startswith="yadav") | Student.objects.filter(surname__startswith='saini')
    '''to do queries with OR statement we use Q objects'''
    posts=Student.objects.filter(Q(surname__startswith='yadav') | Q(surname__startswith='saini'))
    # line 15 and 16 working in same way
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

##------------AND when all and condition true then get output
def student_list_and(request):
    posts=Student.objects.filter(classroom="1") & Student.objects.filter(age='20')
    # posts=Student.objects.filter(Q(surname__startswith='yadav') & Q(age='20'))
    # line 15 and 16 working in same way
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

##--------Union : use values_list with union, and 
## union remove dublicate items
def student_and_teacher_union(request):
    posts=Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))
    #values_lists give tuple outpu : ('ashish',)

    # posts=Student.objects.all().values("firstname").union(Teacher.objects.all().values("firstname"))
    #values give key value pain output :{'firstname': 'ashish'}
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})


##---------Exclude/a Not
def exclude_stu(request):
    # posts = Student.objects.exclude(age="20")

    # posts = Student.objects.exclude(age__gt=21) #output : ashish and sahil rest 1 (chetan) exclude
    #    #exclude show no. of obj excluded

    posts = Student.objects.filter(age__gt=21) #output : chetan rest 2 exclude
    # gt
    # gte
    # lt
    # lte
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

##---------Exclude/a Not
def exclude_stu2(request):
    posts = Student.objects.filter(~Q(age__gt=21)) #output : chetan rest 2 exclude
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})


##---------Select individual field
def individual_field(request):
    posts = Student.objects.filter(classroom='1').only('firstname','age')
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

##-------------- RUN Raw Query
def raw_qry(request):
    # posts = Student.objects.raw("SELECT * FROM app_student")
    posts = Student.objects.raw("SELECT * FROM app_student WHERE age=21")
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request,'output.html',{'posts':posts})

##---------Rwa Query2
def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0]for col in desc],row))
        for row in cursor.fetchall()
    ]
def raw2(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM app_student")
    r=dictfetchall(cursor)
    print(r)
    print(connection.queries
    )
    return render(request,'output.html',{'posts':r})