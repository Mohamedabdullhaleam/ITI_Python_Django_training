from django.urls import path
from homepage.views import helloworld,welcome,sayhi,multplybyten,home,aboutus,contactus,show,delete,create,index,details,deletee,edit,createViaForm

urlpatterns = [
    path('hello/',helloworld,name="myhello"),
    path('welcome/',welcome,name="weeeee"),
    path('welcomeme/<username>',sayhi,name="welcoming"),
    path('mult/<int:num>',multplybyten,name="multiplication"),
    path('home/',home,name="HOME"),
    path('aboutus/',aboutus,name="aboutus"),
    path('contactus/',contactus,name="contactus"),
    path('<int:id>', show, name='laptops.show'),
    # path('<int:course_id>/delete', delete, name='courses.delete'),
    # path('create',create, name='prod.create'),
    path('s',index ,name='products.index'),
    path('<int:id>/details',details, name='products.details'),
    path('<int:id>/delete',deletee ,name='products.delete'),
    path('create', create, name='products.create'),
    path('<int:id>/edit', edit, name='products.edit'),
    path('forms/create', createViaForm, name='products.createForm'),
    # path('forms/create', createViaForm, name='students.createForm'),
    # path('forms/model/create', createViaModelForm, name='students.createForm'),
    # path('<int:id>/edit', edit, name='students.edit')


]