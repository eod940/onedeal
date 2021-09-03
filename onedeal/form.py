from django import forms
from django.forms import Textarea, TextInput

from onedeal.models import LandingApply


class LandingApplyForm(forms.ModelForm):

    class Meta:
        model = LandingApply
        fields = [
            'apply_name',
            'apply_phonenum',
            'apply_email',
            'apply_birth',
            'apply_content',
        ]

        labels = {
            'apply_name': '이름-',
            'apply_phonenum': '연락처',
            'apply_email': '이메일',
            'apply_birth': '생년월일',
            'apply_content': '상세내용',
        }

        widgets = {
            'apply_name': TextInput(attrs={'class': 'form-control', 'placeholder': '이름을 입력하세요'}),
            'apply_phonenum': TextInput(attrs={'class': 'form-control', 'placeholder': '010xxxxxxxx'}),
            'apply_email': TextInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}),
            'apply_birth': TextInput(attrs={'class': 'form-control', 'placeholder': '생년월일 6자리'}),
            'apply_content': Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': '상세내용을 입력하세요'}),
        }
