from django.db import models
class Directory(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    is_root = models.BooleanField(null=False, default=False, verbose_name='корневая?')
    name = models.CharField(
        max_length=255,
        blank=True,
        null=False, 
        verbose_name='имя'
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='родитель',
        on_delete=models.CASCADE,
        related_name='childs',
        null=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'директория'
        verbose_name_plural = 'директории'
