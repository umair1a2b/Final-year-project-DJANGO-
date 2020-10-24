from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session

# Create your views here.
def main(request):
    return render(request,'client/pages/main.html')
def contact(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/contact.html')
    return render(request, 'client/pages/main.html')
def portfolio(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/portfolio.html')
    return render(request, 'client/pages/main.html')
def about(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/about.html')
    return render(request, 'client/pages/main.html')
def video(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/video.html')
    return render(request, 'client/pages/main.html')
def video1(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/video1.html')
    return render(request, 'client/pages/main.html')
def video2(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/video2.html')
    return render(request, 'client/pages/main.html')
def video3(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/video3.html')
    return render(request, 'client/pages/main.html')
def video4(request):
    if request.session.has_key('is_logged'):
        return render(request,'client/pages/video4.html')
    return render(request, 'client/pages/main.html')
def login(request):
    if request.POST:
        email=request.POST["email"]
        password=request.POST["password"]

        count=User.objects.filter(email=email,password=password).count()
        if count >0:
            request.session['is_logged']=True
            request.session['user_id']=User.objects.values('id').filter(email=email,password=password)[0]['id']
            type=User.objects.get(email=email,password=password).type
            if type==0:
                return redirect("home")
            return redirect("view")


        else:
            messages.error(request,"Invalid Email or Password")
            return redirect("login")

    return render(request,'client/pages/login.html')
def signup(request):
    return render(request,'client/pages/signup.html')
def signup_user(request):
    if request.POST:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        type=request._post['type']

        obj=User(first_name=first_name,last_name=last_name,password=password,email=email,phone=phone,type=type)
        obj.save()
        messages.success(request,"You are Signup sucessfully")
    return render(request,'client/pages/login.html')
def home(request):
    if request.session.has_key('is_logged'):
        fetch_data=Hall.objects.all()
        return render(request,'client/pages/home.html',{'data':fetch_data})
    return render(request,'client/pages/login.html')
def logout(request):
    del request.session['is_logged']
    return redirect('main')
def register(request):
    if request.session.has_key('is_logged'):
        if request.POST:
            name=request.POST['name']
            capacity=request.POST['capacity']
            address=request.POST['address']
            phone=request.POST['phone']
            description=request.POST['description']
            image=request.FILES['image']
            menu=request.POST['menu']
            video=request.POST['video']
            dj=request.POST['dj']
            flourist=request.POST['flourist']
            type=request.POST['type']
            separation=request.POST['separation']
            user_id=User.objects.get(id=request.session['is_logged'])

            obj=Hall.objects.create(name=name,capacity=capacity,address=address,phone=phone,description=description,image=image,menu=menu,video=video
                 ,dj=dj,flourist=flourist,type=type,separation=separation,user_id=user_id)

            messages.success(request, "You are Register sucessfully")
            return redirect('view')
        return render(request,'client/pages/register.html')
    return render(request, 'client/pages/main.html')

def book(request):
    if request.session.has_key('is_logged'):
        if request.POST:
            capacity = request.POST['capacity']
            event = request.POST['event']
            videographer = request.POST['videographer']
            package = request.POST['package']
            menu = request.POST['menu']
            decor = request.POST['decor']
            dj = request.POST['dj']
            separate = request.POST['separate']
            date = request.POST['date']
            user_id = request.session['user_id']
            hall_id=Hall.objects.values('id')
            obj=Book(capacity=capacity, event=event, videographer=videographer,
                                                   package=package,
                                                   menu=menu, decor=decor, dj=dj, separate=separate, date=date)
            obj.user_id_id=user_id
            obj.hall_id_id=hall_id
            obj.save()
            return redirect('home')
        return render(request, 'client/pages/book.html')
    return render(request, 'client/pages/main.html')
def view(request):
    if request.session.has_key('is_logged'):
        if request.method == 'POST':
            name = request.POST['name']
            capacity = request.POST['capacity']
            address = request.POST['address']
            phone = request.POST['phone']
            description = request.POST['description']
            image = request.FILES['image']
            menu = request.POST['menu']
            video = request.POST['video']
            dj = request.POST['dj']
            flourist = request.POST['flourist']
            type = request.POST['type']
            separation = request.POST['separation']
            id=request.POST['hall_id']
            Hall.objects.filter(id=id).update(name=name, capacity=capacity, address=address, phone=phone,
                                                  description=description, image=image,
                                                  menu=menu, video=video, dj=dj, flourist=flourist, type=type,
                                                  separation=separation)
            return redirect('view')
        data = Hall.objects.all()
        return render(request, 'client/pages/view.html', {'data': data})
    return render(request,'client/pages/main.html')



def update(request,id):
    if request.session.has_key('is_logged'):
        data = Hall.objects.get(id=id)
        return render(request, 'client/pages/update.html', {'var': data})
    return render(request,'client/pages/main.html')

def update_client(request,id):
    if request.session.has_key('is_logged'):
        data = Hall.objects.get(id=id)
        return render(request, 'client/pages/update_client.html', {'var': data})
    return render(request,'client/pages/main.html')


def delete(request,id):
    if request.session.has_key('is_logged'):
        Hall.objects.filter(id=id).delete()
        return redirect('view')
    return render(request,'client/pages/main.html')

def booking(request):
    if request.session.has_key('is_logged'):
        if request.method == 'POST':
            capacity = request.POST['capacity']
            event = request.POST['event']
            videographer = request.POST['videographer']
            package = request.POST['package']
            menu = request.POST['menu']
            decor = request.POST['decor']
            dj = request.POST['dj']
            separate = request.POST['separate']
            date = request.POST['date']
            id = request.POST['hall_id']
            Book.objects.filter(id=id).update(capacity=capacity,event=event,videographer=videographer,package=package,
                                              menu=menu,decor=decor,dj=dj,separate=separate,date=date)
            return redirect('home')
        data = Book.objects.all()
        return render(request, 'client/pages/booking.html', {'data': data})
    return render(request, 'client/pages/main.html')














def remove_hall(request,id):
    Hall.objects.get(id=id).delete()
    return redirect('testing')

def update_hall(request,id):
    data = Hall.objects.get(id=id)
    return render(request,'update.html',{'hall':data})

def testing(request):
    if request.method=='POST':
        name= request.POST['name']
        description = request.POST['description']
        id = request.POST['hallid']
        Hall.objects.filter(id=id).update(name=name,description = description)
        return redirect('testing')
    data = Hall.objects.all()
    return render(request,'testing.html',{'data':data})