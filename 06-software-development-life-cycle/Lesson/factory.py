from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List, Optional

# Abstract LibraryResource class
class LibraryResource(ABC):
    def __init__(self, resource_id: int, title: str):
        self.resource_id = resource_id
        self.title = title
        self.created_date = datetime.now()

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def check_available(self) -> bool:
        pass

# Concrete classes
class Book(LibraryResource):
    def __init__(self, resource_id: int, title: str, author: str, isbn: str, publisher: str):
        super().__init__(resource_id, title)
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self._is_available = True

    def get_details(self) -> str:
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}, Publisher: {self.publisher}, Created: {self.created_date}"

    def check_available(self) -> bool:
        return self._is_available

    def set_availability(self, available: bool):
        self._is_available = available

class Journal(LibraryResource):
    def __init__(self, resource_id: int, title: str, volume: int, issue: int, field: str):
        super().__init__(resource_id, title)
        self.volume = volume
        self.issue = issue
        self.field = field
        self._is_available = True

    def get_details(self) -> str:
        return f"Journal: {self.title}, Volume: {self.volume}, Issue: {self.issue}, Field: {self.field}, Created: {self.created_date}"

    def check_available(self) -> bool:
        return self._is_available

    def set_availability(self, available: bool):
        self._is_available = available

class DigitalMedia(LibraryResource):
    def __init__(self, resource_id: int, title: str, format: str, size: float, duration: int):
        super().__init__(resource_id, title)
        self.format = format
        self.size = size
        self.duration = duration
        self._is_available = True

    def get_details(self) -> str:
        return f"DigitalMedia: {self.title}, Format: {self.format}, Size: {self.size}MB, Duration: {self.duration} minutes, Created: {self.created_date}"

    def check_available(self) -> bool:
        return self._is_available

    def set_availability(self, available: bool):
        self._is_available = available

# Factory class
class ResourceFactory:
    @staticmethod
    def create_resource(resource_type: str, resource_data: dict) -> LibraryResource:
        resource_id = resource_data.get("resource_id")
        title = resource_data.get("title")

        if resource_type.lower() == "book":
            return Book(
                resource_id=resource_id,
                title=title,
                author=resource_data.get("author"),
                isbn=resource_data.get("isbn"),
                publisher=resource_data.get("publisher")
            )
        elif resource_type.lower() == "journal":
            return Journal(
                resource_id=resource_id,
                title=title,
                volume=resource_data.get("volume"),
                issue=resource_data.get("issue"),
                field=resource_data.get("field")
            )
        elif resource_type.lower() == "digitalmedia":
            return DigitalMedia(
                resource_id=resource_id,
                title=title,
                format=resource_data.get("format"),
                size=resource_data.get("size"),
                duration=resource_data.get("duration")
            )
        else:
            raise ValueError(f"Unknown resource type: {resource_type}")


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass

class EmailNotification(NotificationChannel):
    def send(self, message: str) -> str:
        return f"Sending Email: {message}"

class SMSNotification(NotificationChannel):
    def send(self, message: str) -> str:
        return f"Sending SMS: {message}"

class PushNotification(NotificationChannel):
    def send(self, message: str) -> str:
        return f"Sending Push Notification: {message}"

class NotificationManager:
    def __init__(self, resource: LibraryResource):
        self.resource = resource
        self.notification_channels = []

    def add_channel(self, channel: NotificationChannel):
        self.notification_channels.append(channel)

    def notify(self, message: str) -> List[str]:
        return [channel.send(f"{message} about {self.resource.get_details()}") for channel in self.notification_channels]

class ResourceNotificationManager:
    def __init__(self, resource: LibraryResource, channels: List[NotificationChannel]):
        self.notification_manager = NotificationManager(resource)
        for channel in channels:
            self.notification_manager.add_channel(channel)

    def send_notification(self, message: str) -> List[str]:
        return self.notification_manager.notify(message)