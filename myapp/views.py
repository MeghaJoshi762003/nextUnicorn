from socket import fromshare
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User, auth
from myapp.models import log,feedback,nuser,Image,startup, suggestion,entrepreneur,Comment
from django.contrib import messages
from django import forms
from .forms import nuserForm
def register(request):
    if request.method == "POST":
        username = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']
        userid = email[0:email.index('@')]
        post = request.POST['as'] 
        user = log(username = username , post = post , password = password , email = email, userid = userid )
        user.save()
        request.session['userid']=userid
        if post=="User":
            pro=nuser(userid=userid)
        if post=="Startup":
            pro=startup(startupid=userid)
        if post=="Entrepreneur":
            pro=entrepreneur(entrepreneurid=userid)
        pro.save()
        return redirect('home')
    return render(request,'login.html')

def login(request):
    if request.method== "POST":
        email= request.POST['email']
        password=request.POST['password']
        request.session['userid']=email[0:email.index('@')]
        nuser=log.objects.filter(email=email,password=password)
        if not nuser:
            return redirect('login')
        return redirect('home')
    return redirect('register')

def home(request):
    user=log.objects.get(userid=request.session['userid'])
    alluser=log.objects.all()
    posts=Image.objects.all()
    comment=Comment.objects.all()
    return render(request,'home.html',{'user':user,'post':posts,'log':alluser,'comment':comment})

def viewprofile(request):
   
    if(log.objects.get(userid=request.session['userid']).post=='User'):
        return redirect('user')
    elif(log.objects.get(userid=request.session['userid']).post=='Entrepreneur'):
        return redirect('entrepreneurprofile')
    else: 
        return redirect('startupprofile')

def user(request):
    # profile=user.objects.filter(userid=request.session['userid']).profilepic
    arg={
    'pic':nuser.objects.get(userid=request.session['userid']).profilepic,
    'name':log.objects.get(userid=request.session['userid']).username,
    'userid':request.session['userid'],
    'user':log.objects.get(userid=request.session['userid']),
    'bio':nuser.objects.get(userid=request.session['userid']).bio,
    'skills':nuser.objects.get(userid=request.session['userid']).skills,
    'facebook':nuser.objects.get(userid=request.session['userid']).facebook,
    'instagram':nuser.objects.get(userid=request.session['userid']).instagram,
    'twitter':nuser.objects.get(userid=request.session['userid']).twitter,
    'linkedin':nuser.objects.get(userid=request.session['userid']).linkedin}
    return render(request,'user.html',arg)

def usersettings(request):
    if request.method=='POST':
        userid=request.session['userid']
        user=nuser.objects.get(userid=userid)
        log1=log.objects.get(userid=userid)
        if request.POST['fullName']:
            log1.username=request.POST['fullName']
        if request.POST['pass']:
            log1.password=request.POST['pass']
        if request.POST['bio']:
            user.bio=request.POST['bio']
        if request.POST['skills']:
            user.skills=request.POST['skills']
        if request.POST['facebook']:
            user.facebook=request.POST['facebook']
        if request.POST['instagram']:
            user.instagram=request.POST['instagram']
        if request.POST['twitter']:
            user.twitter=request.POST['twitter']
        if request.POST['linkedin']:
            user.linkedin=request.POST['linkedin']
        log1.save()
        user.save()
        return redirect('home')
    userid=request.session['userid']
    arg={
            'log1':nuser.objects.get(userid=userid)
        }
    return render(request,'usersettings.html',arg)

def userprofile(request):
    if request.method == "POST":
        userid=request.session['userid']
        user=nuser.objects.get(userid=userid)
        user.profilepic = request.FILES['uprofile']
        user.save()
        messages.success(request,"Post Successfully")
    return redirect( 'user' )

def startupsettings(request):
    if request.method=='POST':
        userid=request.session['userid']
        suser=startup.objects.get(startupid=userid)
        log2=log.objects.get(userid=userid)
        if request.POST['username']:
            log2.username=request.POST['username']
        if request.POST['password']:
            log2.password=request.POST['password']
        if request.POST['startuplink']:
            suser.startuplink=request.POST['startuplink']
        if request.POST['about']:
            suser.about=request.POST['about']
        if request.POST['facebook']:
            suser.facebook=request.POST['facebook']
        if request.POST['instagram']:
            suser.instagram=request.POST['instagram']
        if request.POST['twitter']:
            suser.twitter=request.POST['twitter']
        if request.POST['linkedin']:
            suser.linkedin=request.POST['linkedin']
        log2.save()
        suser.save()
        return redirect('home')
    userid=request.session['userid']
    arg={
            'log2':startup.objects.get(startupid=userid)
        }
    return render(request,'startupsettings.html',arg)

