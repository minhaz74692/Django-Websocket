from django.shortcuts import render
from django.http import HttpResponse

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification_count(request, count):
    try:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifications',
            {
                'type': 'send_notification',
                'notification_count': count
            }
        )
        print("-----------Success-----------", count)
        return HttpResponse("Success Notification")
    except Exception as e:
        print("-----------Error__________", count, ":", e)
        
        return HttpResponse(e)
        

def homeData(request):
    return HttpResponse("This is home page")


def signup(request):
   if request.method == 'POST':
        # Handle form submission (optional)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # You can add logic to save the data or create a user here
        return HttpResponse(f"Welcome, {username}! ")
   return render(request, "signup.html")
    
