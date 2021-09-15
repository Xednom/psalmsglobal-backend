from django.contrib import admin


from apps.newsfeed.models import NewsFeed, NewsFeedComment


class NewsFeedCommentAdmin(admin.TabularInline):
    model = NewsFeedComment
    extra = 1
    readonly_fields = ("created_at", "user")


class NewsFeedAdmin(admin.ModelAdmin):
    model = NewsFeed
    list_display = ("title", "body", "publish_to")
    inlines = [NewsFeedCommentAdmin]
    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()


admin.site.register(NewsFeed, NewsFeedAdmin)
