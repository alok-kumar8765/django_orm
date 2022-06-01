from django.shortcuts import render

# open shell
    #python manage.py shell
# import table
    #from student.models import Student
## Add Recode In Table
    # qr = Student.objects.create(
    # username = 'rahul20', first_name = 'Rahul', 
    # last_name = 'Shakya', mobile = '77777', 
    # email = 'rahul@gmail.com')
## Get all records
    # qr=Student.objects.all()
## Retrieving Single data
    # qr=Student.objects.get(pk=1)

# values_list and values
    # qr=Student.objects.filter(pk=1).values_list('first_name')     or
    # qr=Student.objects.filter(pk=1).values_list()  // the output of values_list is always a 
        # value from dictionary
    # qr=Student.objects.filter(pk=1).values()   // the output of values is in key value pair {'id': 1, 'username': 'rahul20'}
    # qr= Student.objects.all().values_list()
# Simple Filtering
    # qr = Student.objects.filter(first_name__startswith = 'R')
    # qr = Student.objects.filter(first_name__endswith = 'l')

# Exclude 
    # qr = Student.objects.exclude(first_name__startswith = 'R') /remove name start with r and show rest result

# Bulk create
    # Student.objects.bulk_create([Student(first_name = 'Jai', last_name = 'Shah', mobile = '88888', email = 'shah@reddif.com'),Student(first_name = 'Tarak', last_name = 'Mehta', mobile = '9999', email = 'tarak@reddif.com'), Student(first_name = 'SuryaKumar', last_name = 'Yadav', mobile = '00000', email = 'yadav@reddif.com')])

# OR 
    # from django.db.models import Q
    # qr = Student.objects.filter(Q(first_name__startswith = 'R') | Q(last_name__startswith = 'S'))                   

# Calculate/Count all objects
    # qr = Student.objects.all().count()

# Limiting Query Set
    # qr = Student.objects.all()[:2] 
    # qr = Student.objects.all()[1:6]

# Ordering Student accending and decending order
    # qr = Student.objects.all().order_by('mobile')
    # qr = Student.objects.all().order_by('mobile').values_list() //accending output
    # qr = Student.objects.all().order_by('-mobile')    // desc order

# check which student belongs to which teacher_id in accending order
    # qr = Student.objects.all().order_by('teacher_name', 'first_name')

# Exect & iexact use for getting exact/fixed obj in result
    # qr = Student.objects.get(first_name__exact = 'ram') // if ram not found through error

# contain and icontain work like startswith and endswith 
    # qr = Student.objects.filter(last_name__contains = 'Shar')

# truncate used in sql but in django we use delete()
    # Student.objects.all().delete()  

# gtrater than, less than, gte, lte
    # qr = Student.objects.filter(id__gte = 5)
    # qr = Student.objects.filter(id__lte = 2)
    # qr = Student.objects.filter(id__lt = 15)
    # qr = Student.objects.filter(id__gt = 9)

# union 
    # q1.union(q2)  //meaning common in both (q1 and q2) + objs from q1

# how to get student and his assigned teacher name
    # qr = Student.objects.select_related('teacher_name').get(id=6) 
    # qr    // output student name
    # qr.teacher_name   // output teacher name
            # or using raw query
    # qr = Student.objects.raw("SELECT *, teacher_name_id AS tn FROM student_student") 
    # for s in qr:                            
    #     print("%s is %s." %(s.first_name,s.tn))