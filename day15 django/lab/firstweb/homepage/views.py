from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from homepage.models import Course,category
from homepage.forms import StudentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def helloworld(request):
    return HttpResponse('hello world ')
def welcome(request):
    return HttpResponse('<h1 style="color:red"> HI ITI  </h1>')
def sayhi (request,username):
    return HttpResponse(f'<h1 style="color:red"> hi {username}</h1>')
def multplybyten(request,num):
    return HttpResponse(f"answer is :{num*10}")

students = [
        {"id":1, "name":'Asus ROG', "image":"Asus ROG.png", 'price':1000 ,'discription':'gaming laptop'},
        {"id":2, "name":'ASUS_ROG_Strix', "image":"ASUS_ROG_Strix.png", "price":8000 ,'discription':'gaming laptop'},
        {"id":3, "name": 'ASUS_TUF_Gaming_F15', "image": "ASUS_TUF_Gaming_F15png.png","price":3000,'discription':'gaming laptop'},
        {"id":4, "name": 'HP_Victus_16', "image": "HP_Victus_16.png","price":40000,'discription':'gaming laptop'},
        {"id":5, "name": 'laptop-lenovo-gaming3', "image": "laptop-lenovo-gaming.png","price":30000,'discription':'gaming laptop'},
        {"id":6, "name": 'Legion_5_Pro_16', "image": "Legion_5_Pro_16.png","price":45000,'discription':'gaming laptop'}
    ]



def home(request):
    Courses = Course.objects.all()
    return render(request,"Home.html", context = {"name":"noha", 'students':Courses})
def show(request, id):
    stds = filter(lambda std: std["id"] == id, students)
    std = list(stds)[0]
    return  render(request, 'show.html', context={"student":std})

def contactus(request):
    return render(request, "contactus.html")
def aboutus(request):
    return render(request, "aboutus.html")

def show(request, id):
    stds = filter(lambda std: std["id"] == id, students)
    std = list(stds)[0]
    return  render(request, 'show.html', context={"student":std})
login_required()
def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    bact_to_url = reverse('HOME')
    return redirect(bact_to_url)

# def create (request):
#     print(request)
#     if request.method =="POST":
#         request_data = request.POST
#         print(request_data)
#         print("hhhh")
#         Name=request_data['name']
#         Price=request_data['price']
#         image =request_data['image']
#         description=request_data['description']
#         No_items=request_data['no_items']
#         course= Course(name=Name ,price=Price,description=description , image=image ,no_items = No_items )
#         course.save()

    #     return HttpResponse("post request succeded")
    # return render(request,'create.html')
def index(request):
    Courses = Course.get_all_products()
    return render(request,"crud/index.html", context = {'students':Courses})
def details(request, id):
    student = Course.get_specific_student(id)
    return render(request, 'crud\show.html', context={"students":student})

@login_required()
def deletee(request, id):
    deletedcourse = Course.get_specific_student(id)
    deletedcourse.delete()
    url = reverse('products.index')
    return redirect(url)

def create(request):
    Categories = Course.get_all_products()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        # return HttpResponse("post request succeded")
        ## validation part
        if request.POST['name'] == '' or request.POST['price'] == '' or request.POST['description'] == '':
            return render(request, 'students/crud/create.html', context={"Categories": Categories})

        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None



        track=None
        if 'category_id' in request.POST:
            track = category.get_specific_category(request.POST['category_id'])

        crs =Course(name=request.POST['name'], price=request.POST['price'],description=request.POST['description'] ,image=image, no_items=request.POST['no_items'],categ_id=request.POST['category_id'])
        crs.save()
        url = reverse('products.index')
        return redirect(url)

    categories = category.get_all_categorys()
    return render(request, 'crud/create.html', context={"categories":categories})
def edit(request,id):

    products = Course.get_specific_student( id)
    if request.method == 'POST':

        products.name = request.POST['name']
        if 'image' in request.FILES:
            products.image = request.FILES['image']

        products.price = request.POST['price']
        products.save()

        url = reverse('products.index')
        return redirect(url)

    return render(request, 'crud/edit.html', context={'product': products})
def createViaForm(request):
    form = StudentForm()

    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = StudentForm(request.POST, request.FILES)
        # return HttpResponse("not data form")
        if form.is_valid():
            if 'image' in request.FILES:
                image = request.FILES['image']
            else:
                image = None

            track = None
            if 'category_id' in request.POST:
                track = category.get_specific_category(request.POST['category_id'])

            crs = Course(name=request.POST['name'], price=request.POST['price'],
                         description=request.POST['description'], image=image, no_items=request.POST['no_items'],
                         categ_id=request.POST['categ_id'])
            crs.save()
            url = reverse('products.index')
            return redirect(url)

        print(form.errors)

        return render(request,'crud/createusingform.html', context={"form":form})

    return render(request,'crud/createusingform.html', context={"form":form})