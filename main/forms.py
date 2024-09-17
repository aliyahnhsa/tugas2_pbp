from django.forms import ModelForm
from main.models import GamesEntry

class GamesEntryForm(ModelForm):
    class Meta:
        model = GamesEntry
        fields = ["name", "price", "description"]