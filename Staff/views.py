from django.shortcuts import get_object_or_404, render,redirect
from .models import Course,Chapter,Skills
from .forms import AddSKills,AddChapterForm
from django.http import HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
def Home(request):
    return render(request,'Staff/Home.html')
# Create your views here.
def AddCourse(request):
    
    if request.method=='POST':
        name=request.POST['course_name']
        thumbnail=request.FILES['course_thumbnail']
        new_course=Course(name=name,thumbnail=thumbnail,author=request.user)
        new_course.save()
        courses=Course.objects.all()
        context={'courses':courses}
        return render(request,'Staff/addCourse.html',context)
    else:
        courses=Course.objects.all()
        context={'courses':courses}
        return render(request,'Staff/addCourse.html',context)
def ViewChapter(request,id):
    chapters=Chapter.objects.filter(course=id)
    form=AddSKills
    return render(request,'Staff/addSkills.html',{'form':form,'addchapter':AddChapterForm,'chapters':chapters,'course_id':id})  
def AddSkill(request,course_id,chapter_id):
    submitted=False
    
    if request.method=='POST':
        #add_chapter_form=AddChapterForm(request.POST)
        form=AddSKills(request.POST)
        if form.is_valid():
            chapter=get_object_or_404(Chapter,id=chapter_id)
            form.instance.chapter=chapter
            form.save()
            url =f'/staff/addcourse/{course_id}'
            return HttpResponseRedirect(url)
        # elif 'add_chapter_form_submit' in request.POST and add_chapter_form.is_valid():
        #     add_chapter_form.instance.course=id
        #     add_chapter_form.save()
        #     url=f'/staff/addcourse/{id}'
        #     return HttpResponseRedirect(url)
        else:
            url =f'/staff/addcourse/{course_id}'
            return HttpResponseRedirect(url)
        
        
        
    else:
        chapters=Chapter.objects.filter(course=course_id)
        form=AddSKills
        return render(request,'Staff/addSkills.html',{'form':form,'addchapter':AddChapterForm,'subitted':submitted,'chapters':chapters,'course_id':id})   
def AddChapter(request,id):
    if request.method=='POST':
        form=AddChapterForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST,request.FILES)
            course=get_object_or_404(Course,id=id)
            form.instance.course=course
            form.save()
            chapters=Chapter.objects.filter(course=id)
            url=f'/staff/addcourse/{id}'
            return HttpResponseRedirect(url)
        else:
            # print(request.POST)
            chapters=Chapter.objects.filter(course=id)
            return render(request,'staff/addskills.html',{'chapters':chapters,'course_id':id,'message':'error in submission'})
    else:
        chapters=Chapter.objects.filter(course=id)
        return render(request,'staff/addskills.html',{'chapters':chapters,'course_id':id})
def GetSkills(request, id):
    try:
        skills = Skills.objects .filter(chapter=id).values()
        # print(skills)
        skills_list=list(skills)
        return JsonResponse({'skills': skills_list})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def SingleSkill(request, id):
    skill = get_object_or_404(Skills, id=id)

    if request.method == 'POST' and  request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        pressed_button = request.POST.get('button')
        if pressed_button == 'next':
            next_skill = Skills.objects.filter(chapter=skill.chapter, id__gt=id).order_by('id').first()
            if next_skill:
                id = next_skill.id
                skill = next_skill
                return JsonResponse({'id': id})
            else:
                return JsonResponse({'message': 'Can not find other id'})
        else:
            previous_skill = Skills.objects.filter(chapter=skill.chapter, id__lt=id).order_by('-id').first()
            if previous_skill:
                id = previous_skill.id
                skill = previous_skill
                return JsonResponse({'id': id})
            else:
                return JsonResponse({'message': 'Can not find previous skill'})

    # Handle non-AJAX requests here
    context = {'skill': skill}
    return render(request, 'pages/singleskill.html', context)