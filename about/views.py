from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'Django Reyhan',
        'author': 'Reyhan Anf',
        'sapaan': 'Halo, Selamat datang',
    }
    return render(request, 'index.html', context)
