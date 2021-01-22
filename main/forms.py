from django import forms
from .models import Match, Stats


class MatchCreateForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ['date', 'yourTeam', 'homeTeam', 'awayTeam', 'homeGoals', 'homePoints', 'awayGoals', 'awayPoints']
        labels = {
            'yourTeam': 'Your team',
            'homeTeam': 'Home team',
            'awayTeam': 'Away team',
            'homeGoals': 'Home goals',
            'homePoints': 'Home points',
            'awayGoals': 'Away goals',
            'awayPoints': 'Away points',
        }
        widgets = {
            'date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'})
        }