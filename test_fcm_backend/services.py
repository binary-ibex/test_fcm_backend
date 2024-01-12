from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification


def send_message():
    message = Message(
        notification=Notification(title="Angry cat", body="hello world", image="https://picsum.photos/200"),
    )

    # You can still use .filter() or any methods that return QuerySet (from the chain)
    device = FCMDevice.objects.all().first()
    # send_message parameters include: message, dry_run, app
    device.send_message(message)