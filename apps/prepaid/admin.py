from django.contrib import admin

from apps.prepaid.models import (
    AccountBalance,
    AccountCharge,
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    CustomerInteractionPrepaid,
    MinutesReport,
    PaymentSummary,
    SubscriptionInfo,
    PrepaidSubscription
)

admin.site.register(AccountBalance)
admin.site.register(AccountCharge)
admin.site.register(InterestedToSell)
admin.site.register(InterestedToBuy)
admin.site.register(GeneralCall)
admin.site.register(CustomerInteractionPrepaid)
admin.site.register(MinutesReport)
admin.site.register(PaymentSummary)
admin.site.register(SubscriptionInfo)
admin.site.register(PrepaidSubscription)