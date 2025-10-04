from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class Tab1View(TemplateView):
    template_name = 'tab_1.html'

class Tab2View(TemplateView):
    template_name = 'tab_2.html'

class Tab3View(TemplateView):
    template_name = 'tab_3.html'

class Tab4View(TemplateView):
    template_name = 'tab_4.html'

class Tab5View(TemplateView):
    template_name = 'tab_5.html'

class Tab6View(TemplateView):
    template_name = 'tab_6.html'
