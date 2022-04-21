from django.db import models

# Create your models here.


class Schedule(models.Model):
    """
    Model for the schedule of the F1 season.
    """
    season = models.CharField(max_length=10)
    round = models.CharField(max_length=10)
    circuit = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    url = models.URLField()


    def __str__(self):
        return f'{self.season} {self.round}'


class ChampionShipConstructors(models.Model):
    """
    Model for the constructors of the F1 season.
    """
    season = models.CharField(max_length=10)
    constructor = models.CharField(max_length=100)
    points = models.IntegerField()
    wins = models.IntegerField()
    image = models.URLField()
    def __str__(self):
        return f'{self.season} {self.constructor}'


class ChampionShipDrivers(models.Model):
    """
    Model for the drivers of the F1 season.
    """
    season = models.CharField(max_length=10)
    driver = models.CharField(max_length=100)
    points = models.IntegerField()
    wins = models.IntegerField()
    constructor = models.ForeignKey(ChampionShipConstructors,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.season} {self.driver}'

class LeaderBoard(models.Model):
    """
    Model for the leaderboard of the F1 season.
    """
    race = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    position = models.CharField(max_length=10)
    driver = models.ForeignKey(ChampionShipDrivers,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.season} {self.round} {self.position}'
