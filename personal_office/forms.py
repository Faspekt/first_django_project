from django import forms
from users.models import User


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["avatar"]

        widgets = {
            "avatar": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            )
        }
