from django.db import models

# Create your models here.
# === Model 1 : Categoria ===
class Categoria(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="nome"
    )
    class Meta:
       verbose_name = "Categoria"
       verbose_name_plural = "Categorias"


    def __str__(self):
        return self.nome

# === Model 2 : Equipamentos ===
class Equipamento(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome do Equipamento"
    )
    numero_serie = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Número de Série"
    )

    data_aquisicao = models.DateField()

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'equipamentos',
        verbose_name = "Categoria",
    )
    STATUS_CHOICES = [
        ('EM_USO', 'Em uso'),
        ('ESTOQUE', 'Estoque'),
        ('MANUTENCAO', 'Manutenção')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ESTOQUE',
        verbose_name="Status do Equipamento"
    )
   
    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

    
    def __str__(self):

        return f"{self.nome}(S/N: {self.numero_serie})"