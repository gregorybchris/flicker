from mongoengine import (Document, DateTimeField, BooleanField,
                         StringField, FloatField)
from datetime import datetime


class Model(Document):
    meta = {'allow_inheritance': True, 'abstract': True}
    created = DateTimeField()
    enabled = BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        if not self.enabled:
            self.enabled = True
        return super(Model, self).save(*args, **kwargs)

    def serialize(self):
        raise NotImplementedError()


class Message(Model):
    text = StringField(max_length=50)

    def serialize(self):
        return {
            'id': str(self.id),
            'text': self.text
        }


class LightStat(Model):
    reading = FloatField()
    description = StringField()

    def serialize(self):
        return {
            'id': str(self.id),
            'reading': self.reading,
            'description': self.description
        }
