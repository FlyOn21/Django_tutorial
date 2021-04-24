from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r"question", views.QuestionViewSet, )
router.register(r"choice", views.ChoiceViewSet, )

app_name = "api"
urlpatterns = [
 path("",include(router.urls)),
 path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]