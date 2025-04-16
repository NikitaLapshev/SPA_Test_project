from django import forms
from captcha.fields import CaptchaField
import bleach

from .models import Comment
from .validators import validate_html

ALLOWED_TAGS = ['b', 'i', 'u', 'em', 'strong', 'a']

class CommentForm(forms.ModelForm):
    username = forms.RegexField(
        regex = r'^[a-zA-Z0-9]+$',
        max_length = 30,
        required = True,
        label = 'User Name',
        error_messages = {'Error': 'Only Latin letters and numbers'}
    )
    email = forms.EmailField()
    homepage = forms.URLField(required=False)
    text = forms.CharField(widget=forms.Textarea, validators=[validate_html])
    attachment = forms.FileField(required=False)
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'homepage', 'text', 'attachment']

    def clean_text(self):
        text = self.cleaned_data['text']
        return bleach.clean(text, tags=ALLOWED_TAGS, strip=True)


