from news.models import TegsModel


def kind_contexttt(request):
    navbar_tegs = TegsModel.objects.all()
    context = {'navbar_tegs': navbar_tegs}
    return context
