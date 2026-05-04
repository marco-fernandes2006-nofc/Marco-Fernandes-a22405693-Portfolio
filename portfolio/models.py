from django.db import models


# ======================
# LICENCIATURA
# ======================
class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    duracao_anos = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


# ======================
# UNIDADE CURRICULAR
# ======================
class UnidadeCurricular(models.Model):
    SEMESTRE_CHOICES = [
    ('S1', '1º Semestre'),
    ('S2', '2º Semestre'),
    ('A', 'Anual'),
    ('S', 'Semestral'),
    ]

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ano_curricular = models.PositiveIntegerField()
    semestre = models.CharField(max_length=2, choices=SEMESTRE_CHOICES)

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# ======================
# TECNOLOGIA
# ======================
class Tecnologia(models.Model):
    TIPO_CHOICES = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('ferramenta', 'Ferramenta'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='portfolio/tecnologias', null=True, blank=True)
    website_oficial = models.URLField(blank=True)
    portfolio = models.BooleanField()

    def __str__(self):
        return self.nome


# ======================
# PROJETO
# ======================
class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    data_realizacao = models.DateField()

    tecnologias = models.ManyToManyField(Tecnologia)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


# ======================
# TFC
# ======================
class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    rating = models.PositiveIntegerField()

    autores = models.CharField(max_length=200)
    orientadores = models.CharField(max_length=200)

    tecnologias = models.ManyToManyField(Tecnologia)

    documento = models.FileField(upload_to='tfc/')

    def __str__(self):
        return self.titulo


# ======================
# COMPETÊNCIA
# ======================
class Competencia(models.Model):
    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermédio'),
        ('avancado', 'Avançado'),
    ]

    TIPO_CHOICES = [
        ('tecnica', 'Técnica'),
        ('soft', 'Soft Skill'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return self.nome


# ======================
# FORMAÇÃO
# ======================
class Formacao(models.Model):
    TIPO_CHOICES = [
        ('curso', 'Curso'),
        ('workshop', 'Workshop'),
        ('certificacao', 'Certificação'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo


# ======================
# MAKING OF
# ======================
class MakingOf(models.Model):
    descricao = models.TextField()
    erros = models.TextField()
    justificacao_opcoes = models.TextField()
    imagem = models.ImageField(upload_to='portfolio/makingof', blank=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    portfolio = models.BooleanField()

    def __str__(self):
        return f"MakingOf - {self.projeto.nome}"


# ======================
# OPEN SOURCE
# ======================
class ContribuicaoOpenSource(models.Model):
    nome = models.CharField(max_length=150)
    nome_projeto = models.CharField(max_length=150, blank=True)
    descricao_projeto = models.TextField()

    repositorio = models.URLField(blank=True)
    website_oficial = models.URLField(blank=True)

    descricao_contribuicao = models.TextField()

    def __str__(self):
        return self.nome