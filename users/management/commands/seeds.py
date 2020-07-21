from django.core.management import BaseCommand
import random
from users.models import CustomUser
from products.models import Products
import seeder


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

        for user in CustomUser.objects.all():
            user.set_password(user.password)
            user.save()


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Populate users and profiles
    seeder.seed_all()
