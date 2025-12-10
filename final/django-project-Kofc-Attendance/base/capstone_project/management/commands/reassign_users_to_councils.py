from django.core.management.base import BaseCommand
from capstone_project.models import User, Council

class Command(BaseCommand):
    help = 'Reassign users without councils to the first available council'

    def add_arguments(self, parser):
        parser.add_argument(
            '--council-id',
            type=int,
            help='Specific council ID to assign users to',
        )
        parser.add_argument(
            '--role',
            type=str,
            help='Only reassign users with this role (member, officer)',
        )

    def handle(self, *args, **options):
        # Get users without councils
        users_without_council = User.objects.filter(council__isnull=True, is_archived=False)
        
        if options['role']:
            users_without_council = users_without_council.filter(role=options['role'])
        
        if not users_without_council.exists():
            self.stdout.write(self.style.SUCCESS('No users without councils found.'))
            return
        
        # Get target council
        if options['council_id']:
            try:
                target_council = Council.objects.get(id=options['council_id'])
            except Council.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Council with ID {options["council_id"]} not found.'))
                return
        else:
            # Use the first available council
            target_council = Council.objects.first()
            if not target_council:
                self.stdout.write(self.style.ERROR('No councils available to assign users to.'))
                return
        
        # Reassign users
        count = 0
        for user in users_without_council:
            user.council = target_council
            user.save()
            count += 1
            self.stdout.write(f'  Reassigned {user.username} ({user.get_full_name()}) to {target_council.name}')
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully reassigned {count} user(s) to {target_council.name}'))
