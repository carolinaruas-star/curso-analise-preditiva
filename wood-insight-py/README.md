# 🪵 SalesInsight PY — Análise de Preços de Madeiras (Wood Prices Dataset) 📊

> 📝 **Nota:** Este documento é um pré-README (primeiro esboço) elaborado para o mini-projeto do curso *Desenvolvimento de IA para Análise Preditiva — Módulo 01, Semana 08*.
> 
> 

---

## 📌 1. Sobre o Projeto

O objetivo deste projeto é analisar, limpar, transformar e visualizar um histórico global de preços e disponibilidade de tipos de madeira (`wood_prices_dataset.csv`). A partir deste conjunto de dados, é construído um fluxo estruturado em funções e encapsulado na classe `AnalisadorDeVendas` para gerar métricas de mercado e exportar relatórios analíticos em CSV, JSON e PNG.

---

## 📅 2. Estrutura e Conteúdo do Dataset Bruto

O dataset possui **1.000 registros** e **8 colunas**:

| Coluna | Tipo de Dado | Descrição / Valores Encontrados |
| --- | --- | --- |
| `Wood Type` 🌳 | Texto (`object`) | Tipo de madeira (ex.: *Maple, Rosewood, Oak, Bamboo, Teak, Pine, Mahogany, Walnut, Birch, Cedar*) |
| `Country` 🌍 | Texto (`object`) | País de origem/comercialização (ex.: *China, South Africa, Russia, Australia, Brazil, Canada, India, USA, Germany, Japan*) |
| `Price (USD)` 💵 | Numérico (`float64`) | Preço da madeira em dólares americanos |
| `Supply Source` 📦 | Texto (`object`) | Origem do fornecimento (*Imported* ou *Local*) |
| `Quality Rating` ⭐ | Texto (`object`) | Classificação de qualidade (*Low, Medium, High*) |
| `Popularity` 🔥 | Numérico (`int64`) | Índice de popularidade (escala numérica) |
| `Demand Level` 📈 | Texto (`object`) | Nível de demanda (*Low, Medium, High*) |
| `Availability` 🪵 | Texto (`object`) | Nível de disponibilidade (*Scarce, Moderate, Abundant*) |

---

## 🔎 3. Principais Análises que Serão Realizadas

Com base nas colunas do arquivo, o projeto analisará:

* 💰 **Distribuição de Preços por Tipo de Madeira e País:** Média, mínima, máxima e desvio padrão dos preços (`Price (USD)`) agrupados por tipo e localização geográfica.


* 🔄 **Relação entre Oferta e Demanda:** Cruzamento entre `Supply Source` (*Imported* / *Local*), `Demand Level` e `Availability`.


* ⭐ **Análise de Qualidade x Preço:** Agrupamento por `Quality Rating` para verificar o ticket médio por nível de qualidade.


* 🏷️ **Segmentação de Registro / Valor:** Classificação condicional das transações/itens por faixa de preço.


* 📄 **Exportação dos Resultados:** Geração de relatórios agregados em formato CSV e estatísticas gerais em JSON.



---

## 📂 4. Estrutura Proposta para o Repositório

```text
salesinsight-py/
│
├── salesinsight.py              # 🐍 Script principal contendo o fluxo de execução
├── wood_prices_dataset.csv     # 📊 Dataset bruto utilizado na análise
├── README.md                   # 📖 Documentação do projeto
├── outputs/
│   ├── metricas_por_madeira.csv # 📄 Agregações calculadas em CSV
│   ├── estatisticas_gerais.json # 📜 Média, mediana e métricas gerais em JSON
│   └── graficos/               # 🖼️ Visualizações exportadas em PNG
│       ├── preco_por_tipo.png
│       ├── dispersao_popularidade_preco.png
│       └── painel_resumo.png
└── planejamento/
    └── tarefas-kanban.md        # 📋 Acompanhamento do projeto (Kanban)

```

(Estrutura sugerida nas diretrizes do curso)

---

## 🛠️ 5. Requisitos de Instalação e Execução

### 💻 Dependências Técnicas

* Python 3.10+


* Bibliotecas principais:


* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`



### 🚀 Como Executar

1. Clone este repositório ou faça o download dos arquivos em seu ambiente (VS Code ou Google Colab).


2. Garanta que as dependências estejam instaladas:


```bash
pip install pandas numpy matplotlib seaborn

```


3. Execute o script principal:


```bash
python salesinsight.py

```



---

## 💡 6. Decisões Técnicas & Conceitos Aplicados

* 🐼 **Pandas & NumPy:** Utilização de `.groupby()`, `.agg()`, operações vetorizadas sem laços `for` e transformações condicionais com `np.select`.


* 📊 **Visualização com Matplotlib/Seaborn:** Construção de gráficos de barras, linha/dispersão e criação de um painel de múltiplos subplots (`plt.subplots(2, 2)`).


* 🧱 **Orientação a Objetos:** Organização do fluxo através da classe `AnalisadorDeVendas` com construtor `__init__` e métodos de tratamento e análise.



---

## 🎬 7. Vídeo de Demonstração

* 🎥 `[Inserir o link do vídeo de apresentação/demonstração aqui]`