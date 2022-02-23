from django.contrib import admin

from apps.core.models import ResolutionCategory

# Register your models here.


class ModelAdminMixin:
    def get_queryset(self, request):
        qs = super(ModelAdminMixin, self).get_queryset(request)
        self.request = request
        return qs


class ResolutionCategoryAdmin(admin.ModelAdmin):
    model = ResolutionCategory
    list_display = ("name", "created_at", "updated_at")
    list_filter = ("name", "created_at", "updated_at")
    search_fields = ("name", "created_at", "updated_at")


admin.site.register(ResolutionCategory, ResolutionCategoryAdmin)
