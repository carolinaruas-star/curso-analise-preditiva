# 🪵 Wood SalesInsight PY

> **Curso:** Desenvolvimento de IA para Análise Preditiva — Módulo 01
> **Professor:** Lucas Lima
> **Aluna:** Ana Carolina Pereira Ruas

---

## 📋 Sobre o Projeto

O **Wood SalesInsight PY** é um mini-projeto de análise de dados desenvolvido em Python, simulando o trabalho de uma **Analista de Dados Júnior** responsável por transformar uma base de dados de produtos de madeira em informações úteis para apoiar a tomada de decisão.

O projeto foi desenvolvido para o **Módulo 01 — Desenvolvimento de IA para Análise Preditiva**, aplicando conceitos fundamentais de:

* Python;
* Pandas;
* NumPy;
* Matplotlib;
* Seaborn;
* análise exploratória de dados;
* limpeza e transformação de dados;
* estatística descritiva;
* programação orientada a objetos.

O fluxo principal do projeto contempla:

```text
Carregamento dos dados
        ↓
Adequação da base
        ↓
Criação de variáveis sintéticas
        ↓
Inserção de inconsistências
        ↓
Inspeção
        ↓
Limpeza e tratamento
        ↓
Conversão USD → BRL
        ↓
Criação de variáveis derivadas
        ↓
Agregações
        ↓
Segmentação de clientes
        ↓
Análise estatística com NumPy
        ↓
Visualização
        ↓
Exportação
        ↓
Resumo executivo
```

As respostas às perguntas de negócio e os principais insights obtidos na análise estão documentados separadamente em **[DESAFIOS.md](DESAFIOS.md)**.

---

# 🎯 Objetivo

O objetivo é desenvolver um analisador capaz de **carregar, limpar, transformar, analisar e visualizar dados de vendas**, utilizando funções reutilizáveis e programação orientada a objetos.

O projeto foi estruturado para permitir análises relacionadas a:

* comportamento das vendas ao longo do tempo;
* desempenho dos produtos;
* desempenho por fonte de fornecimento;
* desempenho por região;
* segmentação de clientes;
* relação entre quantidade e receita;
* estatística descritiva;
* visualização de indicadores.

---

# 🗃️ Dataset

O projeto utiliza como base o **Wood Prices Dataset**, disponível no Kaggle:

