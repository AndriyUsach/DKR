from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


class AccountUtils:
    def save_user(self, user: User):
        user.save()

    def login_user(self, user: User, request):
        login(request, user)

    def logout_user(self, request):
        logout(request)

    def authenticate(self, username, password):
        user = authenticate(username=username, password=password)
        return user

