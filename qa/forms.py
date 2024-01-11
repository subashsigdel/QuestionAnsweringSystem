from django import forms
from .models import Books

class BookCreatefrom(forms.ModelForm):
    class Meta:
        model = Books
        fields = ("title","total_pages","author_name")