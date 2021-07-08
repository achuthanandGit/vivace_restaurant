from django.contrib import admin
from django.contrib.auth.models import Group, User
from rangefilter.filter import DateRangeFilter

from restaurant.models import RestaurantDetail, AboutUs, Award, Function, Gallery, GalleryImage, Enquiry, BookingInfo, FoodCategory, FoodMenu, DrinksMenu, DrinksCategory, DrinksSubCategory

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(RestaurantDetail)
class RestaurantDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'mail', 'address', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'max_people')


class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage
 
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [GalleryImageAdmin]
 
    class Meta:
       model = Gallery


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'subject', 'message', 'is_read', 'submitted_date_time',)
    readonly_fields = ('name', 'mail', 'subject', 'message', 'submitted_date_time', )
    ordering = ('-submitted_date_time',)
    list_filter = ('is_read', 'submitted_date_time',
        ('submitted_date_time', DateRangeFilter),
    )

    def has_add_permission(self, request):
        return False

@admin.register(BookingInfo)
class BookingInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone', 'booking_date', 'time', 'people_count', 'message', 'submitted_date_time',)
    ordering = ('-submitted_date_time',)
    list_filter = ('booking_date', ('booking_date', DateRangeFilter),)

class FoodMenuAdmin(admin.StackedInline):
    model = FoodMenu
 
@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    inlines = [FoodMenuAdmin]
 
    class Meta:
       model = FoodCategory
 

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available',)
    list_filter = ('is_available',)
    pass


class DrinksMenuAdmin(admin.StackedInline):
    model = DrinksMenu

class DrinksSubCategoryAdmin(admin.StackedInline):
    model = DrinksSubCategory

@admin.register(DrinksCategory)
class DrinksCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', )
    inlines = [DrinksSubCategoryAdmin]

    class Meta:
        model = DrinksCategory

@admin.register(DrinksSubCategory)
class DrinksSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_category', )
    inlines = [DrinksMenuAdmin]

    class Meta:
        model = DrinksSubCategory




