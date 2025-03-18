# Interface for notification channels
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete notification channel implementations
class EmailNotification(NotificationChannel):
    def send(self, message):
        return f"Sending Email: {message}"

class SMSNotification(NotificationChannel):
    def send(self, message):
        return f"Sending SMS: {message}"

class PushNotification(NotificationChannel):
    def send(self, message):
        return f"Sending Push Notification: {message}"

# Notification Manager that bridges the resource and notification channel
class NotificationManager:
    def __init__(self, resource):
        self.resource = resource
        self.notification_channels = []

    def add_channel(self, channel):
        self.notification_channels.append(channel)

    def notify(self, message):
        results = []
        for channel in self.notification_channels:
            results.append(channel.send(f"{message} about {self.resource.get_details()}"))
        return results

# Bridge between Resource and Notification
class ResourceNotificationManager:
    def __init__(self, resource, channels):
        self.notification_manager = NotificationManager(resource)
        for channel in channels:
            self.notification_manager.add_channel(channel)

    def send_notification(self, message):
        return self.notification_manager.notify(message)