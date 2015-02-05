from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=100)
    legend = models.TextField()
    author = models.CharField(max_length=100)  # Change it to FK(user)
    prikvel = models.TextField()
    start = models.DateTimeField(default=timezone.datetime(2015, 1, 1, 22, 0))
    end = models.DateTimeField(default=timezone.datetime(2015, 1, 2, 7, 0))

    def __str__(self):
        return str(self.name)

    def active(self):
        return self.end > timezone.now()

    active.boolean = True


class Task(models.Model):
    game = models.ForeignKey(Game)
    num = models.SmallIntegerField()
    desc = models.TextField()
    hint1 = models.TextField(default="-")
    hint2 = models.TextField(default="-")

    def __str__(self):
        return "%s: %s" % (self.num,
                           (self.desc[:10] + "...") if 10 < len(self.desc)
                           else self.desc
        )


class Code(models.Model):
    task = models.ForeignKey(Task)
    code = models.CharField(max_length=100)
    weight = models.SmallIntegerField()
    is_posted = models.BooleanField(default=False)
    post_time = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return "%s (%s)" % (self.code, self.weight)