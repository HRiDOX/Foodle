from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

#Here sender class User and receiver is below this funcion
#kwargs means key words arguments
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print("User Profile is created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #Create the userprofile if does not exist
            UserProfile.objects.create(user=instance)
            print("Profile was not created, I created one")
        print("User is updated")

#Now we will create a trigger this function will execute before it saves the user actually it'll execute before post_save_create_profile_receiver function

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'This user is being saved')
