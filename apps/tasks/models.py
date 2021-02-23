from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class CategoryTask(BaseModel):
    """Model definition for CategoryProduct."""

    # TODO: Define fields here
    description = models.CharField('Descripcion', max_length=50,unique = True,null = False,blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Categoría de tarea'
        verbose_name_plural = 'Categorías de las Tareas'

    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description


class Tasks(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    title = models.CharField('Nombre de la tarea', max_length=150, unique = True,blank = False,null = False)
    description = models.TextField('Descripción de la tarea',blank = False,null = False)
    completed = models.BooleanField(default=False, blank=True, null=True)
    category_task = models.ForeignKey(CategoryTask, on_delete=models.CASCADE,verbose_name = 'Categoria de Producto', null = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'tareas'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
