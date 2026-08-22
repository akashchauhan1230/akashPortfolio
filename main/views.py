import os
# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect
# pyrefly: ignore [missing-import]
from django.contrib import messages
from .models import Contact
import requests
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        contact = request.POST.get('contact', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # 1. Safely save contact enquiry to database
        db_saved = False
        try:
            enq = Contact(
                name=name,
                email=email,
                subject=subject,
                message=message,
                contact=contact
            )
            enq.save()
            db_saved = True
        except Exception as e:
            print(f"Database Save Error: {str(e)}")

        # 2. SMS Notification (only if credentials are provided)
        sms_user = os.getenv('SMS_GATEWAY_USER')
        sms_key = os.getenv('SMS_GATEWAY_KEY')
        if sms_key and sms_user and sms_user != 'default_user':
            url = os.getenv('SMS_GATEWAY_URL', 'http://sms.bulkssms.com/submitsms.jsp')
            params = {
                "user": sms_user,
                "key": sms_key,
                "email": contact,
                "message": "Thanks for enquiry we will contact you soon.\n\n-Bulk SMS",
                "senderid": os.getenv('SMS_GATEWAY_SENDER_ID', 'UPDSMS'),
                "accusage": "1",
                "entityid": os.getenv('SMS_ENTITY_ID', ''),
                "tempid": os.getenv('SMS_TEMP_ID', '')
            }
            try:
                response = requests.get(url, params=params, timeout=5)
                print("SMS Response:", response.text)
            except Exception as e:
                print(f"SMS Gateway Error: {str(e)}")

        if db_saved:
            messages.success(request, "Your message has been sent successfully! I will contact you soon.")
        else:
            messages.info(request, "Thank you for reaching out! Your message was received.")
            
        return redirect('index')
    
    return render(request, 'index.html')

    