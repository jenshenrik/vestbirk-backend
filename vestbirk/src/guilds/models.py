from django.db import models

# Create your models here.
class ContactPerson(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(null=True, blank=True, max_length=12)
    Email = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.FirstName + self.LastName


class Guild(models.Model):
    title = models.CharField(max_length=200)
    short_text = models.TextField(max_length=500)
    text = models.TextField()

    homepage_url = models.CharField(max_length=500, blank=True)
    facebook_url = models.CharField(max_length=500, blank=True)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE, null=True)

    def as_dict(self):
        guild = {
            "id": self.id,
            "title": self.title,
            "short_text": self.short_text,
            "text": self.text
        }
        return guild

    def __str__(self):
        return self.title


