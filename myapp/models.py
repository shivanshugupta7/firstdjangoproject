from django.db import models
class Employee(models.Model):
    eid = models.PositiveIntegerField(unique=True)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField(unique=True)
    econtact = models.PositiveIntegerField(null=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to="users")

    def __str__(self):
        return self.ename




