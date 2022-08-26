import csv 
from models import Startup, Mention
from datetime import date

async def write_csv(end: date, start: date):
    startups = await Startup.filter(date__lte=end, date__gte=start)
    with open("startups.csv", "wt") as fp:
      writer = csv.writer(fp, delimiter=": ")
      writer.writerow(["Стартап", "Кол-во  упоминаний"])
      for startup in startups:
        mentions = await Mention.filter(startup_id=startup.id)
        writer.writerow([startup.title, len(mentions)])
   
    