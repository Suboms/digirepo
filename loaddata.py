# import json
# from django.core.management.base import BaseCommand
# from schools.models import Country, State
# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digirepo.settings")


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         with open("/home/dubsy/virtualenvs/djangoproject/digirepo/countries.json") as f:
#             data = json.load(f)
#             for item in data:
#                 country = Country.objects.create(
#                     name=item["name"],
#                     country_code=item["code3"],
#                     capital=item["capital"],
#                 )
#                 for state_data in item["states"]:
#                     state = State(
#                         country=country,
#                         name=state_data["name"],
#                     )
#                     state.save()
