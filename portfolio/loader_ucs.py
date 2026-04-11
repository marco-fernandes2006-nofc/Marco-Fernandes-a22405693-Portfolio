import os
import sys
import django
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import UnidadeCurricular, Licenciatura

MAIN_JSON = os.path.join(BASE_DIR, "portfolio", "data", "ULHT260-PT.json")
UCS_FOLDER = os.path.join(BASE_DIR, "portfolio", "data", "ucs")

with open(MAIN_JSON, encoding="utf-8") as f:
    data = json.load(f)

ucs = data.get("courseFlatPlan", [])

licenciatura, _ = Licenciatura.objects.get_or_create(
    nome="Engenharia Informática",
    defaults={
        "sigla": "LEI",
        "descricao": "",
        "duracao_anos": 3
    }
)

for uc in ucs:

    nome = uc.get("curricularUnitName", "")
    ano = uc.get("curricularYear", 0)
    semestre = uc.get("semesterCode", "S")

    code = uc.get("curricularIUnitReadableCode", "")
    detalhe_path = os.path.join(UCS_FOLDER, f"{code}-PT.json")

    descricao = ""

    if os.path.exists(detalhe_path):
        with open(detalhe_path, encoding="utf-8") as f:
            detalhe = json.load(f)
            descricao = detalhe.get("objectives", "")

    uc_obj, created = UnidadeCurricular.objects.update_or_create(
        nome=nome,
        defaults={
            "descricao": descricao.strip(),
            "ano_curricular": ano,
            "semestre": semestre,
            "licenciatura": licenciatura
        }
    )

    print(f"{'Criada' if created else 'Atualizada'}: {nome}")

print("Importação de UCs concluída.")