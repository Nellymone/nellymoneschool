from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Branch, Gallery
from .models import News
from .models import Gallery


def about5_10(request):
    return render(request, 'main/5-10.html')

def about11_17(request):
    return render(request, 'main/11-17.html')

def group(request):
    return render(request, 'main/group.html')

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'main/pictures.html', {'images': images})

def training(request):
    return render(request, 'main/training.html')


def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    news = News.objects.order_by('-created_at')[:3]

    return render(request, 'main/home.html', {
        'form': form,
        'news': news
    })

def branches(request):
    branches = Branch.objects.all()
    return render(request, 'main/branches.html', {'branches': branches})


