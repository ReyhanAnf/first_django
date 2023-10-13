from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'Blog Reyhan',
        'harticle': 'Tutorial Django Di Windows',
        'carticle': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ab saepe ea facere similique explicabo laboriosam, praesentium eveniet obcaecati laudantium dolorem suscipit! Iure hic laboriosam aut vero numquam dolore, odit ab fugiat, enim, ad tempore et molestias sed? Nostrum, voluptatum soluta.',
        'author': 'Reyhan Anf - Penulis',
    }
    return render(request, 'blog/blog.html', context)
