import pytz
from django.utils import timezone
from django.conf import settings

def now():
    return timezone.make_aware(timezone.datetime.now(), pytz.timezone(settings.TIME_ZONE))
