from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from posts.forms import PostModelForm
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from posts.models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required


# Create your views here.
class CreatPostView(View):
    def get(self, request):
        form = PostModelForm()
        return render(request, 'posts/create.html', {'form': form})
    def post(self,request):
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("object added ")

        return render(request, 'posts/create.html', {'form': form})


## generic views
class CreatePostGenericView(CreateView):
    form_class =PostModelForm
    template_name = 'posts/create.html'
    success_url ='/posts/'

class PostListGenericView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
class PostDetailGenericView(DetailView):
    model = Post
    template_name = 'posts/show.html'

class UpdatePostGenericView(UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'posts/edit.html'
    # success_url = reverse('posts.index')
    success_url = '/posts/'

class DeletePostGenericView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = '/posts/'
