from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from mainapp.models import Student, Login
from adminapp.models import Material, News
from .models import Response ,Feedback, Question

# Create your views here.
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def index(request):
    try:
        if request.session['studentid']!=None:
            email=request.session['studentid']
            comp=Response.objects.filter(email=email,restype="complaint")
            stu=Student.objects.get(email=email)
            mat=Material.objects.filter(branch=stu.branch,year=stu.year,program=stu.program)
            
            cl=len(comp)
            ml=len(mat)
            
            return render(request,'studenthome.html',{'cl':cl,'ml':ml,'stu':stu})
    except:
        return redirect('mainapp:Studentlogin')    
 
def logout(request):
    try:
        del request.session['studentid']
    except KeyError:
        return redirect('mainapp:Studentlogin')
    return redirect('mainapp:Studentlogin')

@cache_control(nocache=True,must_revalidate=True,no_store=True)
def studymaterial(request):
    try:
        if request.session['studentid']!=None:
            email=request.session['studentid']
            stu=Student.objects.get(email=email)
            mat=Material.objects.filter(program=stu.program, branch=stu.branch, year=stu.year)
            return render(request,'ststudy.html',locals())
    except:
        return redirect('mainapp:Studentlogin')  
       
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def givefeedback(request):
   try: 
    if request.session['studentid']!=None:
     
     feedback=Feedback.objects.all()
     if request.method=="POST":
        fdesc=request.POST['feedback']
        obj=Feedback.objects.create()
        obj.fdesc=fdesc
        obj.save()
        return redirect('studentapp:feedback') 
     return render(request, 'givefeedback.html',locals())
   except:
       return redirect('mainapp:Studentlogin')
      



@cache_control(nocache=True,must_revalidate=True,no_store=True)
def complaint(request):
    try:
        if request.session['studentid']!=None:
           email=request.session['studentid']
           comp=Response.objects.filter(email=email,restype="complaint")
           if request.method=="POST":
               
               stu=Student.objects.get(email=email)
               subject=request.POST['subject']
               responsetext=request.POST['complaint']
               res=Response.objects.create()
               res.roll_no=stu.roll_no
               res.name=stu.name
               res.program=stu.program
               res.branch=stu.branch
               res.year=stu.year
               res.number=stu.number
               res.email=stu.email
               res.restype="complaint"
               res.subject=subject
               res.responsetext=responsetext
               res.save()
               return redirect('studentapp:complaint')
           return render(request,'complaint.html', locals())
    except:
         return redirect('mainapp:Studentlogin')   
    
def delcomplaint(request,id):
    comp=Response.objects.filter(id=id)
    comp.delete()
    return redirect('studentapp:complaint')    

def viewnews(request):
    news=News.objects.all()

    return render(request, 'viewnews.html',locals())

def changepassword(request):
    studentid=request.session.get('studentid')
    if request.method=='POST':
       log=Login.objects.get(userid=studentid)
       cpass=request.POST['cpass']
       npass=request.POST['npass']
       cnpass=request.POST['cnpass']
       if(log.password==cpass):
           if(npass==cnpass):
               if(npass!=cpass):
                   log.password=npass
                   log.save()

    return render(request,'changepassword.html')

def editprofile(request):
    email=request.session.get('studentid')
    pro=Student.objects.get(email=email)
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        address=request.POST['address']
        Student.objects.filter(email=email).update(name=name,number=number,address=address)
        return redirect('studentapp:dash')
    
   
    return render(request,'editprofile.html',locals())
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def addquestions(request):
    try:
        if request.session['studentid']!=None:
          email=request.session['studentid']
          q=Question.objects.all()
          if request.method=='POST':
             que=request.POST['que']
             desc=request.POST['desc']
             qu=Question.objects.create()
             
             qu.que=que
             qu.desc=desc
             qu.created_by=email
             qu.save()
             return redirect('studentapp:addquestions')
          return render(request,'addquestions.html',locals())
    except:
        return redirect('mainapp:Studentlogin')    
    
def delques(request,id):
    ques=Question.objects.filter(qid=id)
    ques.delete()
    return redirect('studentapp:addquestions')
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def disforum(request):
    try:
      if request.session['studentid']!=None:
       que=Question.objects.all()
       return render(request, 'disforum.html',locals())
      
    except:
        return redirect('mainapp:Studentlogin')  
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def uploadanswer(request,id):
    try: 
       if request.session['studentid']!=None:
        que=Question.objects.get(qid=id)
        return render(request,'uploadanswer.html',locals())  
    except:
        return redirect('mainapp:Studentlogin')            