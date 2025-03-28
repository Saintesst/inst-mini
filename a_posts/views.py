from django.shortcuts import render

def home_view(request):
    print('Hello')
    return render(request, 'a_posts/home.html')
