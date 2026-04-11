import os
import sys
import django
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import TFC, Tecnologia

# caminho do JSON
JSON_FILE = os.path.join(BASE_DIR, "portfolio", "data", "tfc.json")

# abrir ficheiro
with open(JSON_FILE, encoding="utf-8") as f:
    data = json.load(f)

for item in data:

    titulo = item.get("Título", "Sem título")
    descricao = item.get("Resumo", "")
    autores = item.get("Aluno", "")
    orientadores = item.get("Orientador", "")
    documento = item.get("PDF", "")

    # garantir que rating é inteiro válido
    rating = item.get("Rating")
    try:
        rating = int(rating)
    except (TypeError, ValueError):
        rating = 0

    # criar ou atualizar TFC
    tfc, created = TFC.objects.update_or_create(
        titulo=titulo,
        defaults={
            "descricao": descricao,
            "rating": rating,
            "autores": autores,
            "orientadores": orientadores,
            "documento": documento
        }
    )

    tecnologias_str = item.get("Tecnologias usadas", "")
    tecnologias_lista = [t.strip() for t in tecnologias_str.split(";") if t.strip()]

    tecnologias_objs = []

    for tech_nome in tecnologias_lista:
        tech, _ = Tecnologia.objects.get_or_create(
            nome=tech_nome,
            defaults={
                "tipo": "linguagem",
                "descricao": ""
            }
        )
        tecnologias_objs.append(tech)

    # associar tecnologias
    tfc.tecnologias.set(tecnologias_objs)

    print(f"{'Criado' if created else 'Atualizado'}: {titulo}")

print("Importação de TFCs concluída.")