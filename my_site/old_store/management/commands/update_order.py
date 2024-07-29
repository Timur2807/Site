from django.core.management import BaseCommand
from old_store.models import Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not object:
            self.stdout.write("no order found")
            return
        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added products {order.products.all()} to order {order}"
                )
            )
