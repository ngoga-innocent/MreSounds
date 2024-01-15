from django import forms
from django.forms import ModelForm
from .models import Skills,Chapter
from ckeditor.widgets import CKEditorWidget

class AddSKills(ModelForm):
    class Meta:
        model=Skills
        fields=('title','body','exercise')
        widgets = {
        'body': CKEditorWidget(),
        'exercise': CKEditorWidget(),
    }
class AddChapterForm(ModelForm):
    class Meta:
        model=Chapter
        fields=('title','icon')