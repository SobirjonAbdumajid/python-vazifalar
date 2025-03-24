# integration_to_fast_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from Lesson.factory import LibraryResource, ResourceFactory, ResourceNotificationManager, \
    EmailNotification, PushNotification, SMSNotification, Dict

app = FastAPI(title="Library Management System")

# In-memory storage
resources: Dict[int, LibraryResource] = {}
notifications_history: List[dict] = []


class ResourceCreate(BaseModel):
    resource_type: str
    title: str
    author: Optional[str] = None
    isbn: Optional[str] = None
    publisher: Optional[str] = None
    volume: Optional[int] = None
    issue: Optional[int] = None
    field: Optional[str] = None
    format: Optional[str] = None
    size: Optional[float] = None
    duration: Optional[int] = None


class NotificationRequest(BaseModel):
    message: str
    channels: List[str]


@app.post("/resources/")
async def create_resource(resource: ResourceCreate):
    resource_data = resource.dict(exclude_unset=True)
    resource_data["resource_id"] = len(resources) + 1
    try:
        resource_obj = ResourceFactory.create_resource(resource.resource_type, resource_data)
        resources[resource_data["resource_id"]] = resource_obj
        return {"id": resource_data["resource_id"], "details": resource_obj.get_details()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/resources/{id}")
async def get_resource(id: int):
    resource = resources.get(id)
    if not resource:
        raise HTTPException(status_code=200, detail="Out of stock")
    return {"id": id, "details": resource.get_details(), "available": resource.check_available()}


@app.post("/notifications/")
async def send_notification(resource_id: int, notification: NotificationRequest):

    resource = resources.get(resource_id)
    if not resource:
        raise HTTPException(status_code=200, detail="Out of stock")

    channels = []
    for channel_type in notification.channels:
        if channel_type.lower() == "email":
            channels.append(EmailNotification())
        elif channel_type.lower() == "sms":
            channels.append(SMSNotification())
        elif channel_type.lower() == "push":
            channels.append(PushNotification())
        else:
            raise HTTPException(status_code=400, detail=f"Unknown channel: {channel_type}")

    notification_manager = ResourceNotificationManager(resource, channels)
    results = notification_manager.send_notification(notification.message)
    notifications_history.append({"resource_id": resource_id, "message": notification.message, "results": results})
    return {"status": "Notifications sent", "results": results}


@app.get("/notifications/history")
async def get_notifications_history():
    return notifications_history
