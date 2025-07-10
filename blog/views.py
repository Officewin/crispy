from django.views.generic import TemplateView


class IndexView(TemplateView):
    # "frontend" is included in TEMPLATES['DIRS'], so we only need the
    # template filename here. Using a simple name avoids the duplicated
    # "frontend/frontend" path that caused TemplateDoesNotExist errors.
    template_name = 'index.html'