"""
URL configuration for smartcity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from smartcity.smartcity.views import *
from .views import *
from . import views
#from .views import cluster_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',main),
    path('',main),
    path('signin/',signin),
    path('premium/',premium),
    path('community/',community),
    path('signout/',signout),
    path('signup/',signup),
    path('signup/main.html',main),
    path('signup/dashboard.html',dashboard),
    path('signin/dashboard/',dashboard),
    path('signin/dashboard.html',dashboard),
    path('signin/raisingcomplaintsection.html',raisingcomplaintsection),
    path('signin/myarea.html',myarea),
    path('signin/helpdesk.html',helpdesk),
    path('signin/home.html',main),
    path('premium/main/',main),
    path('premium/signup/',signup),
    path('premium/signin/',signin),
    path('signin/myticketssection.html',myticketssection),
    path('signin/successfulticketsection.html',successfulticketsection),
    path('signin/canceltickets.html',canceltickets),
    path('premium/community.html',community),
    path('signin/dashboard/myarea.html',myarea),
    path('signin/dashboard/dashboard.html',dashboard),
    path('signin/dashboard/community.html',community),
    path('signin/dashboard/premium.html',premium),
    path('signin/dashboard/main.html',main),
    path('signin/dashboard/premium/',premium),
    path('signin/dashboard/premium/main/',main),
    path('signin/signin/',signin),
    path('signup/raisingcomplaintsection.html',raisingcomplaintsection),
    path('signup/premium/',premium),
    path('signup/myticketssection.html',myticketssection),
    #path('cluster/', cluster_view, name='cluster'),
    path('', views.raiseticket, name="raiseticket"),
    

]
