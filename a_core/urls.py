from django.contrib import admin
from django.urls import path
from a_posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view)
]
