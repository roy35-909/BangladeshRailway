from django.db import models


class Train(models.Model):
    train_name = models.CharField(max_length=255)
    def __str__(self):
        return self.train_name

class Desgination(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Schedule(models.Model):
    
    Train = models.ForeignKey(Train, on_delete=models.CASCADE)
    frm = models.ForeignKey(Desgination,on_delete=models.CASCADE, related_name='frm')
    to = models.ForeignKey(Desgination, on_delete=models.CASCADE, related_name='to')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.Train.train_name







