from mongoengine import Document, EmbeddedDocument, StringField, DateTimeField, BooleanField
from .services import now

class TimeStamp(Document):
    created_at = DateTimeField(default=now)
    deleted_at = DateTimeField(null=True, blank=True)
    is_deleted = BooleanField(default=False)

    meta = {
        'abstract' : True
    }

    @classmethod
    def get_active_objects(cls, **kwargs):
        query = cls.objects.filter(is_deleted=False)
        if kwargs:
            query = query.filter(**kwargs)
        return query
    
    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        return str(self.id)
