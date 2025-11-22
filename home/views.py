from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class PlasteringView(TemplateView):
    template_name = 'plastering.html'

class BuildingWorksView(TemplateView):
    template_name = 'building_works.html'

class MediaWallsView(TemplateView):
    template_name = 'media_walls.html'

class LandscapingAndFencingView(TemplateView):
    template_name = 'landscaping_and_fencing.html'

class ExtensionsAndRenovationsView(TemplateView):
    template_name = 'extensions_and_renovations.html'
