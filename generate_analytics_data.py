"""
Comprehensive Script to add historical data for analytics testing.
This creates donations, events, attendance records, and recruitments
to provide meaningful data for the analytics dashboard.

Run with: py generate_analytics_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from capstone_project.models import Donation, User, Event, EventAttendance, Recruitment, Council
from datetime import date, timedelta
from django.utils import timezone
from decimal import Decimal
import random

print("=" * 60)
print("  ANALYTICS DATA GENERATOR")
print("=" * 60)

# Get users and councils
admin = User.objects.filter(role='admin').first()
members = list(User.objects.filter(role__in=['member', 'officer']).exclude(id=admin.id if admin else 0)[:20])
councils = list(Council.objects.all())

if not admin:
    admin = User.objects.first()

print(f"\nUsing admin: {admin.username}")
print(f"Found {len(members)} members")
print(f"Found {len(councils)} councils")

# ============================================================
# DONATIONS - 12 months of donation history
# ============================================================
print("\n[1/4] Creating Donation History...")

donation_count = 0
base_amounts = [4500, 5200, 5800, 6300, 6700, 7100, 7500, 7800, 8200, 8600, 9000, 9400]

for months_ago in range(12, 0, -1):
    donation_date = date.today() - timedelta(days=30 * months_ago)

    # Create 3-5 donations per month
    num_donations = random.randint(3, 5)
    month_base = base_amounts[12 - months_ago] if 12 - months_ago < len(base_amounts) else 8000

    for i in range(num_donations):
        amount = month_base // num_donations + random.randint(-200, 300)
        donor = random.choice(members) if members else admin

        Donation.objects.create(
            first_name=donor.first_name or 'Donor',
            last_name=donor.last_name or f'#{donation_count + 1}',
            email=donor.email or 'donor@example.com',
            amount=Decimal(str(amount)),
            donation_date=donation_date + timedelta(days=random.randint(0, 28)),
            status='completed',
            submitted_by=donor,
            payment_method=random.choice(['gcash', 'gcash', 'manual']),
            council=donor.council if donor.council else (councils[0] if councils else None),
        )
        donation_count += 1

print(f"   ✓ Created {donation_count} donations over 12 months")

# ============================================================
# EVENTS - Create past events
# ============================================================
print("\n[2/4] Creating Past Events...")

event_templates = [
    ("Monthly Council Meeting", "Council Meeting", "Regular monthly meeting"),
    ("Faith Formation Night", "Service Program", "Fellowship and faith sharing"),
    ("Community Outreach", "Service Program", "Community service activity"),
    ("Exemplification Ceremony", "Exemplification", "Degree exemplification ceremony"),
    ("Family Day", "Service Program", "Family-oriented activities"),
    ("Christmas Party", "Service Program", "Annual Christmas celebration"),
    ("Easter Program", "Service Program", "Easter celebration"),
    ("Youth Activities", "Service Program", "Youth engagement program"),
]

event_count = 0
for months_ago in range(8, 0, -1):
    # 1-3 events per month
    num_events = random.randint(1, 3)
    for i in range(num_events):
        template = random.choice(event_templates)
        event_date = date.today() - timedelta(days=30 * months_ago + random.randint(0, 25))

        council = random.choice(councils) if councils else None

        event = Event.objects.create(
            name=f"{template[0]} - {event_date.strftime('%B %Y')}",
            description=template[2],
            category=template[1],
            subcategory=random.choice(['Faith', 'Family', 'Community', 'Life']) if template[1] == 'Service Program' else None,
            council=council,
            is_global=random.choice([True, False, False]),
            street="Church Street",
            barangay="San Jose",
            city=council.location_city if council and council.location_city else "Batangas City",
            province=council.location_province if council and council.location_province else "Batangas",
            date_from=event_date,
            date_until=event_date,
            status='approved',
            created_by=admin,
            approved_by=admin,
        )
        event_count += 1

print(f"   ✓ Created {event_count} past events")

# ============================================================
# EVENT ATTENDANCE - Add attendance records
# ============================================================
print("\n[3/4] Creating Attendance Records...")

attendance_count = 0
past_events = Event.objects.filter(date_from__lt=date.today(), status='approved')

for event in past_events:
    # Random 50-90% attendance rate
    if members:
        attendees = random.sample(members, k=min(len(members), random.randint(max(1, len(members)//2), len(members))))

        for member in attendees:
            try:
                EventAttendance.objects.get_or_create(
                    event=event,
                    member=member,
                    defaults={
                        'is_present': True,
                        'recorded_by': admin,
                    }
                )
                attendance_count += 1
            except:
                pass

print(f"   ✓ Created {attendance_count} attendance records")

# ============================================================
# RECRUITMENTS - Create recruitment history
# ============================================================
print("\n[4/4] Creating Recruitment Records...")

recruitment_count = 0
# Split members into recruiters and recruits
if len(members) >= 4:
    recruiters = members[:len(members)//2]
    recruits = members[len(members)//2:]

    for months_ago in range(10, 0, -1):
        # 0-2 recruitments per month
        num_recruitments = random.randint(0, 2)
        for _ in range(num_recruitments):
            if recruiters and recruits:
                recruiter = random.choice(recruiters)
                recruited = random.choice(recruits)

                # Avoid self-recruitment and duplicates
                if recruiter.id != recruited.id:
                    try:
                        Recruitment.objects.get_or_create(
                            recruiter=recruiter,
                            recruited=recruited,
                            defaults={
                                'date_recruited': date.today() - timedelta(days=30 * months_ago + random.randint(0, 28)),
                                'is_manual': False,
                                'added_by': admin,
                            }
                        )
                        recruitment_count += 1
                        recruits.remove(recruited)  # Avoid duplicate
                    except:
                        pass

print(f"   ✓ Created {recruitment_count} recruitment records")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("  SUMMARY")
print("=" * 60)
print(f"  Donations:    {donation_count}")
print(f"  Events:       {event_count}")
print(f"  Attendance:   {attendance_count}")
print(f"  Recruitments: {recruitment_count}")
print("=" * 60)
print("\n✓ Historical data generation complete!")
print("  Refresh the analytics page to see the updated charts.")
