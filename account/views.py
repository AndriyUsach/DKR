from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from json import loads

from .factory import UserFactory
from .serializer import AccountSerializer
from .serializer import AccountLoginSerializer
from .utils import AccountUtils


class AccountView(APIView):

    def __init__(self):
        super().__init__()
        self.serializer = AccountSerializer
        self.log_serializer = AccountLoginSerializer
        self.factory = UserFactory()
        self.utils = AccountUtils()

    def get(self, request: Request):
        try:
            self.utils.logout_user(request)
        except:
            return Response(status=400)
        return Response(status=200)

    def post(self, request: Request):
        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)
        try:
            user = self.factory.create_user(**data_serializer.data)
            if user:
                self.utils.save_user(user)
                return Response(status=200)
            return Response(status=400)

        except:
            return Response(status=400)

    def put(self ,request: Request):
        data = loads(request.data)
        data_serializer = self.log_serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)
        user = self.utils.authenticate(**data_serializer.data)
        if user is not None:
            self.utils.login_user(user, request)
            return Response(status=200)
        return Response(status=400)
