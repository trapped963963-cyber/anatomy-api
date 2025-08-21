from fastapi import FastAPI
from fastapi.responses import JSONResponse

# This is our main FastAPI app instance
app = FastAPI()

# This is the contact information you can change later
CONTACT_INFO = {
    "contact_number": "+963997564200", # Your WhatsApp/Telegram number
}

# This defines our single API endpoint
@app.get("/api/get-contact-info")
def get_contact_info():
    """
    This endpoint returns the current contact number for app activation.
    """
    return JSONResponse(content=CONTACT_INFO)