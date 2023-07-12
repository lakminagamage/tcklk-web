from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from website.views import contactView,legalView,creativesView,solutionsView,eventsView,estoreView,indexView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView , name='homeUrl'),
    path('accounts/', include('accounts.urls'), name='accountUrls'),
    #path('accounts/', include('allauth.urls')),
    path('legal/', legalView , name='legalUrl'),
    path('contacts/', contactView, name='contactsUrl'),
    path('creatives/', creativesView, name='creativesUrl'),
    path('solutions/', solutionsView, name='solutionsUrl'),
    path('events/', eventsView, name='eventsUrl'),
    path('estore/', estoreView, name='estoreUrl'),
    path('third-party/', include('allauth.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE