from django import forms

class getURL(forms.Form):
    url = forms.CharField(label = "Enter Playlist URL", max_length = 100)