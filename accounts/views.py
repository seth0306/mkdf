from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm


class IndexView(TemplateView):
    """_summary_

    Args:
        TemplateView (_type_): _description_
    """

    template_name = "index.html"


class SignupView(CreateView):
    """_summary_

    Args:
        CreateView (_type_): _description_

    Returns:
        _type_: _description_
    """

    form_class = SignUpForm  # 作成した登録用フォームを設定
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:index")  # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response


# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "login.html"


# ログアウトビューを作成
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")
