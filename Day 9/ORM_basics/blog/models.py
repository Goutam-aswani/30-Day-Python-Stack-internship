from django.db import models
# import uuid
class BlogPost(models.Model):
    # id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    title = models.CharField(max_length=100)
    content =  models.TextField()