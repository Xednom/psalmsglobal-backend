from django.contrib import admin


# commented this out first due to models not being able to be integrated yet.
# class SubscriptionAdmin(admin.ModelAdmin):
#     model = Subscription
#     list_display = (
#         "company",
#         "signed_up_date",
#         "signed_out_date",
#         "biling_cycle",
#         "date_call_started",
#         "status",
#     )
#     list_filter = ("company",)
#     search_fields = (
#         "company",
#         "company__client__user__first_name",
#         "client__user__last_name",
#         "client__client_code",
#     )
#     readonly_fields = ("created_at", "updated_at")
#     fieldsets = (
#         (
#             "Subscription Information",
#             {
#                 "fields": (
#                     "company",
#                     "signed_up_date",
#                     "signed_out_date",
#                     "billing_cycle",
#                     "date_call_started",
#                     "status",
#                     "script_created",
#                     "notes"
#                 )
#             },
#         ),
#     )