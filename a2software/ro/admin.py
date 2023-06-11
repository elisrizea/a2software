from django.contrib import admin
from .models import (
    HomePage,
    AboutPage,
    FaqsPage,
    AdmFaqs,
    CookiePage,
    PlatformPage,
    WebappePage,
    Testimonial,
    BaseHeaderFooterMenu,
    ContactPage,
    Emails,
)

# Register your models here.
admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(FaqsPage)
admin.site.register(AdmFaqs)
admin.site.register(CookiePage)
admin.site.register(PlatformPage)
admin.site.register(WebappePage)
admin.site.register(Testimonial)
admin.site.register(BaseHeaderFooterMenu)
admin.site.register(ContactPage)
admin.site.register(Emails)
