from tortoise.models import Model
from tortoise import fields


class Startup(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=300, unique=True)
    description = fields.TextField(null=True)
    country = fields.CharField(max_length=300, null=True)
    link = fields.CharField(max_length=300, null=True)
    img_link = fields.CharField(max_length=300, null=True)
    def __str__(self):
        return self.title

    class Meta:
        table = "startups"


class Mention(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=400)
    link = fields.CharField(max_length=300, unique=True)
    date = fields.DateField()
    startup_id = fields.ForeignKeyField("models.Startup", related_name="links")

    def __str__(self):
        return self.link

    class Meta:
        table = "mentions"
