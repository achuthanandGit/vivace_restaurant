from django.db import models

# Create your models here.
class RestaurantDetail(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    mail = models.EmailField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    fb_page = models.CharField(max_length=255, null=False, blank=True)
    insta_page = models.CharField(max_length=255, null=False, blank=True)
    days_open = models.TextField()
    is_reservation_open = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Restaurant Information"


class AboutUs(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=False)

    class Meta:
        verbose_name_plural = "About Us Information"

class Award(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Awards Obtained"

class Function(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    list_points = models.TextField(blank=True, null=False)
    max_people = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to = 'function/')

    class Meta:
        verbose_name_plural = "Event Information"

class Gallery(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Gallery Categories"
 
class GalleryImage(models.Model):
    name = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'gallery/')

    class Meta:
        verbose_name_plural = "Images to Upload to Gallery"

class Enquiry(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    mail = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=255, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    submitted_date_time = models.DateTimeField(auto_now_add=False)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Customer Enquiry"

class BookingInfo(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    mail = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    booking_date = models.DateField(blank=False, null=False)
    time = models.CharField(max_length=20, blank=False, null=False)
    people_count = models.IntegerField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    submitted_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Booking Information"

class FoodCategory(models.Model):
    category = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Food Category"

class FoodMenu(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    category = models.ForeignKey(FoodCategory, default=None, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Food Menu"

class DrinksCategory(models.Model):
    category = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Drinks Category"

class DrinksSubCategory(models.Model):
    sub_category = models.CharField(max_length=255, blank=False, null=True)
    category = models.ForeignKey(DrinksCategory, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category

    class Meta:
        verbose_name_plural = "Drinks Sub Category"

class DrinksMenu(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    category = models.ForeignKey(DrinksCategory, default=None, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(DrinksSubCategory, default=None, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Drinks Menu"



    
