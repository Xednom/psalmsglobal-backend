from django.contrib import admin

from apps.grading.models import PostpaidInteractionRate, PrepaidInteractionRate


admin.site.register(PostpaidInteractionRate)
admin.site.register(PrepaidInteractionRate)