from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import NewsModel, TegsModel, AdditionalImage


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", "imageee", "views_new", "create_at")
    ordering = ["-create_at"]
    search_fields = ("name", "tegs")
    list_display_links = ("name", "imageee")
    exclude = ["views_new"]

    def imageee(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return "None"

    imageee.short_description = "Image"
    inlines = (AdditionalImageInline,)


@admin.register(TegsModel)
class TegsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
