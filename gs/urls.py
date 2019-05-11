from django.urls import path, include

from django.contrib import admin
from rest_framework import routers
from administration import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

admin.autodiscover()

# import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]