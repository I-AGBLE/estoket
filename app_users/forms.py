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
    """
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

    email = forms.EmailField(max_length=100, 
        label="",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "required": True,
            }
        ),
    )
"""
    USER_TYPE_CHOICES = [
    ('freelancer', 'Freelancer'),
    ('company', 'Company'),
    ('other', 'Other'),
]

    # Correct field for choices
    user_type = forms.ChoiceField(
        label="",
        choices=USER_TYPE_CHOICES,
        initial='other',  # default selection
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    """
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
"""
