import datetime
import random
import time

from faker import Faker, factory

fake = Faker()

from users.models import CustomUser
from products.models import Products


def seed_users(num_entries=5):
    """
    Creates num_entries worth a new users
    """
    count = 0
    for _ in range(num_entries):
        email = fake.email()
        u = CustomUser(
            username=email,
            email=email,
            password='password',
            password2='password',
        )
        u.save()

        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Adding new Users, Addresses and Locations: {:.2f}%".format(percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_all(num_entries=100, overwrite=False):
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
    start_time = time.time()
    # run seeds
    seed_users(num_entries=num_entries)
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))
