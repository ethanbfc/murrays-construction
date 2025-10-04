from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('tab-1/', Tab1View.as_view(), name="tab-1"),
    path('tab-2/', Tab2View.as_view(), name="tab-2"),
    path('tab-3/', Tab3View.as_view(), name="tab-3"),
    path('tab-4/', Tab4View.as_view(), name="tab-4"),
    path('tab-5/', Tab5View.as_view(), name="tab-5"),
    path('tab-6/', Tab6View.as_view(), name="tab-6"),
]
