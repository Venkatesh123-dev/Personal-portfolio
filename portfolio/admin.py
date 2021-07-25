from django.contrib import admin

from .models import Portfolio, Screenshot


class EmbeddedScreenshot(admin.TabularInline):
    model = Screenshot
    extra = 1


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'live_url', 'source_url', 'port_type']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'description']
    inlines = [EmbeddedScreenshot, ]


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_filter = ['portfolio', ]
