from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'second_name', 'last_name']

class UserRegistrationSerializer(RegisterSerializer):
    """
    Сериализатор регистрации

    """
    username = None
    first_name = serializers.CharField(max_length=20)
    second_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'second_name', 'last_name']

    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.second_name = self.data.get('second_name')
        user.last_name = self.data.get('last_name')
        user.save()
        return user

    # def custom_signup(self, request, user):
    #     user.first_name = self.validated_data.get('first_name', '')
    #     user.second_name = self.validated_data.get('second_name', '')
    #     user.last_name = self.validated_data.get('last_name', '')
    #     user.save(update_fields=['first_name', 'last_name', 'second_name'])

    # def get_cleaned_data(self):
    #     return {
    #         'username': self.validated_data.get('username', ''),
    #         'password1': self.validated_data.get('password1', ''),
    #         'email': self.validated_data.get('email', '')
    #     }

    # def validate_username(self, username):
    #     return username

    # def save(self, request):
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     adapter.save_user(request, user, self)
    #     self.custom_signup(request, user)
    #     setup_user_email(request, user, [])

    #     return user
