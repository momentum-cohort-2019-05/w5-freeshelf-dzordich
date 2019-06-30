from django import forms
    
class CommentForm(forms.Form):
    user_comment = forms.CharField(max_length=256, help_text="Enter comment (max: 256 chars)")
