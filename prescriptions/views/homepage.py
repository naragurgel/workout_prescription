from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

class HomePageView(TemplateView):
    template_name = "index.html"


def error404(request):
     template = loader.get_template('404.html')
     context = Context({'message': 'All: %s' % request,})
     return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)


def handler500(request, *args, **argv):
    """
    Displays 500.html path
    """
    return render(request, '500.html')

def handler403(request, *args, **argv):
    """
    Displays 403.html path
    """
    return render(request, '403.html')

    