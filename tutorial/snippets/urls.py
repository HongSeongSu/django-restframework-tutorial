from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import class_views

router = DefaultRouter()
router.register(r'snippets', class_views.SnippetViewSet)
router.register(r'users', class_views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
