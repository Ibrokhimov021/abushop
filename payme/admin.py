from django.contrib import admin

from .models import MerchatTransactionsModel, Order

admin.site.register(Order)
admin.site.register(MerchatTransactionsModel)