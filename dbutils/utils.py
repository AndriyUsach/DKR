class DBUtils:
    @staticmethod
    def get_task_query(obj, username: str):
        query_set = obj.objects.filter(user=username)
        return query_set

    @staticmethod
    def get_task_id(obj, username, id):
        tasks = obj.objects.filter(user=username)
        task = tasks.filter(pk=id)
        if task:
            return task
        return None

    @staticmethod
    def create_task(obj, task, finish_date, user)->bool:
        try:
            task = obj(task=task, finish_date=finish_date, user=user)
            task.save()
            return True
        except:
            print("save error")
            return False

    @staticmethod
    def update_task(obj, id, task, finish_date, user) -> bool:
        try:
            obj_task = obj.objects.get(pk=id)
            obj_task.task = task
            obj_task.finish_date = finish_date
            obj_task.user = user
            obj_task.save()

            return True
        except:
            return False

    @staticmethod
    def delete_task(obj, id) -> bool:
        try:
            obj.objects.get(pk=id).delete()
            return True
        except:
            return False
