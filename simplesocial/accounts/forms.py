from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ['username', 'email', 'password1', 'password2'] # putin psw once and confirm with second one
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # customize the website form labels
        self.fields['username'].label = 'Display User Name'
        self.fields['email'].label = 'Email Address'
