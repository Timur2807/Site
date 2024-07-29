from django.contrib.auth.models import User
from django.core.management import BaseCommand
from old_store.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo select fields")
        users_info = User.objects.values_list('username', flat=True) # тут получается список
        print(list(users_info))
        for user_info in users_info:
            print(user_info)
        # products_value = Product.objects.values('pk', 'name') # тут получается словарь
        # for p_values in products_value:
        #     print(p_values)
        self.stdout.write('Done')
