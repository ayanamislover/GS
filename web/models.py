from __future__ import unicode_literals

# Import Django's model module
from django.db import models
from django.db import models, transaction
from django.contrib import admin
from usersinformation.models import PlayerProfile



from django.contrib.auth.hashers import make_password
# Define the User model class
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    # OneToOneField is associated with PlayerProfile
    player_profile = models.OneToOneField(PlayerProfile, on_delete=models.CASCADE, null=True, related_name='user')

    def save(self, *args, **kwargs):
        # First save the User object
        super(User, self).save(*args, **kwargs)
        # Then get or create a PlayerProfile instance
        player_profile, created = PlayerProfile.objects.get_or_create(user=self)
        # If it is a newly created PlayerProfile, set its additional fields
        if created:
            player_profile.nickname = self.username
            player_profile.email = self.email  # Assume that the PlayerProfile model has an email field
            player_profile.save()


    #def set_password(self, raw_password):
    #    self.password = make_password(raw_password)
    #    self.save()



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User, UserAdmin)


