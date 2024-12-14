from fastapi import FastAPI, HTTPException
from app.schemas import EmailRequest
from app.email_utils import send_email

app = FastAPI(title="Email Service", version="1.0.0")

@app.post("/send-email")
async def send_email_endpoint(request: EmailRequest):
    try:
        send_email(request.email, request.subject, request.body)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")
