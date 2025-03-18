from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from factory import *

app = FastAPI(title="Library Management System")


class ResourceCreate(BaseModel):
    resource_type: str
    title: str
    author: Optional[str] = None
    issue: Optional[str] = None
    format: Optional[str] = None


class NotificationRequest(BaseModel):
    message: str
    channels: List[str]


resources = {}
notifications_history = []


@app.post("/resources")
async def create_resource(resource: ResourceCreate):
    try:
        resource_obj = ResourceFactory.create_resource(
            resource.resource_type,
            title=resource.title,
            author=resource.author,
            issue=resource.issue,
            format=resource.format
        )
        resource_id = len(resources) + 1
        resources[resource_id] = resource_obj
        return {"id": resource_id, "details": resource_obj.get_details()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/resources/{id}")
async def get_resource(id: int):
    resource = resources.get(id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return {"id": id, "details": resource.get_details()}


@app.post("/notifications")
async def send_notification(resource_id: int, notification: NotificationRequest):
    resource = resources.get(resource_id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

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
