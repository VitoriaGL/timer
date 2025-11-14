from django.db import models


class Contador(models.Model):
    """Modelo simples para demonstrar operações assíncronas."""
    nome = models.CharField(max_length=100)
    valor = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}: {self.valor}"

    class Meta:
        verbose_name = "Contador"
        verbose_name_plural = "Contadores"
        ordering = ['-criado_em']

