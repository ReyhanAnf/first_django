from django.shortcuts import render

# Create your views here.
def index(request):
    info = {
        'judul': 'My Contact',
        'name': 'Reyhan',
        'gmail': 'reyhananf7@gmail.com',
        'whatsapp': '085871235944'
    }
    return render(request, 'blog/contact.html', info)