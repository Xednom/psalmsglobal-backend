from django.contrib import admin

from apps.prepaid.models import (
    AccountBalance,
    CustomerInteractionPrepaid,
    MinutesReport,
    PaymentSummary,
    SubscriptionInfo,
    PrepaidSubscription
)

admin.site.register(AccountBalance)
admin.site.register(CustomerInteractionPrepaid)
admin.site.register(MinutesReport)
admin.site.register(PaymentSummary)
admin.site.register(SubscriptionInfo)
admin.site.register(PrepaidSubscription)