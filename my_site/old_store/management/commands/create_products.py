"""
Этот модуль создаёт продукты и загружает в БД при помощи класса.
"""
from django.core.management import BaseCommand
from old_store.models import Product


class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **options):
        """Медот определяет логику этой команды."""
        products_names = [
            "book",
            "note",
            "paper",
            ]
        for product_name in products_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Created product {product.name}")
        self.stdout.write("Create products")
        self.stdout.write(self.style.SUCCESS("Products Created"))
