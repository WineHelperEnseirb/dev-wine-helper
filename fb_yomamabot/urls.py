from django.conf.urls import include, url
from .views import YoMamaBotView
urlpatterns = [
                  url(r'^9850eea4020c130fb92af877a626248479ef038f67a8638090/?$', YoMamaBotView.as_view()) 
               ]
