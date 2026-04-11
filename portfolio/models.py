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
        (1, '1º Semestre'),
        (2, '2º Semestre'),
    ]

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ano_curricular = models.PositiveIntegerField()
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES)

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
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/', null=True, blank=True)
    website_oficial = models.URLField(blank=True)

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
    ano = models.PositiveIntegerField()

    autores = models.CharField(max_length=200)
    orientadores = models.CharField(max_length=200)

    tecnologias = models.ManyToManyField(Tecnologia)

    repositorio_git = models.URLField(blank=True)
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
    descricao = models.TextField()
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

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return f"MakingOf - {self.projeto.nome}"


class RegistoMakingOf(models.Model):
    imagem = models.ImageField(upload_to='makingof/')
    descricao = models.TextField()

    makingof = models.ForeignKey(MakingOf, on_delete=models.CASCADE)

    def __str__(self):
        return f"Registo de {self.makingof.projeto.nome}"


# ======================
# OPEN SOURCE
# ======================
class ContribuicaoOpenSource(models.Model):
    nome = models.CharField(max_length=150)
    descricao_projeto = models.TextField()

    repositorio = models.URLField(blank=True)
    website_oficial = models.URLField(blank=True)

    descricao_contribuicao = models.TextField()

    def __str__(self):
        return self.nome