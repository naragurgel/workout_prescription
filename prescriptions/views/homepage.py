from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


def error_404_view(request, exception):
    """
    Displays 404.html path
    """

    return render(request, '404.html')


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