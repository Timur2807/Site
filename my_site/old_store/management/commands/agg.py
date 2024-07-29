"""
Этот модуль позволяет получать средние значение определенных полей.
Количество продуктов или заказов.
Количество продуктов в каждом заказе.
Все эти действия называются агрегация и аннотация.
"""

from django.core.management import BaseCommand
from django.db.models import Avg, Max, Min, Count, Sum

from old_store.models import Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo aggregate")
        # result = Product.objects.filter(
        #     name__contains="Smartphon",
        # ).aggregate(
        #     Avg("price"),
        #     Max("price"),
        #     min_price=Min("price"),
        #     count=Count("id"),
        # )
        # print(result)

        orders = Order.objects.annotate(
            total=Sum("products__price", default=0),
            products_count=Count("products"),
        )
        for order in orders:
            print(
                f"Order №{order.id}"
                f"with {order.products_count}"
                f"products_worth ${order.total}"
            )


        self.stdout.write('Done')