def editprofile(request):
    form=nuserForm()
    if request.method=="POST":
        form=nuserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {'form':form,
    'user':user}
    return render(request,'usersettings.html',context)

def startupprofile(request):
    post=Image.objects.all()
    userid=request.session['userid']
    i=0
    for p in post:
        if p.userid == userid:
            i=i+1
    arg={
    'box':suggestion.objects.all(),
    'about':startup.objects.get(startupid=request.session['userid']).about,
    'name':log.objects.get(userid=request.session['userid']).username,
    'email':log.objects.get(userid=request.session['userid']).email,
    'userid':request.session['userid'],
    'phoneno':startup.objects.get(startupid=request.session['userid']).phoneno,
    'pitchvideo':startup.objects.get(startupid=request.session['userid']).pitch,
    'startuplink':startup.objects.get(startupid=request.session['userid']).startuplink,
    'facebook':startup.objects.get(startupid=request.session['userid']).facebook,
    'instagram':startup.objects.get(startupid=request.session['userid']).instagram,
    'twitter':startup.objects.get(startupid=request.session['userid']).twitter,
    'linkedin':startup.objects.get(startupid=request.session['userid']).linkedin,
    'user':log.objects.get(userid=request.session['userid']),
    'cover':startup.objects.get(startupid=request.session['userid']).coverphoto,
    'pic':startup.objects.get(startupid=request.session['userid']).profilepic,
    'post':Image.objects.all(),
    'num':i,
    'form':startup.objects.get(startupid=request.session['userid']).form
     }
    return render(request, 'startup.html',arg)

def main(request):
    return render(request,'login.html')
    
