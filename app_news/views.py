from django.shortcuts import render

# Create your views here.
def tin_tuc(request):

    return render(request,'app_news/blog-list.html')

def chi_tiet_tin_tuc(request):

    return render(request,'app_news/blog-single.html')