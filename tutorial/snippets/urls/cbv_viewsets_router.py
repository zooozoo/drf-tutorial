from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from snippets.views.cbv_viewsets import SnippetViewSet

router = DefaultRouter()
router.register(r'', SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]