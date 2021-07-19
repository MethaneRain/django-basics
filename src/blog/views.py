from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request,*args, **kwargs):
    print('args:',args,'\nkwargs:',kwargs)
    print('request user:',request.user)
    my_context = {"my_text": "High five",
    "my_number": 43,
    "my_list": [123,432,634],
    "my_dict": {"cat":"EF5","wndmax":162,"KI":-12.4,"county":"BOU"},
    "my_html": "<h1>Tornado Malaise</h1>",
    }
    return render(request, "home.html", my_context)
    #return HttpResponse("<h2>oh yes</h2><ul><li><a href='http://127.0.0.1:8000/about/'>About</a></li><li><a href='http://127.0.0.1:8000/contact/'>Contact</a></li></ul>")


def about_view(request,*args, **kwargs):
    return render(request, "about.html", {})
    #return HttpResponse("<h2>oh yes. Here's something about me!</h2><br><a href='https://apod.nasa.gov/apod/astropix.html' target='_blank'>Family friendly site</a>")

def contact_view(request,*args, **kwargs):
    return HttpResponse("<h2>oh yes</h2><a href='https://github.com/MethaneRain' target='_blank'>Here's how to contact me:</a><br><br><br><br><br><br><br><br>----------------------------------<br><br><br><img src='https://www.placecage.com/gif/200/300'>")
