
# Bot de Apostas Esportivas com Valor Esperado (EV+)

Este projeto implementa um sistema completo para análise de apostas esportivas com base em Valor Esperado (EV%) e Score de Confiança, focado nas ligas **NBA, NFL, MLB, NCAAB e NCAAF**.

## 🔍 Funcionalidades

- Coleta de projeções reais de placares (Oddshark, Sportsline)
- Scraping/API de odds reais (The Odds API, API-Sports, Sports Game Odds)
- Cálculo de EV% por tipo de linha (Spread, Total, Moneyline)
- Score de Confiança baseado em estatísticas e contexto (forma, matchup, lesões, sharp money)
- Geração de relatório diário com destaques visuais 🟢 ⚠️ 🔴
- Envio automático via Telegram
- API com rota `/healthz` para deploy em nuvem (Render)

## ⚙️ Como usar

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/ev-bot.git
cd ev-bot
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Crie um arquivo `.env` com suas chaves de API**
```
ODDS_API_KEY=your_odds_api_key
API_SPORTS_KEY=your_apisports_key
SGO_API_KEY=your_sgo_api_key
```

5. **Execute localmente**
```bash
python main.py
```

- Acesse: [http://localhost:10000/healthz](http://localhost:10000/healthz)

6. **Deploy no Render.com**
- Crie um novo Web Service com este repositório.
- Use `python main.py` como comando de start.
- Configure porta `10000` e rota de health check: `/healthz`.

7. **Automatize com UptimeRobot**
- Adicione ping para sua URL `/send-daily` às 11h diárias.

## 📤 Envio via Telegram

- Já configurado para enviar para o Chat ID `896985205` com o bot:
```
Token: 7523685081:AAFIngESWWNZh5IqWD6j46X63I_oArpGNQE
```

## ✅ Exemplo de uso

Rota para disparo manual da análise:
```
GET https://seu-projeto.onrender.com/send-daily
```

## 🧠 Lógicas principais

- `ev_percent()` calcula o valor esperado com base na odd e probabilidade do modelo
- `calcular_score_confiança()` combina 6 fatores com pesos ajustáveis
- `orquestrar_analise()` junta dados, calcula EV e Score, e retorna lista dos jogos do dia

## 📁 Estrutura do Projeto

- `/scrapers`: coleta de dados
- `/calculations`: EV e score
- `/telegram_bot`: envio e formatação
- `/utils`: configuração e logger
- `main.py`: ponto de entrada (com Flask)

## 📌 Requisitos

- Python 3.9+
- Conta gratuita nas APIs:
    - https://the-odds-api.com
    - https://www.api-sports.io
    - https://sportsgameodds.com

## 📬 Contato

Desenvolvido por Harthur com suporte técnico de IA. Para dúvidas ou melhorias, abra um pull request.
