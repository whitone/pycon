from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class VoteRange(TimeStampedModel):

    name = models.CharField(max_length=100, unique=True)
    first = models.IntegerField(_('first'))
    last = models.IntegerField(_('last'))
    step = models.PositiveIntegerField(_('step'), validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.name} goes from {self.first} to {self.last} with step {self.step}'


class Vote(TimeStampedModel):
    range = models.ForeignKey(
        VoteRange,
        verbose_name=_('range'),
        on_delete=models.PROTECT
    )

    value = models.FloatField(_('vote'))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
    )

    submission = models.ForeignKey(
        'submissions.Submission',
        on_delete=models.CASCADE,
        verbose_name=_('submission'),
        related_name='votes'
    )

    def __str__(self):
        return f'{self.user} voted {self.value} for Submission {self.submission}'

