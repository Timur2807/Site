"""
Этот модуль за один запрос записывает несколько объектов в БД.

При помощи одной команды sql можно сделать несколько записей в БД.

'Product.objects.bulk_create(products)' вот эта команда.
Product.objects.filter(name__contains="Smartphon",).update(discount=10) эта команда обновляет
записи о продуктах в данном случаи обновили discount.

"""
from django.core.management import BaseCommand
from old_store.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo bulk actions")
        result = Product.objects.filter(
            name__contains="Smartphon",
        ).update(discount=10)

        print(result)
        # info = [
        #     ('Smartphon 1', 199),
        #     ('Smartphon 2', 299),
        #     ('Smartphon 3', 399)
        # ]
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        #
        # result = Product.objects.bulk_create(products)
        # for obj in result:
        #     print(obj)
        self.stdout.write('Done')
