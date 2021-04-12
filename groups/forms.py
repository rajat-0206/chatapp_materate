from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserDataCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email','first_name','last_name',)


class UserDataChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')