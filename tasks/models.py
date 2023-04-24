from django.db import models

class Tile(models.Model):
    launch_date = models.DateField()
    STATUS_CHOICES = (
        ('LIVE', 'Live'),
        ('PENDING', 'Pending'),
        ('ARCHIVED', 'Archived'),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Tile {self.id} ({self.get_status_display()})'
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=20)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


