from django.shortcuts import render


# Create your views here.

def test_template(request):
    my_dir = {}
    return render (request, "help.html", my_dir)
