from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField(null=True)
    descricao = models.TextField(null=True)
    order = models.PositiveIntegerField(("order"), editable=False, db_index=True, null=True)
    slug = models.SlugField(unique=True)


    class Meta(OrderedModel.Meta):
        pass


    def __str__(self):
        return self.titulo


    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})
