"""
Этот модуль создаёт заказы через класс который описан ниже.
"""
from typing import Sequence
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from old_store.models import Order, Product


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Create order with products")
        user = User.objects.get(username="Timur")
        products: Sequence[Product] = Product.objects.only('id').all()

        order, created = Order.objects.get_or_create(
            diliveri_address='st. Ermolova h.13',
            promocode='promo4',
            user=user,
            )

        for product in products:
            order.products.add(product)
        self.stdout.write(f'Create order {order}')
