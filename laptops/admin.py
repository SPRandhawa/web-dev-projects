from django.contrib import admin
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Brand, Laptop, Category, Banner, ContactMessage, Review

from .models import Comparison

#cpadmin.site.register(Brand)
from .models import Comparison

from .models import Accessory

@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'rating', 'ram', 'ssd', 'processor', 'display', 'battery', 'gpu', 'portability', 'ports', 'connectivity', 'category')

# ✅ Review
admin.site.register(Review)


# ✅ Contact Message (EMAIL LOGIC)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'reply', 'is_replied')

    def save_model(self, request, obj, form, change):

        # 🔥 MUST BE INDENTED
        if obj.reply and not obj.is_replied:

            html_content = render_to_string('email/reply_email.html', {
                'name': obj.name,
                'reply': obj.reply,
            })

            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                subject="Reply from BuyLaptop",
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[obj.email],
            )

            email.attach_alternative(html_content, "text/html")
            email.send()

            obj.is_replied = True

        super().save_model(request, obj, form, change)


# ✅ Banner
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'banner_type')
    list_filter = ('banner_type',)


# ✅ Brand
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


# ✅ Laptop
@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price_min', 'price_max', 'is_featured', 'last_updated')
    list_filter = ('brand', 'is_featured')
    search_fields = ('name',)


# ✅ Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# accessories model


admin.site.register(Accessory)