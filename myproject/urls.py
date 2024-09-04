from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("horses_app/", include("horses_app.urls"), name="horses_app-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]
