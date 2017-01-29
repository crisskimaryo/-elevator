"""elevator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin


from elevator_api.urls import router
# from elevator_api1.views import books
from elevator_api.views import cars

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     # url(r'^sb_api1/boo/$', books.as_view()),
    url(r'^sb_api1/cars/$', cars.as_view()),
    url(r'^sb_api1/', include(router.urls)),

]
