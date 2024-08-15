from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login", 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: John Doe"
            }
        )
    )
    senha = forms.CharField(
        label="Senha", 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome completo",
        required=True,
        max_length=250,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: John Doe"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=250,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: john.doe@email.com"
            }
        )
    )
    password_1 = forms.CharField(
        label="Senha", 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    password_2 = forms.CharField(
        label="Confirmação de senha", 
        required=True, 
        max_length=70, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha mais uma vez"
            }
        )
    )