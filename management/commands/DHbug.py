from click import BaseCommand

from api.models import Tag


class Command(BaseCommand):
    """
    暂时用来生成小红点标记
    """

    def handle(self, *args, **options):
        for i in range(10):
            Tag.objects.create(name="index-%s" % i)
