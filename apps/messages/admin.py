# coding:utf-8
import xlwt
from datetime import datetime, date

from django.contrib import admin
from django.http import HttpResponse

from models import MailingAddress, Order, PartnershipOffer, EntryInSchool, Question
from apps.products.models import Product

class OrderAdmin(admin.ModelAdmin):
    list_filter = ('state',)
    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Заказы %s', date.today())

        ws.write(0, 0, 'Статус')
        ws.write(0, 1, 'Тип товара')
        ws.write(0, 2, 'Количество')
        ws.write(0, 3, 'Итого')
        ws.write(0, 4, 'Инициалы заказчика')
        ws.write(0, 5, 'Электропочта')
        ws.write(0, 6, 'Город')
        ws.write(0, 7, 'Адрес')
        ws.write(0, 8, 'Код телефона')
        ws.write(0, 9, 'Телефон')

        states = {'new': 'новый', 'in_progress': 'в обработке', 'done': 'обработан'}

        for idx, order in enumerate(queryset):
            ws.write(idx+1, 0, states[order.state])
            ws.write(idx+1, 1, order.product.title)
            ws.write(idx+1, 2, order.product_quantity)
            ws.write(idx+1, 3, order.product_quantity*order.product.price)
            ws.write(idx+1, 4, order.initials)
            ws.write(idx+1, 5, order.email)
            ws.write(idx+1, 6, order.city)
            ws.write(idx+1, 7, order.address)
            ws.write(idx+1, 8, order.phone_code)
            ws.write(idx+1, 9, order.phone)

        filename = 'заказы_%s.xls' %(date.today())
        response = HttpResponse(mimetype="application/vnd.ms-excel")
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        wb.save(response)

        return response

    export_to_excel.short_description = "Экспортировать выбранные заказы в excel"


admin.site.register(Order,OrderAdmin)
admin.site.register(MailingAddress,)
admin.site.register(PartnershipOffer,)
admin.site.register(EntryInSchool,)
admin.site.register(Question,)