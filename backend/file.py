import csv
from models import Startup, Mention
from datetime import date


async def write_csv(end: date, start: date):
    all_mentions = await Mention.filter(date__lte=end, date__gte=start)
    startups, startup_ids = [], set()
    for mention in all_mentions:
        startup_ids.add(mention.startup_id)
    for id in startup_ids:
        startups.append(await Startup.get(id=id))
    with open("startups.csv", "wt") as fp:
        writer = csv.writer(fp, delimiter=": ")
    writer.writerow(["Стартап", "Кол-во  упоминаний"])
    for startup in startups:
        mentions = list(filter(lambda m: startup.id == m.startup_id, all_mentions))
        writer.writerow([startup.title, len(mentions)])
