from django.contrib.auth.models import User
import re

class UserFactory:

    def create_user(self, username: str, email: str, password1: str, password2: str ):
        if not self._username_valid(username):
            return None

        if not self._email_valid(email):
            return None

        if not self._password_valid(password1, password2):
            return None
        try:
            user = User.objects.create_user(username, email, password1)
        except:
            return None
        return user

    def _username_valid(self, username: str) -> bool:
        regex = '^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
        if (re.search(regex, username)):
            return True
        print("username invalid")
        return False

    def _email_valid(self, email: str) -> bool:
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if (re.search(regex, email)):
            return True
        print("email invalid")
        return False

    def _password_valid(self, password1: str, password2: str) -> bool:
        if not (password1 and password2 and password1 == password2):
            print("password invalid")
            return False
        return True