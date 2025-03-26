from abc import ABC, abstractmethod
import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
import jwt
from typing import Any, Optional, Dict


class LibraryResource(ABC):
    def __init__(self, resource_id: str, title: str, created_date: datetime.date):
        self.resource_id = resource_id
        self.title = title
        self.created_date = created_date

    @abstractmethod
    def get_details(self) -> dict:
        pass

    @abstractmethod
    def check_available(self) -> bool:
        pass


class Book(LibraryResource):
    def __init__(
        self,
        resource_id: str,
        title: str,
        created_date: datetime.date,
        author: str,
        isbn: str,
        publisher: str,
    ):
        super().__init__(resource_id, title, created_date)
        self.author = author
        self.isbn = isbn
        self.publisher = publisher

    def get_details(self) -> dict:
        return {
            "resource_id": self.resource_id,
            "title": self.title,
            "created_date": self.created_date.isoformat(),
            "type": "book",
            "author": self.author,
            "isbn": self.isbn,
            "publisher": self.publisher,
        }

    def check_available(self) -> bool:
        return True


class Journal(LibraryResource):
    def __init__(
        self,
        resource_id: str,
        title: str,
        created_date: datetime.date,
        volume: str,
        issue: str,
        field: str,
    ):
        super().__init__(resource_id, title, created_date)
        self.volume = volume
        self.issue = issue
        self.field = field

    def get_details(self) -> dict:
        return {
            "resource_id": self.resource_id,
            "title": self.title,
            "created_date": self.created_date.isoformat(),
            "type": "journal",
            "volume": self.volume,
            "issue": self.issue,
            "field": self.field,
        }

    def check_available(self) -> bool:
        return True


class DigitalMedia(LibraryResource):
    def __init__(
        self,
        resource_id: str,
        title: str,
        created_date: datetime.date,
        format: str,
        size: str,
        duration: str,
    ):
        super().__init__(resource_id, title, created_date)
        self.format = format
        self.size = size
        self.duration = duration

    def get_details(self) -> dict:
        return {
            "resource_id": self.resource_id,
            "title": self.title,
            "created_date": self.created_date.isoformat(),
            "type": "digital_media",
            "format": self.format,
            "size": self.size,
            "duration": self.duration,
        }

    def check_available(self) -> bool:
        return True


class ResourceFactory:
    @staticmethod
    def create_resource(resource_type: str, resource_data: dict) -> LibraryResource:
        if resource_type == "book":
            return Book(
                resource_id=resource_data["resource_id"],
                title=resource_data["title"],
                created_date=resource_data["created_at"],  # Changed from created_date to created_at
                author=resource_data["author"],
                isbn=resource_data["isbn"],
                publisher=resource_data["publisher"],
            )
        elif resource_type == "journal":
            return Journal(
                resource_id=resource_data["resource_id"],
                title=resource_data["title"],
                created_date=resource_data["created_at"],  # Changed from created_date to created_at
                volume=resource_data["volume"],
                issue=resource_data["issue"],
                field=resource_data["field"],
            )
        elif resource_type == "digital_media":
            return DigitalMedia(
                resource_id=resource_data["resource_id"],
                title=resource_data["title"],
                created_date=resource_data["created_at"],  # Changed from created_date to created_at
                format=resource_data["format"],
                size=resource_data["size"],
                duration=resource_data["duration"],
            )
        else:
            raise ValueError(f"Invalid resource type: {resource_type}")


class NotificationChannel(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass


class EmailNotification(NotificationChannel):
    def send_notification(self, message: str) -> None:
        print(f"Sending email: {message}")


class SMSNotification(NotificationChannel):
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS: {message}")


class PushNotification(NotificationChannel):
    def send_notification(self, message: str) -> None:
        print(f"Sending push notification: {message}")


class NotificationManager:
    def __init__(self, notification_channel: NotificationChannel):
        self.notification_channel = notification_channel

    def send(self, message: str) -> None:
        self.notification_channel.send_notification(message)


SECRET_KEY = "kandsglmflasdm"


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class APIKeyHandler(AbstractHandler):
    VALID_API_KEYS = {"admin_api_key", "user_api_key"}

    def handle(self, request: dict) -> str:
        api_key = request.get("api_key")
        if api_key in self.VALID_API_KEYS:
            return f"API Key Authenticated: {api_key}"
        return super().handle(request)


class JWTHandler(AbstractHandler):
    def handle(self, request: dict) -> str:
        token = request.get("jwt_token")
        if not token:
            return super().handle(request)
        try:
            decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request["user"] = decoded_data
            return f"JWT Authenticated: {decoded_data}"
        except jwt.ExpiredSignatureError:
            return "JWT Error: Token expired"
        except jwt.InvalidTokenError:
            return "JWT Error: Invalid token"
        return super().handle(request)


class RoleHandler(AbstractHandler):
    def handle(self, request: dict) -> str:
        user_data = request.get("user", {})
        user_role = user_data.get("role")
        if not user_role:
            return "Role Error: No role found"
        if user_role == "admin":
            return "Access Granted: Admin"
        elif user_role == "user":
            return "Access Granted: Regular User"
        else:
            return "Role Error: Unauthorized role"
        return super().handle(request)


api_key_handler = APIKeyHandler()
jwt_handler = JWTHandler()
role_handler = RoleHandler()

api_key_handler.set_next(jwt_handler).set_next(role_handler)

app = FastAPI()


class ResourceData(BaseModel):
    resource_id: str
    title: str
    created_at: datetime.date
    author: Optional[str] = None
    isbn: Optional[str] = None
    publisher: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    field: Optional[str] = None
    format: Optional[str] = None
    size: Optional[str] = None
    duration: Optional[str] = None


class NotificationData(BaseModel):
    message: str
    channel: str


resources = dict()

notifications = list()

notification_channels = {
    "email": EmailNotification(),
    "sms": SMSNotification(),
    "push": PushNotification(),
}


@app.post("/resources")
def create_resource(resource_type: str, resource_data: ResourceData):
    try:
        resource = ResourceFactory.create_resource(resource_type, resource_data.dict())
        resources[resource.resource_id] = resource
        return {"message": f"{resource_type.capitalize()} created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/resources/{resource_id}")
def get_resource(resource_id: str):
    resource = resources.get(resource_id)
    if resource:
        return resource.get_details()
    raise HTTPException(status_code=404, detail="Resource not found")


@app.post("/notifications")
def send_notification(notification_data: NotificationData):
    channel = notification_channels.get(notification_data.channel)
    if not channel:
        raise HTTPException(status_code=400, detail="Invalid notification channel")
    manager = NotificationManager(channel)
    manager.send(notification_data.message)
    notifications.append(
        {
            "message": notification_data.message,
            "channel": notification_data.channel,
            "timestamp": datetime.datetime.now().isoformat(),
        }
    )
    return {"message": "Notification sent successfully"}


@app.get("/notifications/history")
def get_notification_history():
    return notifications


@app.post("/auth/token/")
def get_access_token(request: Dict):
    now = datetime.datetime.utcnow()
    return {
        "message": api_key_handler.handle(request),
        "time": f"{(datetime.datetime.utcnow() - now).microseconds} seconds",
    }


def create_jwt_token(data: Dict) -> str:
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    data["exp"] = expiration
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


@app.post("/auth/acc_tok/")
def get_access(data: Dict):
    token = create_jwt_token(data)
    return {"access_token": token, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
