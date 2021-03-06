from django.db import models
from django.utils import timezone

class HostelAnnouncements(models.Model):
    announcement_title = models.CharField(max_length=30, blank=True, null=True)
    announcement = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    isDeleted = models.BooleanField(default = 0)
    def __str__(self):
        return str(self.announcement_title)

    @property

    def isDelete(self):
        return bool(self.isDeleted())

class MessAnnouncements(models.Model):
    announcement_title = models.CharField(max_length=30, blank=True, null=True)
    announcement = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    isDeleted = models.BooleanField(default = 0)
    def __str__(self):
        return str(self.announcement_title)

    @property
    def isDelete(self):
        return bool(self.isDeleted())

class MedicalAnnouncements(models.Model):
    announcement_title = models.CharField(max_length=30, blank=True, null=True)
    announcement = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)
    isDeleted = models.BooleanField(default = 0)
    def __str__(self):
        return str(self.announcement_title)

    @property
    def isDelete(self):
        return bool(self.isDeleted())

class ImportantContacts(models.Model):
    name = models.CharField(max_length = 30, blank = False)
    mobile = models.CharField(max_length = 13, blank = False)
    email = models.EmailField(max_length = 70, blank = False)
    isDeleted = models.BooleanField(default = 0)

    def __str__(self):
        return str(self.name)

    @property
    def isDelete(self):
        return bool(self.isDeleted())


class Messages(models.Model):
    message=models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    student=models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    isDeleted = models.BooleanField(default = 0)
    def __str__(self):
        return str(self.message)

    @property
    def isDelete(self):
        return bool(self.isDeleted())
