from django.shortcuts import render,redirect
from .models import News, Program, Branch , Year , Material
from mainapp.models import Student, Login , Enquiry
from studentapp.models import Feedback, Response
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def addash(request):
    try:
        if request.session['adminid']!=None:
            news=News.objects.all()
            program=Program.objects.all()
            branch=Branch.objects.all()
            year=Year.objects.all()
            mat=Material.objects.all()
            st=Student.objects.all()
            feed=Feedback.objects.all()
            comp=Response.objects.filter(restype="complaint")
            nl=len(news)
            pl=len(program)
            bl=len(branch)
            yl=len(year)
            ml=len(mat)
            sl=len(st)
            fl=len(feed)
            cl=len(comp)
            return render(request,'adminhome.html',locals())
    except:
        return redirect('mainapp:Studentlogin')    
    
   
def news(request):
    news=News.objects.all()
    if(request.method=="POST"):
        title=request.POST['title']
        desc=request.POST['desc']
        obj=News.objects.create()
        obj.ntitle=title
        obj.ndesc=desc
        obj.status="u"
        obj.save()
        return redirect('adminapp:news')
    return render(request,'news.html',locals())

def delnews(request,id):
    news=News.objects.filter(nid=id)
    news.delete()
    return redirect('adminapp:news')

def editnews(request,id):
    news=News.objects.get(nid=id)
    if(request.method=="POST"):
        ntitle=request.POST['title']
        ndesc=request.POST['desc']
        News.objects.filter(nid=id).update(ntitle=ntitle,ndesc=ndesc)
        return redirect('adminapp:news')
    return render(request,'editnews.html',locals())

def program(request):
    program=Program.objects.all()
    if(request.method=="POST"):
        pname=request.POST['pname']
        obj=Program.objects.create()
        obj.pname=pname
        obj.status="u"
        obj.save()
        return redirect('adminapp:program')
    return render(request,'program.html',locals())

def delprogram(request,id):
    program=Program.objects.filter(pid=id)
    program.delete()
    return redirect('adminapp:program')

def editprogram(request,id):
    program=Program.objects.get(pid=id)
    if(request.method=="POST"):
     pname=request.POST['pname']
     Program.objects.filter(pid=id).update(pname=pname)
     return redirect('adminapp:program')
    return render(request,'editprogram.html',locals())

def branch(request):
    branch=Branch.objects.all()
    if(request.method=="POST"):
        bname=request.POST['bname']
        obj=Branch.objects.create()
        obj.bname=bname
        obj.status="u"
        obj.save()
        return redirect('adminapp:branch')
        
    return render(request,'branch.html',locals())

def delbranch(request,id):
    branch=Branch.objects.filter(bid=id)
    branch.delete()
    return redirect('adminapp:branch')
def editbranch(request,id):
    branch=Branch.objects.get(bid=id)
    if(request.method=='POST'):
        bname=request.POST['bname']
        Branch.objects.filter(bid=id).update(bname=bname)
        return redirect('adminapp:branch')
    return render(request,'editbranch.html',locals())

def year(request):
    year=Year.objects.all()
    if(request.method=="POST"):
     yname=request.POST['yname']
     obj=Year.objects.create()
     obj.yname=yname
     obj.status="u"
     obj.save()
     return redirect('adminapp:year')
    return render(request,'year.html',locals())

def delyear(request,id):
    year=Year.objects.filter(yid=id)
    year.delete()
    return redirect('adminapp:year')

def edityear(request,id):
    year=Year.objects.get(yid=id)
    if(request.method=="POST"):
        yname=request.POST['yname']
        Year.objects.filter(yid=id).update(yname=yname)
        return redirect('adminapp:year')
    return render(request,'edityear.html',locals())

def logout(request):
     try:
        del request.session['adminid']
     except KeyError:
        return redirect("mainapp:Studentlogin")
     return redirect("mainapp:Studentlogin")

def viewstudent(request):
    stu=Student.objects.all()
    return render(request,'viewstudent.html',locals())

@cache_control(nocache=True,must_revalidate=True,no_store=True)
def studymaterial(request):
    pr=Program.objects.all()
    br=Branch.objects.all()
    yr=Year.objects.all()
    material=Material.objects.all()
    if request.method=="POST":
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        subject=request.POST['subject']
        file_name=request.POST['file_name']
        my_file=request.FILES['my_file']
        status="u"
        mat=Material(program=program,branch=branch,year=year,subject=subject,file_name=file_name,my_file=my_file,status=status)
        mat.save()
        return redirect('adminapp:studymaterial')
    return render(request,'adstudy.html',locals())

def delstudy(request,id):
    mat=Material.objects.filter(id=id)
    mat.delete()
    return redirect('adminapp:studymaterial')
def editstudent(request,email):
    stu=Student.objects.get(email=email)
    log=Login.objects.get(userid=email)
    if request.method=="POST":
        
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        mobile=request.POST['number']
        gender=request.POST['gender']
        emailaddress=request.POST['email']
        address=request.POST['address']
        status=request.POST['status']
        stu.name=name
        stu.email=emailaddress
        stu.fname=fname
        stu.mname=mname
        stu.number=mobile
        stu.gender=gender
        stu.adress=address
        log.status=status
        stu.save()
        log.save()
        return redirect('adminapp:viewstudent')
    return render(request,'editstudent.html',{'stu':stu, 'status':log.status})

def delstudent(request,email):
    stu=Student.objects.filter(email=email)
    stu.delete()
    return redirect('adminapp:viewstudent')

def viewfeedback(request):
    feed=Feedback.objects.all()
    return render(request,'viewfeedback.html', locals())

def delfeedback(request,id):
    feedback=Feedback.objects.get(fid=id)
    feedback.delete()
    return redirect('adminapp:viewfeedback')
@cache_control(nocache=True,must_revalidate=True,no_store=True)
def viewcomplaint(request):
  try: 
   if request.session['adminid']!=None: 
    comp=Response.objects.all()
    return render(request,'viewcomplaint.html',locals())
  except:
      return redirect('mainapp:Studentlogin') 

def viewenquiry(request):
    enq=Enquiry.objects.all()
    return render(request, 'viewenquiry.html',locals())  
def delenquiry(request,id):
    enq=Enquiry.objects.filter(id=id)
    enq.delete()
    return redirect('adminapp:viewenquiry')