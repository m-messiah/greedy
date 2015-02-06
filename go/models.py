from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import force_text, pgettext_lazy


class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    legend = models.TextField(verbose_name=_('legend'))
    # Change it to FK(user)
    author = models.CharField(max_length=100, verbose_name=_('author'))
    pretask = models.TextField(verbose_name=_('pretask'))
    tools = models.TextField(
        default="\n".join(map(force_text, (
            _("Automobile"), _("Internet device"), _("Flashlight")
        ))),
        verbose_name=_('tools'))
    start = models.DateTimeField(default=timezone.datetime(2015, 1, 1, 22, 0),
                                 verbose_name=_('start'))
    end = models.DateTimeField(default=timezone.datetime(2015, 1, 2, 7, 0),
                               verbose_name=_('end'))

    def __str__(self):
        return str(self.name)

    def active(self):
        return self.end > timezone.now()

    active.boolean = True
    active.short_description = pgettext_lazy('model method', 'active?')

    verbose_name = _('game')
    verbose_name_plural = _('games')


class Task(models.Model):
    game = models.ForeignKey(Game, verbose_name=_('game'))
    num = models.SmallIntegerField(verbose_name=_('num'))
    desc = models.TextField(verbose_name=_('text'))
    hint1 = models.TextField(default="-", verbose_name=_('hint1'))
    hint2 = models.TextField(default="-", verbose_name=_('hint2'))
    is_bonus = models.BooleanField(default=False, verbose_name=_('is_bonus'))

    def __str__(self):
        return "%s: %s" % (self.num,
                           (self.desc[:10] + "...") if 10 < len(self.desc)
                           else self.desc
        )
    verbose_name = _('task')
    verbose_name_plural = _('tasks')


class Code(models.Model):
    task = models.ForeignKey(Task, verbose_name=_('task'))
    code = models.CharField(max_length=100, verbose_name=_('code'))
    weight = models.SmallIntegerField(verbose_name=_('weight'))
    is_posted = models.BooleanField(default=False, verbose_name=_('posted'))
    post_time = models.DateTimeField(auto_now=True, blank=False,
                                     verbose_name=_('post_time'))

    def __str__(self):
        return "%s (%s)" % (self.code, self.weight)

    verbose_name = _('code')
    verbose_name_plural = _('codes')