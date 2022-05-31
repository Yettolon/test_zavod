from django.shortcuts import render

from news.models import NewsModel


def index(request):
    if "teg" in request.GET:
        news = NewsModel.objects.filter(tegs__pk=request.GET["teg"]).prefetch_related(
            "tegs"
        )
    else:
        news = NewsModel.objects.prefetch_related("tegs").all()
    context = {"news": news}
    return render(request, "main/index.html", context)


def alone(request, pk):
    new = NewsModel.objects.defer("tegs").get(pk=pk)
    view = new.views_new + 1
    new.views_new = view
    new.save()
    ais = new.additionalimage_set.all()
    return render(request, "main/alone.html", {"new": new, "ais": ais})


def statistics(request):
    news_stat = NewsModel.objects.all().order_by("-views_new").defer("tegs")
    context = {"news_stat": news_stat}
    return render(request, "main/statis.html", context)
