from django import forms
from .models import Tag

class create_new_page(forms.Form):
    title = forms.CharField(max_length=255, help_text="please enter the title of this page")
    data = forms.CharField(widget=forms.Textarea, help_text="Please enter the text")
    OPTIONS = Tag.set_all()
    tags = forms.MultipleChoiceField(help_text="Please enter the name for this tag", widget=forms.CheckboxSelectMultiple,
    choices=OPTIONS)

class add_tags_to_page(forms.Form):
    page = forms.UUIDField()
    OPTIONS = Tag.set_all()
    tags = forms.MultipleChoiceField(help_text="Please enter the name for this tag", widget=forms.CheckboxSelectMultiple,
    choices=OPTIONS)

class create_new_tag(forms.Form):
    name = forms.CharField(max_length=255, help_text="please enter name of tag")
    