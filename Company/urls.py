"""
URL configuration for Company project.

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
from Company_app.views import Reg_category,Reg_employee,Read_all,Read_specific,Del_cat,Del_emp,Update_emp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg_cat/',Reg_category.as_view(),name="r_cat"),
    path('reg_emp/',Reg_employee.as_view(),name="r_emp"),
    path('read_spec/<int:pk>',Read_specific.as_view()),
    path('read_all/',Read_all.as_view()),
    path('del/<int:pk>',Del_cat.as_view()),
    path('del_emp/<int:pk>',Del_emp.as_view()),
    path('up_emp/<int:pk>',Update_emp.as_view()),


]
