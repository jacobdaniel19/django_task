from django.shortcuts import render,redirect
from django.views.generic import View
from Company_app.models import Category_model,Employee_model
from Company_app.forms import Category_modelform,Employee_modelform
# Create your views here.


class Reg_category(View):

    def get(self,request,*args,**kwargs):

        form=Category_modelform()

        return render (request,"reg_cat.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=Category_modelform(request.POST)

        if form.is_valid():

            form.save()

        return render (request,"reg_cat.html",{"form":form})    


class Reg_employee(View):

    def get(self,request,*args,**kwargs):

        form1=Employee_modelform()

        return render (request,"reg_emp.html",{"form":form1})
    
    def post(self,request,*args,**kwargs):
        
        form1=Employee_modelform(request.POST)

        if form1.is_valid():

            form1.save()

        return render(request,"reg_emp.html")   

class Read_all(View):

    def get(self,request,*args,**kwargs): 

        data=Category_model.objects.all()

        data1=Employee_model.objects.all()


        return render(request,"read_all.html",{"data":data,"data1":data1})    
    
class Read_specific(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data1=Employee_model.objects.filter(id=id)

        print(data1)

        return render(request,"read_emp.html",{"data1":data1})
    

class Del_cat(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Category_model.objects.get(id=id).delete()

        print("deleted successfully")

        return redirect("r_cat")
    
class Del_emp(View):

     def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee_model.objects.get(id=id).delete()

        print("deleted successfully")

        return redirect("r_emp")


class Update_emp(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data=Employee_model.objects.get(id=id)

        form=Employee_modelform(instance=data)

        return render(request,"update_cat.html",{"form":form})
    

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data=Employee_model.objects.get(id=id)

        form=Employee_modelform(request.POST,instance=data)

        return render(request,"update_cat.html",{"form":form})
       
