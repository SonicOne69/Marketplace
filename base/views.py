from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
    post = Post.objects.all()
    categories = Categories.objects.all()
    context = {'posts': post, 'categories': categories}
    return render(request, 'base/home.html', context)

@login_required(login_url='/login/')
def create_post(request: HttpRequest) -> HttpResponse:
    form: Create_post = Create_post()
    categories = Categories.objects.all()
    if request.method == 'POST':
        print(request.FILES)
        image = request.FILES.get('image')
        price: int = request.POST.get('price') 
        currency_id: int = request.POST.get('currency')
        currency = Currency.objects.get(id = currency_id)
        title: str = request.POST.get('title')
        description: str = request.POST.get('description')
        adress: str = request.POST.get('adress')
        user_id: int = request.POST.get('user')
        user = User.objects.get(id = user_id)
        category_id: int = request.POST.get('category')
        if category_id == 'new':
            categories = Categories.objects.all()
            new_category:str = request.POST.get('new_category', '').replace(' ', '').lower()
            for x in categories:
                if new_category == x.name.replace(' ', '').lower():
                    messages.error(request, 'This categorie already exists')
                    return render(request, 'base/create_post.html', {'form': form, 'categories': categories})
            category = Categories.objects.create(
                name = request.POST.get('new_category')
            )
            
        else:
            category = Categories.objects.get(id = category_id)
       
        Post.objects.create(
            currency = currency,
            price = price,
            image = image,
            user = user,
            title = title,
            description = description,
            adress = adress,
            categorie = category
        )
        return redirect('main')
        
            
        
        # get_form = forms.Create_post(request.POST)
        # if get_form.is_valid():
        #     get_form.save()
        #     return redirect('main')
    return render(request, 'base/create_post.html', {'form': form, 'categories': categories})

def search(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        categories = Categories.objects.all()
        filter = Post.objects.filter(title__icontains = q)
        if filter.first() == None:
            messages.error(request, 'Sorry no posts yet ')
        if q == '':
            filter = Post.objects.all()
        context = {'posts': filter, 'categories': categories}
        return render(request, 'base/home.html', context)       

def categories(request, category):
    filter = Post.objects.filter(categorie__name = category)
    categories = Categories.objects.all()
    context = {'posts': filter, 'categories': categories}
    return render(request, 'base/home.html', context)       

def post_page(request, postname):
    post = Post.objects.get(title = postname)
    context = {
        'post':post
    }
    return render(request, 'base/post_page.html', context)
@login_required(login_url='/login/')
def chat(request, chatname):
    message = Message.objects.filter(page__title = chatname)
    chat_name = Post.objects.get(title = chatname)
    if request.htmx:
        new_message = Message.objects.create(
            text = request.POST.get('message'),
            page = chat_name,
            user = request.user
        )
        return render(request, 'base/partials/partial_mes.html', {'message': new_message, 'chatname': chat_name})
    return render(request, 'base/chat.html', {'messages': message, 'chatname': chat_name})

def login_user(request):
    page = 'login'
    form = UserCreate()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Sorry this user does not exist')
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'base/reg_log.html', context)

def register(request):
    page = 'register'
    form = UserCreate()
    if request.POST:
        form = UserCreate(request.POST)
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('main')
    context = {
        'page': page,
        'form': form
    }
    return render(request, 'base/reg_log.html', context)

def logout_user(request):
    logout(request)
    return redirect('main')