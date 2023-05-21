from django.db import models
from stdimage.models import StdImageField

#Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de criação!', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
                                                                        #Classe base para herdar dela
    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)}) #variations = cria um thumb com o                                                                                             #tamanho de px 124 por 124
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs): #função para dizer oq será mostrado no signal
    instance.slug= slugify(instance.nome) #coloca o nome no slug ex: Maria Mole fica maria-mole

signals.pre_save.connect(produto_pre_save, sender=Produto) #Antes de salvar, execute a função produto_pre_save, 
                                                            #quando o Produto submeter a um sinal