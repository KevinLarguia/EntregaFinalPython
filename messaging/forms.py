from django import forms
from django.contrib.auth.models import User
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content']
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto del mensaje'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Escribe tu mensaje aquí...'
            }),
        }
        labels = {
            'receiver': 'Para',
            'subject': 'Asunto',
            'content': 'Mensaje',
        }

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        if current_user:
            self.fields['receiver'].queryset = User.objects.exclude(pk=current_user.pk).order_by('username')
