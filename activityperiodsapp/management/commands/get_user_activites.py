from django.core.management.base import BaseCommand
from activityperiodsapp.models import User,ActivityPeriod

class Command(BaseCommand):
    help = 'Displays user activites'

    def handle(self, *args, **kwargs):
        user_list = User.objects.all().values('real_name','activity_periods')
        self.stdout.write('success')
        self.stdout.write('{}'.format(user_list))
