from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import class_views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


router = DefaultRouter()
router.register(r'snippets', class_views.SnippetViewSet)
router.register(r'users', class_views.UserViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls))
]
