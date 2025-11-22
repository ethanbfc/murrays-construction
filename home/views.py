from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class PlasteringView(TemplateView):
    template_name = 'plastering.html'

class BuildingWorksView(TemplateView):
    template_name = 'building_works.html'

class MediaWallsView(TemplateView):
    template_name = 'media_walls.html'

class Tab4View(TemplateView):
    template_name = 'tab_4.html'

class Tab5View(TemplateView):
    template_name = 'tab_5.html'
