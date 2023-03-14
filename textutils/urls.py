"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views #here we imported our file that was made by us
# from . import exercise1 --it is for the exeercise1

# it's about previous chapter
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('adm',views.adm,name='adm'),
#     # path('',views.text,name='text')
#     path('web',exercise1.web,name='web')
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index2, name='index2'),
    path('analyze',views.analyze,name='analyze'),
    path('About',views.About,name='About'),
    path('Contact',views.Contact,name='Contact')
    # path("capfirst",views.capfirst,name='capfirst'),
    # path("newlineremove",views.newlineremove,name='newlineremove'),
    # path("spaceremove",views.spaceremove,name='spaceremove'),
    # path('charcount',views.charcount,name='charcount')
]
