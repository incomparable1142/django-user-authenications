from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='image/image', null=True, blank=True, help_text="Upload only .png, .jpg & .jpeg image extension.")
    video = models.FileField(upload_to='image/video', null=True, blank=True, help_text="Upload only mp4, etc..")
    current_user = models.IntegerField()

    class Meta:
        db_table = 'shool'
        verbose_name_plural = 'School'
        managed = True

    def __str__(self):
        return self.name


class Coaching(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='image/image', null=True, blank=True, help_text="Upload only .png, .jpg & .jpeg image extension.")
    video = models.FileField(upload_to='image/video', null=True, blank=True, help_text="Upload only mp4, etc..")
    current_user = models.IntegerField()

    class Meta:
        db_table = 'coaching'
        verbose_name_plural = 'Coaching'
        managed = True

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    photo = models.FileField(upload_to='image/image', null=True, blank=True, help_text="Upload only .png, .jpg & .jpeg image extension.")
    video = models.FileField(upload_to='image/video', null=True, blank=True, help_text="Upload only mp4, etc..")
    current_user = models.IntegerField()

    class Meta:
        db_table = 'tutor'
        verbose_name_plural = 'Tutor'
        managed = True

    def __str__(self):
        return self.name
