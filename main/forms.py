from django.forms import ModelForm, TextInput, Textarea,NumberInput
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'placeholder': 'Enter Name',
            }),
            "amount": NumberInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'min': 1,
                'placeholder': 'Enter Amount',
            }),
            "description": Textarea(attrs={
                'class': 'min-w-[370px] max-h-[150px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'placeholder': 'Enter Description',
            })
        }
