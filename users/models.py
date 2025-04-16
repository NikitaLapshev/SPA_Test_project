from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length= 30)
    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)


    def __str__(self):
        return f"Users: {self.username}. Data: {self.date}"


    def is_top_level(self):
        return self.parent is None