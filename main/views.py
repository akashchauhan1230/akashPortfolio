import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        enq = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            contact=contact
        )
        enq.save()
        
        # Use environment variables instead of hardcoded credentials
        url = "http://sms.bulkssms.com/submitsms.jsp"
        params = {
            "user": os.getenv('SMS_GATEWAY_USER', 'default_user'),
            "key": os.getenv('SMS_GATEWAY_KEY', ''),
            "email": f"{contact}",
            "message": "Thanks for enquiry we will contact you soon.\n\n-Bulk SMS",
            "senderid": os.getenv('SMS_GATEWAY_SENDER_ID', 'UPDSMS'),
            "accusage": "1",
            "entityid": os.getenv('SMS_ENTITY_ID', ''),
            "tempid": os.getenv('SMS_TEMP_ID', '')
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            print("SMS Response:", response.text)
            messages.success(request, "Your message has been sent successfully!")
        except requests.exceptions.RequestException as e:
            print(f"SMS Gateway Error: {str(e)}")
            messages.warning(request, "Message saved but SMS notification failed. We'll contact you soon!")
        
        return redirect('index')
    
    return render(request, 'index.html')
    