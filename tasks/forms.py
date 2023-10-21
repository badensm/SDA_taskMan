from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = ('title','desc','importance')
        exclude = ('complete_date', 'user')
        #fields = '__all__'