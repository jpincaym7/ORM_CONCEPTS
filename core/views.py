# core/views.py

from django.views.generic import TemplateView, ListView
from django.apps import apps
from django.http import Http404

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener todos los modelos de la app 'core'
        modelos = [model.__name__ for model in apps.get_app_config('core').get_models()]
        context['modelos'] = modelos
        return context

class ListaObjetosView(ListView):
    template_name = 'lista_objetos.html'  # Ruta por defecto al template HTML
    context_object_name = 'objetos'  # Nombre del contexto en el template

    def get_queryset(self):
        modelo_nombre = self.kwargs['modelo']
        try:
            Modelo = apps.get_model('core', modelo_nombre)
        except LookupError:
            raise Http404(f"Modelo '{modelo_nombre}' no encontrado.")
        return Modelo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelo'] = self.kwargs['modelo']
        return context
