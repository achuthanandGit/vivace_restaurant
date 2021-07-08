from django.shortcuts import render, HttpResponse

import restaurant.model_facade as mf

import json

# Create your views here.
def load_home(request):
    """
        loads the home page
    """
    context = {}

    context['restaurant'] = mf.get_restaurant_details()

    context['ourStory'] = mf.get_about_data()
    
    context['awards'] = mf.get_award_details()

    context['events'] = mf.get_function_details()

    slider_images, gallery_images = mf.get_images()
    context['gallery'] = gallery_images
    context['slider'] = slider_images


    return render(request, 'restaurant/home.html', context)


def submit_contact(request):
    isSuccess = False
    message = 'Invalid request, Please try again.'

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and mail and subject and message:
            isSuccess = mf.save_enquiry_message(name, mail, subject, message)
            if isSuccess:
                message = 'Message submitted successfully.'
            else:
                message = 'Internal error occured, please try again.'
        else:
            isSuccess = False
            message = 'All fields are required.'

    response_data = {
        'isSuccess':isSuccess,
        'message':message
    }
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def submit_booking(request):
    isSuccess = False
    message = 'Invalid request, Please try again.'

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        booking_date = request.POST.get('date')
        time = request.POST.get('time')
        peopleCount = request.POST.get('peopleCount')
        message = request.POST.get('message')
        if name and mail and phone and booking_date and time and message:
            isSuccess = mf.save_booking_info(name, mail, phone, booking_date, time, peopleCount, message)
            if isSuccess:
                message = 'Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!'
            else:
                message = 'Internal error occured, please try again.'
        else:
            isSuccess = False
            message = 'All fields are required.'

    response_data = {
        'isSuccess':isSuccess,
        'message':message
    }
    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )