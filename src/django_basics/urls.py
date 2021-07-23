"""django_basics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blog.views import homepage_view, about_view, contact_view
from django.contrib import admin
from django.urls import path

from products.views import product_detail_view, product_create_view#,product_py_test_view


from products.views import button,output,external,py_tests,read_file



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage_view,name="home"),
    path("home/",homepage_view,name="home"),
    path("about/",about_view,name="about"),
    path("contact/",contact_view,name="contact"),
    path("product/",product_detail_view,name="product"),
    path("create/",product_create_view),
    #path("create2/",product_py_test_view),

    #path("external/",external),

    #path("external/",numpy_test),

    path("external/",external),
    #path("external/",py_tests),

    #path("external/",read_file),

    #path("external/",py_tests),
    path('external', read_file, name='external'),
    path("home/",read_file),

    path('button', button),
    path('output', output,name="script"),
    path('wow/', output),
    path('forecaster4/', output),
]
