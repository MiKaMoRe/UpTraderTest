from django.db import models
from django.core.exceptions import ValidationError


class Directory(models.Model):
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
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'директория'
        verbose_name_plural = 'директории'
    
    def validate_parent(self):
        if self.parent and self.parent.pk == self.pk:
            raise ValidationError("Directory self parent")
    
    def root_switch(self):
        if self.parent:
            self.is_root = False
        else:
            self.is_root = True
    
    def clean(self):
        self.root_switch()
        self.validate_parent()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
