from restaurant.models import RestaurantDetail, AboutUs, Award, Function, Gallery, GalleryImage, Enquiry, BookingInfo

def get_restaurant_details():
    restaurant_list = RestaurantDetail.objects.all()
    if restaurant_list:
        detail = restaurant_list[0]
        return {
            'name': detail.name,
            'mail': detail.mail,
            'phone': detail.phone,
            'address': detail.address.split('\n'),
            'days_open': detail.days_open.split('\n'),
            'is_reservation_open':detail.is_reservation_open,
            'fb_page': detail.fb_page,
            'insta_page': detail.insta_page
        }

def get_about_data():
    our_story_details = AboutUs.objects.all().filter(name='our_story')
    if our_story_details:
        return our_story_details[0].description.split('\n')
    else:
        return None 

def get_award_details():
    return Award.objects.all()

def get_function_details():
    function_details = Function.objects.all()
    function_list = []
    if function_details:
        for func in function_details:
            function = {}
            function['name'] = func.name
            function['description'] = func.description.split('\n')
            function['list'] = func.list_points.split('\n')
            function['price'] = func.price
            function['people'] = func.max_people
            function['image'] = func.image
            function_list.append(function)
        return function_list
    else:
        return None

def save_enquiry_message(name, mail, subject, message):
    try:
        p = Enquiry.objects.create(
        name=name,
        mail=mail,
        subject=subject,
        message=message
        )
        return True
    except Exception as e:
        return False

def save_booking_info(name, mail, phone, booking_date, time, peopleCount, message):
    try:
        p = BookingInfo.objects.create(
            name=name,
            mail=mail,
            phone=phone,
            booking_date=booking_date,
            time=time,
            people_count=peopleCount,
            message=message
        )
        return True
    except Exception as e:
        print(e)
        return False

def get_images():
    images = GalleryImage.objects.all()
    slide_images = images.filter(name__name__contains="slider")
    gallery_images = images.filter(name__name__contains='gallery')
    return slide_images, gallery_images
   