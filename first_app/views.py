
from django.shortcuts import render
from first_app.models import RealUser


# Create your views here.

def test_template(request):
    my_dir = {}
    return render(request, "help.html", my_dir)


def user_data(request):
    print(RealUser.objects.all())
    d = {"md": RealUser.objects.all()}
    return render(request, "data.html", d)
