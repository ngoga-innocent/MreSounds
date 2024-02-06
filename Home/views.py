from django.shortcuts import get_object_or_404, render,redirect,HttpResponse,HttpResponseRedirect
from Staff.models import Course,Chapter,Team
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home(request):
    courses=Course.objects.all().order_by('-created_at')[:12]
    team=Team.objects.all()
    return render(request,'Home.html',{'courses':courses,'team_mates':team})
def AllCourse(request):
    courses=Course.objects.all()
    context={'courses':courses}
    return render(request,'pages/Allcourses.html',context)

@login_required
def Singlecourse(request,id):
    if(request.user.is_authenticated):
        course=Course.objects.get(id=id)
        user=request.user
        is_paid_user=course.paid_user.filter(id=user.id).exists()
        # print(is_paid_user)
       
        if course and is_paid_user:
            chapters=Chapter.objects.filter(course=id)
            return render(request,'pages/chapters.html',{'chapters':chapters})
        elif not is_paid_user:
            return render(request,'pages/payment.html',{'course_id':id})
        else:
            return render(request,'pages/notfound.html',{'message':'requested course not found'})
    else:
        return redirect('login')
@login_required   
def PaymentFunction(request,id):
    if request.method=='POST':
        print(request.POST)
        course=Course.objects.get(id=id)
        adduser=course.paid_user.add(request.user)
        if adduser:
            url=f'/course/' + id
            return HttpResponseRedirect(url)
        else:
            return render(request,'pages/payment.html',{'course_id':id})
    