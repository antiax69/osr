from django import forms
from osr.models import SudokuModel

class SudokuForm(forms.ModelForm):

    class Meta:
        model = SudokuModel
        fields = ('image',)
