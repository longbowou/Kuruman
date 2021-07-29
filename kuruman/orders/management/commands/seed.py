from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from faker.providers import company, address, date_time

from kuruman.orders.models import Order


class Command(BaseCommand):
    help = 'Seed data'

    def add_arguments(self, parser):
        pass

    @transaction.atomic
    def handle(self, *args, **options):
        fake = Faker()
        fake.add_provider(company)
        fake.add_provider(address)
        fake.add_provider(date_time)

        orders = []
        for _ in range(100000):
            order = Order(**{
                "country": fake.country(),
                "company": fake.company(),
                "status": fake.random_element((Order.STATUS_INFO, Order.STATUS_DELIVERED,
                                               Order.STATUS_DANGER, Order.STATUS_PENDING,
                                               Order.STATUS_CANCELED, Order.STATUS_SUCCESS)),
                "type": fake.random_element((Order.TYPE_ONLINE, Order.TYPE_RETAIL, Order.TYPE_DIRECT)),
                "created_at": fake.date_between(start_date='-30y', end_date='today')
            })
            order.order_id = f'{str(order.id)[-8:]}'
            orders.append(order)
            self.stdout.write(self.style.SUCCESS(f'{order}'))

        Order.objects.bulk_create(orders)
        self.stdout.write(self.style.SUCCESS('Seed complete'))
