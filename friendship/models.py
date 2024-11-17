from django.conf import settings
from django.db import models


class Friendship(models.Model):
    user1 = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user1')
    user2 = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user2')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user1', 'user2')
        # index_together = (('user1', 'user2'),)
        ordering = ('created_at',)
        db_table = 'friendship'
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendship'
        constraints = [
            models.UniqueConstraint(
                fields=['user1', 'user2'],
                name='unique_friendship_user1_user2_friendship'

            )
        ]
