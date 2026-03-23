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
        ("freelancer", "Freelancer"),
        ("company", "Company"),
        ("other", "Other"),
    ]

    # Correct field for choices
    user_type = forms.ChoiceField(
        label="",
        choices=USER_TYPE_CHOICES,
        initial="other",  # default selection
        widget=forms.Select(attrs={"class": "form-control"}),
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


class CompanyForm(forms.Form):
    COMPANY_SIZE_CHOICES = [
        ("1-10", "1-10"),
        ("11-20", "11-20"),
        ("21-50", "21-50"),
        ("50+", "More than 50"),
    ]

    company_name = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Company Name", "required": True}),
    )

    about = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell us about your company",
                "rows": 4,
                "required": True,
            }
        ),
    )

    location = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Location", "required": True}),
    )

    year_founded = forms.DateField(
        label="Date Founded",
        widget=forms.DateInput(
            attrs={
                "type": "date",  # triggers calendar picker
                "required": True,
                'class': 'form_date'  
            }
        ),
    )

    industry = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Industry", "required": True}),
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "Email", "required": True}),
    )
    
    telephone = forms.CharField(
        max_length=13,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telephone",
                "required": True,
                "pattern": "[0-9]{1,13}",
                "title": "Enter up to 13 digits"
            }
        )
    )
    
    company_size = forms.ChoiceField(
        choices=COMPANY_SIZE_CHOICES,
        label="",
        widget=forms.Select(attrs={"required": True}),
    )

    logo = forms.ImageField(label="Company Logo", required=False)
    
    
    
    

class ExpertiseForm(forms.Form):
    expertise_title = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Expertise Title",
            "required": True
        })
    )

    expertise_desc = forms.CharField(
        label="",
        max_length=500,
        widget=forms.Textarea(attrs={
            "placeholder": "Describe your expertise",
            "rows": 4,
            "required": True
        })
    )
