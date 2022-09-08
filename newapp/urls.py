from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("BlogCategory", views.BlogViewSet)
app_name = "newapp"
urlpatterns = [
    path("", include(router.urls)),
]
