from django.shortcuts import render,redirect
from .models import Login , Student, Enquiry
from adminapp.models import Program, Branch, Year
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=="POST":
       userid=request.POST['userid']
       password=request.POST['password']
       utype=request.POST['utype']
       try:
        user=Login.objects.get(userid=userid,password=password)
        if(user and utype==user.utype and user.utype=="admin"):
           request.session['adminid']=userid
           return redirect('adminapp:dash')
        elif(user and utype==user.utype and user.utype=="student"):
           if(user.status=="u"):
              request.session['studentid']=userid
              return redirect('studentapp:dash')
           else:
              return redirect('mainapp:Studentlogin')
       except:
          return redirect('mainapp:Studentlogin')
    return render(request,'login.html')
    
def register(request):
    pr=Program.objects.all()
    br=Branch.objects.all()
    yr=Year.objects.all()
    if request.method=="POST":
       rollno=request.POST['rollno']
       name=request.POST['name']
       fname=request.POST['fname']
       mname=request.POST['mname']
       gender=request.POST['gender']
       address=request.POST['address']
       program=request.POST['program']
       branch=request.POST['branch']
       year=request.POST['year']
       number=request.POST['number']
       email=request.POST['email']
       stu=Student(roll_no=rollno,name=name,fname=fname,mname=mname,gender=gender,address=address,program=program,branch=branch,year=year,number=number,email=email)
       stu.save()
       log=Login(userid=email,password="1234",utype="student",status="b")
       log.save()
    return render(request,'register.html', locals());

def contactus(request):
   if request.method=="POST":
      name=request.POST['name']
      gender=request.POST['gender']
      address=request.POST['address']
      number=request.POST['number']
      email=request.POST['email']
      enquiry=request.POST['enquiry']
      contact=Enquiry(name=name,gender=gender,address=address,contactno=number,email=email,enquirytext=enquiry)
      contact.save()
   return render(request,'contactus.html')