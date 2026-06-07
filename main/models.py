# main/models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class Resume(models.Model):
    file = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    is_current = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Resume - {self.uploaded_at.strftime('%Y-%m-%d')}"
