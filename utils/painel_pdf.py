
from fpdf import FPDF
import json
from datetime import datetime

def gerar_relatorio_pdf():
    with open("painel_estatistico.json", "r") as f:
        data = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Relatório Semanal EV+ | Bot de Apostas", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Data: {data['data_geracao']}", ln=True, align="C")
    pdf.ln(10)

    for liga, tipos in data['resumo'].items():
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt=f"Liga: {liga.upper()}", ln=True)
        for tipo, valor in tipos.items():
            pdf.set_font("Arial", size=11)
            pdf.cell(200, 8, txt=f"  - {tipo.upper()}: {valor} alertas", ln=True)

    path = "relatorio_semanal.pdf"
    pdf.output(path)
    return path
