Este projeto consiste em construir um **pipeline ETL completo** que coleta dados climáticos reais de cidades brasileiras via API, transforma e limpa os dados com Python/Pandas, e os armazena em um banco SQLite local com geração de relatórios automáticos.

O projeto simula um cenário real de engenharia de dados, com código organizado, testes e agendamento automatizado.

---

## Objetivo

Praticar e consolidar as três camadas de um pipeline de dados profissional: **Extract → Transform → Load**, usando ferramentas reais do mercado.

---

## Stack tecnológica

| Camada | Ferramenta | Para que serve |
| --- | --- | --- |
| Extract | `requests` | Consumir a API Open-Meteo |
| Extract | `json` | Salvar dados brutos |
| Extract | `schedule` | Agendar execução diária |
| Transform | `pandas` | Limpeza e transformação |
| Transform | `pytest` | Testes unitários |
| Load | `sqlite3` | Banco de dados local |
| Load | `matplotlib` | Gráficos e visualizações |
| Geral | `logging` | Registro de erros e status |

---

## Arquitetura do pipeline

```
API Open-Meteo
      ↓
  Extract (requests)
      ↓
  Raw Layer (JSON)
      ↓
  Transform (pandas)
      ↓
  Clean Layer
      ↓
  Load (sqlite3)
      ↓
  Relatório (matplotlib)
```

---

## Estrutura de pastas sugerida

```
etl-clima/
├── extract/
│   ├── fetch_data.py
│   └── scheduler.py
├── transform/
│   ├── clean.py
│   └── enrich.py
├── load/
│   ├── database.py
│   └── report.py
├── tests/
│   └── test_transform.py
├── data/
│   ├── raw/
│   └── processed/
├── reports/
├── main.py
├── requirements.txt
└── README.md
```

---

## API: Open-Meteo (gratuita, sem cadastro)

- Documentação: https://open-meteo.com/en/docs
- Endpoint: `https://api.open-meteo.com/v1/forecast`

```python
import requests

params = {
    'latitude': -8.05,
    'longitude': -34.9,
    'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum',
    'timezone': 'America/Recife',
    'past_days': 7
}
response = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
data = response.json()
```

---

## Sites de estudo por módulo

### Python geral

- https://docs.python.org/3/tutorial/
- https://realpython.com

### requests (HTTP)

- https://docs.python-requests.org/en/latest/
- https://realpython.com/python-requests/

### Pandas

- https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- https://www.kaggle.com/learn/pandas
- https://realpython.com/pandas-dataframe/

### SQLite

- https://docs.python.org/3/library/sqlite3.html
- https://realpython.com/python-sqlite-sqlalchemy/

### Matplotlib

- https://matplotlib.org/stable/tutorials/
- https://realpython.com/python-matplotlib-guide/

### pytest

- https://docs.pytest.org/en/stable/getting-started.html
- https://realpython.com/pytest-python-testing/

### Agendamento (schedule)

- https://schedule.readthedocs.io/en/stable/

### ETL / Engenharia de Dados

- https://www.databricks.com/glossary/etl
- https://www.alura.com.br/artigos/engenharia-de-dados
- https://mode.com/sql-tutorial/

---

## Metodologia: Scrum

O projeto é dividido em **4 sprints de 1 semana**. Pontuação por story points:

| Pontos | Complexidade |
| --- | --- |
| 1 | Muito simples (leitura/config) |
| 2 | Simples (script direto) |
| 3 | Médio (lógica + tratamento) |
| 5 | Complexo (integração de partes) |
| 8 | Muito complexo (arquitetura) |

---

## Definition of Done

- Código funciona sem erros
- Tem comentários explicando o que faz
- Está commitado no Git
- Testado manualmente ou com pytest
- Task marcada como Done no board

---

> Dica: Commite no GitHub desde o início. Isso vai compor seu portfólio!
> 

[📋 Backlog &amp; Sprints](https://www.notion.so/c3d8ed2e226f493796de8f266e7d11cb?pvs=21)