**Fonte:** [Wood Prices Dataset — Kaggle](https://www.kaggle.com/datasets/swarajkhan/wood-prices-dataset)

O dataset original possui:

* **1.000 registros**;
* **8 colunas**.

Entre as informações disponíveis estão:

* tipo de madeira;
* país;
* preço em USD;
* fonte de fornecimento;
* avaliação de qualidade;
* popularidade;
* nível de demanda;
* disponibilidade.

Como o dataset original não possui todas as variáveis necessárias para o desafio, algumas colunas foram criadas ou adaptadas.

---

# 🔄 Adaptação da Base

| Requisito      | Origem / Implementação                       |
| -------------- | -------------------------------------------- |
| Data           | Gerada a partir do nível de demanda          |
| Produto        | `Wood Type`                                  |
| Categoria      | `Supply Source`                              |
| Quantidade     | Gerada a partir de demanda e disponibilidade |
| Preço unitário | `Price (USD)` convertido para BRL            |
| Região         | `Country`                                    |
| Cliente        | Identificação sintética                      |

## 📅 Data

A coluna `Data` é criada com base no nível de demanda, utilizando uma regra de sazonalidade.

São considerados os anos de **2023 e 2024**.

## 📦 Quantidade

A quantidade é gerada considerando:

* nível de demanda;
* disponibilidade.

Dessa forma, a variável é construída artificialmente para possibilitar as análises de volume de vendas.

## 👥 Clientes

Como o dataset original não possui uma identificação de cliente, foram criados **50 clientes sintéticos**, identificados como:

```text
Cliente_001
Cliente_002
...
Cliente_050
```

Os identificadores são utilizados exclusivamente para possibilitar a segmentação exigida pelo projeto.

---

# 🧹 Tratamento e Limpeza dos Dados

Para demonstrar as etapas de tratamento de dados, foram inseridas artificialmente inconsistências na base.

A função:

```python
sujar_dataset()
```

simula problemas como:

* valores nulos;
* datas inválidas;
* espaços extras;
* caracteres especiais;
* inconsistências na padronização dos países.

---

## 🔎 Inspeção

A inspeção inicial utiliza operações como:

```python
df.shape
df.dtypes
df.isnull().sum()
df.head()
```

Essas operações permitem verificar:

* quantidade de registros;
* quantidade de colunas;
* tipos de dados;
* valores ausentes;
* estrutura inicial da base.

---

## 🧽 Limpeza

A função:

```python
limpar_dados()
```

realiza etapas como:

### Remoção de espaços

```python
.str.strip()
```

### Conversão de datas

```python
pd.to_datetime(..., errors="coerce")
```

### Conversão numérica

```python
pd.to_numeric()
```

### Padronização textual

A limpeza utiliza expressões regulares (`re`) para tratar caracteres especiais, espaços e padronização dos países.

### Tratamento de valores ausentes

São removidos registros com valores ausentes em campos críticos.

Na etapa demonstrativa de limpeza:

```text
Registros iniciais:       1000
Registros removidos:       287
Registros finais:          713
```

---

# 💱 Conversão USD → BRL

O preço original do dataset está em dólares americanos.

Para realizar as análises financeiras em reais, foi utilizada a taxa:

```python
TAXA_USD_BRL = 5.70
```

A conversão é realizada de forma vetorizada:

```python
df["Preço (BRL)"] = (
    df["Preço (USD)"] * TAXA_USD_BRL
).round(2)
```

Após a conversão, a coluna `Preço (USD)` é removida.

> A taxa utilizada é uma premissa definida no projeto e pode ser alterada conforme a necessidade da análise.

---

# 🔄 Transformação dos Dados

## 💰 Receita Total

A receita é calculada por:

```python
df["Receita Total"] = (
    df["Quantidade"] * df["Preço (BRL)"]
)
```

---

## 📅 Variáveis Temporais

A partir da coluna `Data`, são extraídos:

* `Mês`;
* `Mês Nome`;
* `Trimestre`;
* `Ano`.

Exemplo:

```python
df["Mês"] = df["Data"].dt.month
df["Ano"] = df["Data"].dt.year
df["Trimestre"] = df["Data"].dt.quarter
```

---

## 💵 Faixa de Receita

A variável `Faixa de Receita` é criada utilizando `np.select()`.

As transações são classificadas em:

* **Baixa**;
* **Média**;
* **Alta**.

Essa variável permanece disponível no DataFrame derivado para análises específicas.

---

## 📦 Perfil de Volume

Também é criada uma classificação de volume:

```python
df["Perfil de Volume"] = df["Quantidade"].apply(
    lambda q:
        "Alto Volume"
        if q > 50
        else "Baixo Volume"
)
```

---

# 📊 Agregações

As análises utilizam operações de agrupamento com `groupby()`.

São calculadas métricas por diferentes dimensões, incluindo:

* mês;
* trimestre;
* tipo de madeira;
* fonte de fornecimento;
* país;
* cliente;
* faixa de receita.

Entre as métricas calculadas estão:

* receita total;
* quantidade vendida;
* número de vendas;
* ticket médio.

---

# 👥 Segmentação de Clientes

Os clientes são segmentados de acordo com o gasto total acumulado.

Foram utilizadas três categorias:

| Segmento  | Critério                            |
| --------- | ----------------------------------- |
| 🥇 Ouro   | Gasto acima de R$ 550.000           |
| 🥈 Prata  | Gasto entre R$ 460.000 e R$ 550.000 |
| 🥉 Bronze | Gasto abaixo de R$ 460.000          |

As faixas foram recalibradas considerando a escala real dos dados, pois os valores originalmente sugeridos no desafio — R$ 5.000 e R$ 15.000 — classificariam praticamente toda a carteira como Ouro.

---

# 🔢 Análise com NumPy

A receita é convertida para um array NumPy:

```python
receitas = df["Receita Total"].to_numpy()
```

São utilizadas operações como:

```python
np.mean()
np.median()
np.std()
np.sum()
np.min()
np.max()
np.percentile()
```

Também são demonstrados:

* filtragem booleana;
* operações vetorizadas;
* broadcasting;
* normalização;
* cálculo de percentis.

---

# 📈 Visualizações

O projeto utiliza **Matplotlib** e **Seaborn** para produzir visualizações analíticas.

## Gráficos principais

### 📉 Receita por mês

Gráfico de linha para análise temporal da receita.

```text
outputs/graficos/receita_por_mes.png
```

### 📊 Receita por trimestre

Gráfico de barras para comparação dos trimestres.

```text
outputs/graficos/receita_por_trimestre.png
```

### 🌳 Top 5 produtos

Gráfico de barras com os cinco produtos de maior receita.

```text
outputs/graficos/top_produtos.png
```

### 🔵 Quantidade × Receita

Gráfico de dispersão relacionando quantidade vendida e receita.

```text
outputs/graficos/quantidade_vs_receita.png
```

### 🖼️ Painel resumo

Painel consolidado com as principais visualizações.

```text
outputs/graficos/painel_resumo.png
```

---

# 📊 Visualizações Bônus

Também foram implementadas visualizações adicionais.

## 📦 Boxplot

Distribuição da receita por tipo de madeira.

```text
outputs/graficos/boxplot_receita.png
```

## 🔥 Heatmap

Receita média por tipo de madeira e mês.

```text
outputs/graficos/heatmap_receita.png
```

---

# 🧩 Organização do Código

O projeto utiliza funções reutilizáveis para separar as responsabilidades do fluxo.

Entre elas:

```python
gerar_data()
gerar_quantidade()
sujar_dataset()
inspecionar_dados()
limpar_dados()
criar_colunas_derivadas()
calcular_metricas()
segmentar_clientes()
calcular_estatisticas_numpy()
gerar_visualizacoes()
exportar_resultados()
```

---

# 🔁 Função como Argumento

O projeto demonstra o uso de uma função que recebe outra função como argumento:

```python
def processar_coluna(
    df,
    coluna,
    funcao_transformacao,
    nome_saida=None
):
    ...
```

Essa abordagem permite reutilizar uma mesma estrutura para diferentes transformações.

Exemplo:

```python
lambda x: round(x / 1000, 2)
```

---

# 🏗️ Programação Orientada a Objetos

O fluxo principal foi organizado na classe:

```python
AnalisadorDeVendas
```

A classe possui:

* construtor `__init__`;
* atributos;
* métodos;
* `self`.

Entre suas responsabilidades estão:

```text
Carregar
Limpar
Transformar
Analisar
Visualizar
Gerar resumo
Exportar resultados
```

---

# 🧬 Bônus B01 — Herança

Foi criada a classe:

```python
AnalisadorComProjecao
```

que herda de:

```python
AnalisadorDeVendas
```

A implementação utiliza:

```python
super()
```

para reaproveitar o comportamento da classe principal.

---

# 📈 Bônus B02 — Projeção

A classe derivada implementa uma projeção simples de receita utilizando **média móvel**.

A função permite projetar meses futuros:

```python
projetar(n_meses=3)
```

O gráfico correspondente é salvo em:

```text
outputs/graficos/projecao_receita.png
```

> A projeção é uma técnica simples de tendência e não representa um modelo de Machine Learning.

---

# 🔀 Bônus B03 — Pivot Table

Foi criada uma tabela dinâmica relacionando:

```text
Faixa de Receita × Mês
```

utilizando:

```python
pivot_table()
```

Resultado:

```text
outputs/pivot_faixa_mes.csv
```

---

# 📐 Bônus B05 — Percentis

Foram calculados percentis utilizando:

```python
np.percentile()
```

Os principais percentis analisados são:

* P25;
* P50;
* P75.

---

# 💾 Exportação dos Resultados

Os resultados são exportados para a pasta:

```text
outputs/
```

## CSV

Principais arquivos:

```text
outputs/metricas_por_mes.csv
outputs/segmentacao_clientes.csv
outputs/pivot_faixa_mes.csv
```

## JSON

As estatísticas gerais são armazenadas em:

```text
outputs/estatisticas_gerais.json
```

O arquivo JSON também é lido novamente com:

```python
json.load()
```

para conferência da exportação.

---

# 📋 Requisitos Funcionais Implementados

| Requisito | Descrição                                                           | Status |
| --------- | ------------------------------------------------------------------- | :----: |
| RF01      | Carregar o dataset de vendas                                        |    ✅   |
| RF02      | Inspecionar e descrever os dados                                    |    ✅   |
| RF03      | Limpar e tratar os dados com datetime e regex                       |    ✅   |
| RF04      | Criar colunas derivadas com transformações condicionais             |    ✅   |
| RF05      | Calcular métricas agregadas com `groupby` por Fonte de Fornecimento |    ✅   |
| RF06      | Segmentar clientes por nível de gasto                               |    ✅   |
| RF07      | Realizar operações numéricas com NumPy                              |    ✅   |
| RF08      | Criar visualizações com Matplotlib e Seaborn                        |    ✅   |

---

# 📌 Categoria da Análise

A categoria utilizada nas principais métricas e visualizações é **Fonte de Fornecimento**, com duas classificações:

* **Local**;
* **Importado**.

A variável **Faixa de Receita** continua disponível no dataset derivado e é utilizada em análises específicas, incluindo a tabela pivot do Bônus B03.

---

# ▶️ Como Executar

## 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

## 2. Acesse a pasta

```bash
cd NOME_DO_REPOSITORIO
```

## 3. Instale as dependências

```bash
pip install pandas numpy matplotlib seaborn
```

## 4. Verifique o dataset

Certifique-se de que o arquivo:

```text
wood_prices_dataset.csv
```

esteja disponível no diretório esperado pelo notebook.

## 5. Execute o notebook

O projeto pode ser executado em:

* Jupyter Notebook;
* JupyterLab;
* Google Colab.

Para Jupyter:

```bash
jupyter notebook
```

Depois, abra:

```text
Wood_SalesInsight_PY(3).ipynb
```

e execute as células em ordem.

---

# 📁 Estrutura do Projeto

```text
📦 Wood-SalesInsight-PY
│
├── 📄 Wood_SalesInsight_PY(3).ipynb
├── 📄 wood_prices_dataset.csv
├── 📄 README.md
├── 📄 insights_e_desafio.md
│
└── 📁 outputs/
    ├── metricas_por_mes.csv
    ├── segmentacao_clientes.csv
    ├── estatisticas_gerais.json
    ├── pivot_faixa_mes.csv
    │
    └── 📁 graficos/
        ├── receita_por_mes.png
        ├── receita_por_trimestre.png
        ├── top_produtos.png
        ├── quantidade_vs_receita.png
        ├── painel_resumo.png
        ├── projecao_receita.png
        ├── boxplot_receita.png
        └── heatmap_receita.png
```

---

# 🎥 Vídeo de Demonstração

Vídeo de demonstração do projeto:

**[🔗 Assistir ao vídeo](LINK_DO_VIDEO)**

O vídeo apresenta o funcionamento do projeto, o fluxo de análise, as decisões de implementação e os resultados obtidos.

---

# 📋 Trello

O desenvolvimento do projeto foi organizado utilizando um quadro Trello.

**[📌 Acessar o quadro Trello](https://trello.com/b/JHsh6g3A)**

---

# 🔗 Repositório

**[💻 Acessar o repositório no GitHub](https://github.com/carolinaruas-star/curso-analise-preditiva/tree/main/wood-insight-py)**

---

# 🚀 Possíveis Melhorias

Como próximos passos, o projeto poderia evoluir para uma aplicação mais próxima de um ambiente de produção, incluindo:

* automatização da atualização dos dados;
* separação do notebook em módulos Python;
* criação de testes automatizados;
* validações mais robustas dos dados;
* utilização de uma fonte de câmbio atualizada;
* criação de dashboard interativo;
* implementação de novos indicadores de negócio;
* utilização de dados reais de vendas;
* integração com banco de dados;
* disponibilização da análise por meio de aplicação web ou API;
* evolução da projeção simples para modelos preditivos.

---

# 👩‍💻 Autora

**Ana Carolina Pereira Ruas**

Mini-projeto desenvolvido no:

**Desenvolvimento de IA para Análise Preditiva — Módulo 01**

---

# 📌 Status

🟢 **Projeto concluído / em finalização dos materiais de entrega**

O fluxo principal de análise está implementado utilizando funções reutilizáveis e programação orientada a objetos.

Também foram implementados os requisitos bônus:

* ✅ B01 — Herança;
* ✅ B02 — Projeção por média móvel;
* ✅ B03 — Pivot Table;
* ✅ B04 — Boxplot e Heatmap;
* ✅ B05 — Percentis.

---

*Projeto desenvolvido para fins educacionais — Módulo 01 do Curso de IA para Análise Preditiva.* 🎓
