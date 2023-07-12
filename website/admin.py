from django.contrib import admin
from .models import ContactFormModel
from .models import PortfolioItems,TestimonialItems,ClientlogoItems


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    class Meta:
        model = ContactFormModel

admin.site.register(ContactFormModel ,WebsiteAdmin)

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'sort_by']
    class Meta:
        model = PortfolioItems

admin.site.register(PortfolioItems ,WebsiteAdmin)

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_name', 'sort_by']
    class Meta:
        model = TestimonialItems

admin.site.register(TestimonialItems ,WebsiteAdmin)

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'sort_by']
    class Meta:
        model = ClientlogoItems

admin.site.register(ClientlogoItems ,WebsiteAdmin)

