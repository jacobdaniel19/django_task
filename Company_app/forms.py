from django import forms
from Company_app.models import Category_model,Employee_model

class Category_modelform(forms.ModelForm):

    class Meta:

        model=Category_model
        fields="__all__"

class Employee_modelform(forms.ModelForm):

    class Meta:

        model=Employee_model
        fields="__all__"

    