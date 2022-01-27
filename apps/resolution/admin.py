from django.contrib import admin

from apps.resolution.models import Resolution, ResolutionConversation


class ResolutionConversation(admin.TabularInline):
    model = ResolutionConversation
    extra = 1


class ResolutionAdmin(admin.ModelAdmin):
    model = Resolution
    list_filter = ("category", "assigned_to", "client")
    list_display = ("category", "assigned_to", "client", "status")
    fieldsets = (
        (
            "Resolution",
            {"fields": ("category", "assigned_to", "client", "status", "description")},
        ),
    )
    inlines = [ResolutionConversation]


admin.site.register(Resolution, ResolutionAdmin)
