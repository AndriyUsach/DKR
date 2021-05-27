import redis
import os

from json import loads
from json import dumps

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from dbutils.utils import DBUtils

from .serializer import  TaskSerializer
from .models import Task


HOST = os.environ.get("REDIS_HOST")
PORT = os.environ.get("REDIS_PORT")
DB = os.environ.get("REDIS_DB")
redis = redis.Redis(HOST, port=PORT, db=DB)


class CarView(APIView):
    def __init__(self):
        super().__init__()
        self.db = DBUtils
        self.serializer = TaskSerializer
        self.model = Task

    def get(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)

        username = request.user.username
        id = request.query_params.get('id', None)

        if id is None:
            tasks = self.db.get_task_query(self.model, username)
            tasks_serializer = self.serializer(tasks, many=True)
            return Response(tasks_serializer.data, status=200)

        return self.get_detail(username, id)

    def get_detail(self, username: str, id: int):
        task = redis.get(id)
        if task:
            data = loads(task)
            return Response(data, status=200)

        task = self.db.get_task_id(self.model, username, id)
        if not task:
            return Response(status=400)

        task_serializer = self.serializer(task)
        data = task_serializer.data

        redis.set(id, dumps(data))
        return Response(data, status=200)

    def post(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)
        data = loads(request.body)
        data_serializer = self.serializer(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)

        if not self.db.update_car(data_serializer.data, data_serializer.data['id']):
            return Response(status=400)
        redis.delete(data_serializer.data['id'])
        return Response(status=200)

    def put(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)

        data = loads(request.body)
        data_serializer = self.serializer(data=data)

        if not data_serializer.is_valid():
            return Response(status=400)

        id = data_serializer.data['id']
        task = data_serializer.data['id']
        finish_date = data_serializer.data['finish_date']
        user = data_serializer.data['finish_date']

        if not self.db.update_task(self.model, id, task, finish_date, user):
            return Response(status=400)
        return Response(status=200)

    def delete(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)

        id = loads(request.body)['id']
        status = self.db.delete_task(self.model, id)

        if status:
            redis.delete(id)
            return Response(status=200)

        return Response(status=400)


