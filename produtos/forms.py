from django import forms
from django.forms import fields, widgets
from .models import Review


REVIEW_CHOICES = [('1','1'), ('2','2'),('3','3'),('4','4'),('5','5')]

class Review_Form(forms.ModelForm):

    class Meta:

        model = Review
        fields = ['texto', 'rating']
        
        widgets = {

            'text':forms.Textarea(attrs={

                'class':'form-control shadow px-2', 'rows':6
            }
            ), 'rating':forms.RadioSelect(
                
                choices=REVIEW_CHOICES
            )
        }