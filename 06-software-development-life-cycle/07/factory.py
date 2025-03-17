from abc import ABC, abstractmethod


class LibraryResource(ABC):
    @abstractmethod
    def get_details(self):
        pass


class Book(LibraryResource):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Book: {self.title} by {self.author}"


class Journal(LibraryResource):
    def __init__(self, title, issue):
        self.title = title
        self.issue = issue

    def get_details(self):
        return f"Journal: {self.title}, Issue {self.issue}"


class DigitalMedia(LibraryResource):
    def __init__(self, title, format):
        self.title = title
        self.format = format

    def get_details(self):
        return f"DigitalMedia: {self.title}, Format: {self.format}"


class ResourceFactory:
    @staticmethod
    def create_resource(resource_type, **kwargs):
        if resource_type.lower() == "book":
            return Book(kwargs.get("title"), kwargs.get("author"))
        elif resource_type.lower() == "journal":
            return Journal(kwargs.get("title"), kwargs.get("issue"))
        elif resource_type.lower() == "digitalmedia":
            return DigitalMedia(kwargs.get("title"), kwargs.get("format"))
        else:
            raise ValueError(f"Unknown resource type: {resource_type}")






# Interface for notification channels
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationChannel):
    def send(self, message):
        return f"Sending Email: {message}"


class SMSNotification(NotificationChannel):
    def send(self, message):
        return f"Sending SMS: {message}"


class PushNotification(NotificationChannel):
    def send(self, message):
        return f"Sending Push Notification: {message}"


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

class ResourceNotificationManager:
    def __init__(self, resource, channels):
        self.notification_manager = NotificationManager(resource)
        for channel in channels:
            self.notification_manager.add_channel(channel)

    def send_notification(self, message):
        return self.notification_manager.notify(message)