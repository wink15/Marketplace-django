from django import forms 
from .models import Item

INPUTN_CLASSES='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image')
        widgets={
            'category':forms.Select(attrs={
                'class': INPUTN_CLASSES
            }),
             'name':forms.TextInput(attrs={
                'class': INPUTN_CLASSES
            }),
              'description':forms.Textarea(attrs={
                'class': INPUTN_CLASSES
            }),
              'price':forms.TextInput(attrs={
                'class': INPUTN_CLASSES
            }),
               'image':forms.FileInput(attrs={
                'class': INPUTN_CLASSES
            })
        }