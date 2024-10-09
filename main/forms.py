from django.forms import ModelForm
from django.utils.html import strip_tags
from main.models import GameEntry

class GameEntryForm(ModelForm):
    class Meta:
        model = GameEntry
        fields = ["name", "price", "description"]
        
    def clean_game(self):
        game = self.cleaned_data["game"]
        return strip_tags(game)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)