def about(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        opinion=request.POST['opinion']
        text=feedback(name=name,email=email,opinion=opinion)
        text.save()
    user=log.objects.get(userid=request.session['userid'])
    return render(request,'about.html',{'user':user})

         # Instance Variable
        

def PostImage(request):
    if request.method == "POST":
        userid=request.session['userid']
        caption = request.POST.get('description')
        photo = request.FILES['image']
        prod = Image(caption = caption,photo = photo,userid=userid)
        prod.save()
        return redirect('home' )
    
    return redirect( 'home' )

def articles(request):
    user=log.objects.get(userid=request.session['userid'])
    return render(request,'articles.html',{'user':user})

def schemes(request):
    user=log.objects.get(userid=request.session['userid'])
    return render(request,'scheme.html',{'user':user})

def search(request):
    if request.method=="POST":
        ouserid=request.POST['search']
        t=log.objects.all()
        for i in t:
            if i.userid == ouserid:
               request.session['ouserid']=ouserid
               return redirect('otherprofile') 
        return HttpResponse('user not found')
        

def otherprofile(request):
    if(log.objects.get(userid=request.session['ouserid']).post=='User'):
        return redirect('ouser')
    elif(log.objects.get(userid=request.session['ouserid']).post=='Entrepreneur'):
        return redirect('oentrepreneurprofile')
    else: 
        return redirect('ostartupprofile')

def ouser(request):
    # profile=user.objects.filter(userid=request.session['userid']).profilepic
    user=log.objects.get(userid=request.session['ouserid'])
    arg={
    'profile':nuser.objects.get(userid=request.session['ouserid']),
    'name':log.objects.get(userid=request.session['ouserid']).username,
    'userid':request.session['ouserid'],
    'bio':nuser.objects.get(userid=request.session['ouserid']).bio,
    'skills':nuser.objects.get(userid=request.session['ouserid']).skills,
    'facebook':nuser.objects.get(userid=request.session['ouserid']).facebook,
    'instagram':nuser.objects.get(userid=request.session['ouserid']).instagram,
    'twitter':nuser.objects.get(userid=request.session['ouserid']).twitter,
    'linkedin':nuser.objects.get(userid=request.session['ouserid']).linkedin,
    'user':user}
   
    return render(request,'user.html',arg)

def suggestionbox(request):
    if request.method=="POST":
        by=request.session['userid']
        to=request.POST['to']
        opinion=request.POST['content']
        new=suggestion(by=by,to=to,opinion=opinion)
        new.save()
        return redirect('suggestionbox')
    suggestions=suggestion.objects.all()
    userid=request.session['userid']
    user=log.objects.get(userid=request.session['userid'])
    return render(request,'suggestion.html',{'suggestions':suggestions,'userid':userid,'user':user})

def startupsettings(request):
    if request.method=='POST':
        userid=request.session['userid']
        suser=startup.objects.get(startupid=userid)
        
        log2=log.objects.get(userid=userid)
        if request.POST['username']: 
            log2.username=request.POST['username']
        if request.POST['password']:
            log2.password=request.POST['password']
        if request.POST['phoneno']:
            suser.phoneno=request.POST['phoneno']
        if request.POST['startuplink']:
            suser.startuplink=request.POST['startuplink']
        if request.POST['about']:
            suser.about=request.POST['about']
        if request.POST['facebook']:
            suser.facebook=request.POST['facebook']
        if request.POST['instagram']:
            suser.instagram=request.POST['instagram']
        if request.POST['twitter']: 
            suser.twitter=request.POST['twitter']
        if request.POST['linkedin']:
            suser.linkedin=request.POST['linkedin']
        log2.save()
        suser.save()
        return redirect('home')
    userid=request.session['userid']
    arg={
            'log2':startup.objects.get(startupid=userid)
        }
    return render(request,'startupsettings.html',arg)

def startuplogo(request):
    if request.method == "POST":
        userid=request.session['userid']
        user=startup.objects.get(startupid=userid)
        user.profilepic = request.FILES['logo']
        user.save()
        messages.success(request,"Post Successfully")
    return redirect( 'startupprofile' )

def startupcp(request):
    if request.method == "POST":
        userid=request.session['userid']
        user=startup.objects.get(startupid=userid)
        user.coverphoto = request.FILES['cp']
        user.save()
    return redirect( 'startupprofile' )

def pitch(request):
    if request.method == "POST":
        userid=request.session['userid']
        user=startup.objects.get(startupid=userid)
        user.pitch = request.FILES['video']
        user.save()
    return redirect( 'startupprofile' )

def entrepreneurprofile(request):
    post=Image.objects.all()
    userid=request.session['userid']
    i=0
    for p in post:
        if p.userid == userid:
            i=i+1
    arg={
    'box':suggestion.objects.all(),
    'about':entrepreneur.objects.get(entrepreneurid=request.session['userid']).about,
    'name':log.objects.get(userid=request.session['userid']).username,
    'userid':request.session['userid'],
    'email':log.objects.get(userid=request.session['userid']).email,
    'phoneno':entrepreneur.objects.get(entrepreneurid=request.session['userid']).phoneno,
    'startup':entrepreneur.objects.get(entrepreneurid=request.session['userid']).startup,
    'facebook':entrepreneur.objects.get(entrepreneurid=request.session['userid']).facebook,
    'instagram':entrepreneur.objects.get(entrepreneurid=request.session['userid']).instagram,
    'twitter':entrepreneur.objects.get(entrepreneurid=request.session['userid']).twitter,
    'linkedin':entrepreneur.objects.get(entrepreneurid=request.session['userid']).linkedin,
    'user':log.objects.get(userid=request.session['userid']),
    'ecover':entrepreneur.objects.get(entrepreneurid=request.session['userid']).coverphoto,
    'epic':entrepreneur.objects.get(entrepreneurid=request.session['userid']).profilepic,
    'post':Image.objects.all(),
    'num':i,
    'form':entrepreneur.objects.get(entrepreneurid=request.session['userid']).form
    }
    return render(request, 'entrepreneur.html',arg)

def entrepreneursettings(request):
    if request.method=='POST':
        userid=request.session['userid']
        suser=entrepreneur.objects.get(entrepreneurid=userid)
        log3=log.objects.get(userid=userid)
        if request.POST['username']:
            log3.username=request.POST['username']
        if request.POST['password']:
            log3.password=request.POST['password']
        if request.POST['phoneno']:
            suser.phoneno=request.POST['phoneno']
        if request.POST['startup']:
            suser.startup=request.POST['startup']
        if request.POST['about']:
            suser.about=request.POST['about']
        if request.POST['facebook']:
            suser.facebook=request.POST['facebook']
        if request.POST['instagram']:
            suser.instagram=request.POST['instagram']
        if request.POST['twitter']:
            suser.twitter=request.POST['twitter']
        if request.POST['linkedin']:
            suser.linkedin=request.POST['linkedin']
        log3.save()
        suser.save()
        return redirect('home')
    userid=request.session['userid']
    
    arg={
            'log3':entrepreneur.objects.get(entrepreneurid=userid)
        }
    return render(request,'entrepreneursettings.html',arg)

def entrepreneurdp(request):
    if request.method == "POST":
        userid=request.session['userid']
        user=entrepreneur.objects.get(entrepreneurid=userid)
        user.profilepic = request.FILES['dp']
        user.save()
        messages.success(request,"Post Successfully")
    
    return redirect( 'entrepreneurprofile' )

def entrepreneurcp(request):
    if request.method == "POST":
        userid=request.session['userid']
        user=entrepreneur.objects.get(entrepreneurid=userid)
        user.coverphoto = request.FILES['ecp']
        user.save()
        messages.success(request,"Post Successfully")
    return redirect( 'entrepreneurprofile' )

def ostartupprofile(request):
    post=Image.objects.all()
    userid=request.session['ouserid']
    i=0
    for p in post:
        if p.userid == userid:
            i=i+1
    arg={
    'box':suggestion.objects.all(),
    'about':startup.objects.get(startupid=request.session['ouserid']).about,
    'name':log.objects.get(userid=request.session['ouserid']).username,
    'email':log.objects.get(userid=request.session['ouserid']).email,
    'userid':request.session['ouserid'],
    'phoneno':startup.objects.get(startupid=request.session['ouserid']).phoneno,
    'pitchvideo':startup.objects.get(startupid=request.session['ouserid']).pitch,
    'startuplink':startup.objects.get(startupid=request.session['ouserid']).startuplink,
    'facebook':startup.objects.get(startupid=request.session['ouserid']).facebook,
    'instagram':startup.objects.get(startupid=request.session['ouserid']).instagram,
    'twitter':startup.objects.get(startupid=request.session['ouserid']).twitter,
    'linkedin':startup.objects.get(startupid=request.session['ouserid']).linkedin,
    'user':log.objects.get(userid=request.session['ouserid']),
    'cover':startup.objects.get(startupid=request.session['ouserid']).coverphoto,
    'pic':startup.objects.get(startupid=request.session['ouserid']).profilepic,
    'form':startup.objects.get(startupid=request.session['ouserid']).form,
    'post':Image.objects.all(),
    'num':i
     }
    return render(request, 'startup.html',arg)

def oentrepreneurprofile(request):
    post=Image.objects.all()
    userid=request.session['ouserid']
    i=0
    for p in post:
        if p.userid == userid:
            i=i+1
    arg={
    'box':suggestion.objects.all(),
    'about':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).about,
    'name':log.objects.get(userid=request.session['ouserid']).username,
    'userid':request.session['ouserid'],
    'email':log.objects.get(userid=request.session['ouserid']).email,
    'phoneno':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).phoneno,
    'startup':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).startup,
    'facebook':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).facebook,
    'instagram':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).instagram,
    'twitter':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).twitter,
    'linkedin':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).linkedin,
    'user':log.objects.get(userid=request.session['ouserid']),
    'ecover':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).coverphoto,
    'epic':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).profilepic,
    'form':entrepreneur.objects.get(entrepreneurid=request.session['ouserid']).form,
    'post':Image.objects.all(),
    'num':i
    }
    return render(request, 'entrepreneur.html',arg)

def form(request):
    if request.method == "POST":
        user=log.objects.get(userid=request.session['userid'])
        if user.post == "Startup":
            user=startup.objects.get(startupid=request.session['userid'])
            user.form=request.POST['form']
        else:
            user=entrepreneur.objects.get(entrepreneurid=request.session['userid'])
            user.form=request.POST['form']
        user.save()
        return redirect('home')

def comment(request):
     if request.method == "POST":
        userid=request.session['userid']
        comment = request.POST.get('description')
        # imageId=request.POST.get('imageId')
       
        post_id = request.POST['submit']
        prod = Comment(comment = comment,userid=userid,post_id=post_id)
        print("Hii2")
        prod.save()
        print("Hi1")
        messages.success(request,"comment sucessfully")
      
        return redirect('home' )
    
     return redirect( 'home' )


    