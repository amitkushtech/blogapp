from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
# router.register("socialAuth", views.FacebookSocialAuthView)
app_name = "socialauth"
urlpatterns = [
    path("", include(router.urls)),
    path("socialauth", views.FacebookSocialAuthView.as_view(), name="socialauth"),
]
