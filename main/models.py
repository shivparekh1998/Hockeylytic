from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone


class Dummy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.firstName} {self.lastName} (unlinked)'


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    wins = models.IntegerField(default=0, blank=True)
    losses = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


# Team roster
class PlayerList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    join_date = models.DateTimeField(default=timezone.now, null=True)
    leave_date = models.DateTimeField(blank=True, null=True)
    isDummy = models.BooleanField(default=True)
    dummy = models.ForeignKey(Dummy, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.team} | {self.player} | {self.dummy}'


class Match(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    AWAY = 'AW'
    HOME = 'HO'
    USER_TYPE_CHOICES = [
        (AWAY, 'Away'),
        (HOME, 'Home'),
    ]
    yourTeam = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=AWAY,
    )
    homeTeam = models.ForeignKey(Team, null=True, related_name='home_team', on_delete=models.SET_NULL)
    awayTeam = models.ForeignKey(Team, null=True, related_name='away_team', on_delete=models.SET_NULL)
    homeGoals = models.IntegerField(default=0)
    homePoints = models.IntegerField(default=0)
    awayGoals = models.IntegerField(default=0)
    awayPoints = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.homeTeam} vs. {self.awayTeam}'


class Stats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isDummy = models.BooleanField(default=True)
    dummy = models.ForeignKey(Dummy, on_delete=models.CASCADE, null=True, blank=True)

    FORWARD = 'FWD'
    DEFENSE = 'DEF'
    CENTER = 'CNT'
    GOALIE = 'GOL'
    POSITION_CHOICES = [
        (FORWARD, 'Forward'),
        (DEFENSE, 'Defense'),
        (CENTER, 'Center'),
        (GOALIE, 'Goalie'),
    ]
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        default=FORWARD,
    )

    goals = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    fow = models.IntegerField(blank=True, null=True)
    fol = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    ppp = models.IntegerField(blank=True, null=True)
    shg = models.IntegerField(blank=True, null=True)
    shp = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    # Dont let player enter foPercent and shootingPercent
    foPercent = models.FloatField(blank=True, null=True)
    shootingPercent = models.FloatField(blank=True, null=True)
    toi = models.IntegerField(blank=True, null=True)
    sog = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.match} | {self.player} | {self.dummy}'
