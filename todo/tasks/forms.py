from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    class Meta:

        # This class needs a minimum of two values : 1. What model are we using for form and 2. What fields will be used for forms

        model = Task
        fields = '__all__'      # All the fields