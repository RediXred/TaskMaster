from celery import shared_task

@shared_task
def send_notification(user_id, task_id):
    # Пример долгой задачи: отправка уведомления пользователю
    print(f"Send notification to user: {user_id} for task: {task_id}")
