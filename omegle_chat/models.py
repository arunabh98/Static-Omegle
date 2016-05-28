from django.db import models


# Create your models here.

class User(models.Model):

    MAC = models.CharField(max_length=20, primary_key=True)
    points = models.IntegerField()
    MMR = models.IntegerField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    HOSTELS = (('Hostel 1', 'Hostel 1'), ('Hostel 2', 'Hostel 2'),
               ('Hostel 3', 'Hostel 3'), ('Hostel 4', 'Hostel 4'),
               ('Hostel 5', 'Hostel 5'), ('Hostel 6', 'Hostel 6'),
               ('Hostel 7', 'Hostel 7'), ('Hostel 8', 'Hostel 8'),
               ('Hostel 9', 'Hostel 9'), ('Hostel 10', 'Hostel 10'),
               ('Hostel 11', 'Hostel 11'), ('Hostel 12', 'Hostel 12'),
               ('Hostel 13', 'Hostel 13'), ('Hostel 14', 'Hostel 14'),
               ('Hostel 15', 'Hostel 15'), ('Tansa', 'Tansa'), ('QIP', 'QIP'))
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hostel = models.CharField(max_length=10, choices=HOSTELS)

    def __str__(self):
        return self.MAC


class Chat(models.Model):

    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_who_sent_the_message')
    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_who_received_the_message')
    chat_message = models.TextField()
    status = models.TextField()
