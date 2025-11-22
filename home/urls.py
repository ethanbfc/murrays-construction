from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('plastering/', PlasteringView.as_view(), name="plastering"),
    path('building-works/', BuildingWorksView.as_view(), name="building-works"),
    path('media-walls/', MediaWallsView.as_view(), name="media-walls"),
    path('landscaping-and-fencing/', LandscapingAndFencingView.as_view(), name="landscaping-and-fencing"),
    path('tab-5/', Tab5View.as_view(), name="tab-5"),
]
