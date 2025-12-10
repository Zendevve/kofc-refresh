"""
Script to add historical donation data for testing the forecast chart.
Run with: py add_test_donations.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from capstone_project.models import Donation, User
from datetime import date, timedelta
from decimal import Decimal
import random

# Get an admin user to attribute the donations to
user = User.objects.filter(role='admin').first()
if not user:
    user = User.objects.first()

print(f'Using user: {user.username}')

# Create donations for the past 8 months (so we have enough history for forecast)
# Format: (months_ago, base_amount)
historical_data = [
    (7, 5200),
    (6, 6100),
    (5, 5800),
    (4, 7200),
    (3, 6900),
    (2, 7800),
    (1, 8100),
]

created = 0
for months_ago, base_amount in historical_data:
    donation_date = date.today() - timedelta(days=30*months_ago)
    # Add some randomness
    amount = base_amount + random.randint(-300, 500)

    Donation.objects.create(
        first_name=user.first_name or 'Test',
        last_name=user.last_name or 'Donor',
        email=user.email or 'test@example.com',
        amount=Decimal(str(amount)),
        donation_date=donation_date,
        status='completed',
        submitted_by=user,
        payment_method='gcash',
    )
    created += 1
    print(f'Created: {donation_date.strftime("%Y-%m")} - PHP {amount:,.2f}')

print(f'\n✓ Total created: {created} donations')
print('Historical donations added successfully!')
print('Refresh the analytics page to see the forecast chart.')
