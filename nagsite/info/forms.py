from .models import project
from django.forms import ModelForm, TextInput,Textarea,TimeInput,DateInput,NumberInput


class projectForm(ModelForm):
    class Meta:
        model = project
        fields = ["name", "description", "team_quantity"]
        widgets = {
            "name": TextInput(),
            "description": Textarea(),
            "team_quantity": NumberInput(),
        }