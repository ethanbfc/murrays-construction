from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('plastering-and-rendering/', PlasteringAndRenderingView.as_view(), name="plastering-and-rendering"),
    path('building-works/', BuildingWorksView.as_view(), name="building-works"),
    path('media-walls/', MediaWallsView.as_view(), name="media-walls"),
    path('landscaping/', LandscapingView.as_view(), name="landscaping"),
    path('extensions-and-renovations/', ExtensionsAndRenovationsView.as_view(), name="extensions-and-renovations"),
]
