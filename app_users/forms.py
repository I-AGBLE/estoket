from django import forms


from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=50,
        label="",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "required": True,
                "autofocus": True,
            }
        ),
    )

    password = forms.CharField(
        max_length=50,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "required": True,
            }
        ),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "required": True,
                "autofocus": True,
            }
        ),
    )

    password = forms.CharField(
        max_length=50,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "required": True,
            }
        ),
    )

    confirm_password = forms.CharField(
        max_length=50,
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "required": True,
            }
        ),
    )

    email = forms.EmailField(max_length=100, 
        label="",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "required": True,
            }
        ),
    )

    about = forms.CharField(
        label="",
        max_length=200,
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Tell us about yourself..."}),
    )
    
    bio = forms.CharField(
        label="",
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Tell us about yourself..."}),
    )

