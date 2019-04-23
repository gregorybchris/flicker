"""MongoEngine ORM models."""
from mongoengine import (Document, DateTimeField, BooleanField,
                         StringField, FloatField)
from datetime import datetime


class Model(Document):
    """Abstract DB model."""

    meta = {'allow_inheritance': True, 'abstract': True}
    created = DateTimeField()
    enabled = BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Override the save method.

        All models have a `created` timestamp and an `enabled` flag.
        """
        if not self.created:
            self.created = datetime.now()
        if not self.enabled:
            self.enabled = True
        return super(Model, self).save(*args, **kwargs)

    def serialize(self):
        """Serialize the model to a dictionary."""
        raise NotImplementedError()


class Message(Model):
    """Model for a message."""

    text = StringField(max_length=50)

    def serialize(self):
        """Serialize the model to a dictionary."""
        return {
            'id': str(self.id),
            'text': self.text
        }


class LightStat(Model):
    """Model for a light reading."""

    reading = FloatField()
    description = StringField()

    def serialize(self):
        """Serialize the model to a dictionary."""
        return {
            'id': str(self.id),
            'reading': self.reading,
            'description': self.description
        }


class SonicStat(Model):
    """Model for an ultrasonic reading."""

    reading = FloatField()
    description = StringField()

    def serialize(self):
        """Serialize the model to a dictionary."""
        return {
            'id': str(self.id),
            'reading': self.reading,
            'description': self.description
        }
