from django.core.management.base import BaseCommand
from activityperiodsapp.models import User,ActivityPeriod

class Command(BaseCommand):
    help = 'Displays user activites'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stdout.write('processing...')

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Primary Id to get specific user activty')

    def handle(self, *args, **kwargs):
        activity_periods = ActivityPeriod.objects.filter(activity=kwargs.get('id',None)).values()
        self.stdout.write('success')
        self.stdout.write('{}'.format(activity_periods))
