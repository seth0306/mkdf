from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
        )
        labels = {
            "account_id": "アカウントID",
            "email": "E-Mail",
            "last_name": "姓",
            "first_name": "名",
        }


# ログインフォームを追加
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
