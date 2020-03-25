from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        fields = ('email', 'username',)
        model = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        fields = ('email', 'username',)
        model = get_user_model()
