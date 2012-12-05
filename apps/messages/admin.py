from django.contrib import admin
from models import MailingAddress, Order, PartnershipOffer, EntryInSchool, Question

admin.site.register(Order,)
admin.site.register(MailingAddress,)
admin.site.register(PartnershipOffer,)
admin.site.register(EntryInSchool,)
admin.site.register(Question,)