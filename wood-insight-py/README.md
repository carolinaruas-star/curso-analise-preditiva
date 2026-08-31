# 🌳 Wood SalesInsight PY

> **Mini-projeto de análise de dados de vendas utilizando Python, Pandas, NumPy e visualização de dados.**

## 📌 Sobre o projeto

O **Wood SalesInsight PY** é um mini-projeto desenvolvido para o **Módulo 01 — Desenvolvimento de IA para Análise Preditiva**, com o objetivo de aplicar conceitos fundamentais de **Python e Análise de Dados** em um cenário próximo ao contexto profissional.

O projeto simula o trabalho de um **Analista de Dados Júnior** responsável por transformar uma base de dados de produtos de madeira em informações úteis para análise de vendas.

O fluxo desenvolvido contempla:

```text
Carregamento dos dados
        ↓
Inspeção
        ↓
Criação e adequação das variáveis
        ↓
Inserção de inconsistências
        ↓
Limpeza e tratamento
        ↓
Transformações
        ↓
Agregações e segmentação
        ↓
Análise com NumPy
        ↓
Visualização dos dados
        ↓
Exportação dos resultados
```

---

## 🎯 Objetivo

O objetivo principal é desenvolver um analisador de dados capaz de **carregar, limpar, transformar, analisar e visualizar dados de vendas**, utilizando funções reutilizáveis e programação orientada a objetos.

A análise busca responder questões como:

* 📅 Como as vendas se comportam ao longo do tempo?
* 🌳 Quais tipos de madeira apresentam maior receita?
* 🌎 Quais regiões apresentam melhor desempenho?
* 👥 Quais clientes apresentam maior volume de gastos?
* 📦 Qual é a relação entre quantidade vendida e receita?
* 📊 Como os resultados podem ser apresentados visualmente para facilitar a tomada de decisão?

---

## 🗃️ Dataset

O projeto utiliza como base o **Wood Prices Dataset**, disponível no Kaggle:

**Fonte:** [Wood Prices Dataset — Kaggle](https://www.kaggle.com/datasets/swarajkhan/wood-prices-dataset)

O dataset original possui:

* **1.000 registros**
* **8 colunas**

Entre as informações disponíveis estão:

* Tipo de madeira;
* País;
* Preço;
* Fonte de fornecimento;
* Avaliação de qualidade;
* Popularidade;
* Nível de demanda;
* Disponibilidade.

Como o dataset original não possui todas as colunas necessárias ao desafio, algumas variáveis foram criadas ou adaptadas a partir das informações existentes.

### 🔄 Adaptação da base

| Requisito do projeto | Origem/implementação                          |
| -------------------- | --------------------------------------------- |
| Data                 | Gerada a partir do nível de demanda           |
| Produto              | `Wood Type`                                   |
| Categoria            | `Supply Source`                               |
| Quantidade           | Gerada a partir de demanda e disponibilidade  |
| Preço unitário       | `Price (USD)` convertido para BRL             |
| Região               | `Country`                                     |
| Cliente              | Identificação sintética criada para a análise |

A identificação dos clientes é **sintética**, criada exclusivamente para possibilitar a etapa de segmentação exigida pelo projeto.

---

## 🧹 Tratamento e limpeza dos dados

Para demonstrar as etapas de tratamento de dados exigidas pelo projeto, foram inseridas artificialmente algumas inconsistências na base original.

Foram simulados problemas como:

* valores nulos;
* datas inválidas;
* espaços extras em textos;
* caracteres especiais;
* inconsistências na padronização dos países.

Depois disso, foi desenvolvido um processo de limpeza para corrigir os problemas identificados.

### 🔎 Inspeção

A inspeção inicial utiliza recursos como:

```python
df.shape
df.dtypes
df.isnull().sum()
df.head()
```

permitindo verificar a estrutura, os tipos de dados, os valores ausentes e os primeiros registros.

### 🧽 Limpeza

A função `limpar_dados()` realiza, entre outras etapas:

* remoção de espaços extras;
* conversão de datas utilizando `pd.to_datetime()`;
* tratamento de datas inválidas;
* remoção de registros com valores ausentes em colunas críticas;
* conversão de tipos numéricos;
* padronização textual;
* tratamento de valores inválidos.

Também é gerado um **relatório de limpeza**, permitindo acompanhar a quantidade de registros antes e depois do tratamento.

No fluxo executado no notebook:

```text
Registros iniciais: 1000
Registros removidos: 287
Registros finais: 713
```

---

## 🔄 Transformação dos dados

Após a limpeza, novas variáveis são criadas para possibilitar análises mais completas.

### 💰 Receita Total

A receita é calculada de forma vetorizada:

```python
df["Receita Total"] = df["Quantidade"] * df["Preço (BRL)"]
```

### 📅 Variáveis temporais

A partir da coluna `Data`, são extraídos:

* mês;
* nome do mês;
* trimestre;
* ano.

Exemplo:

```python
df["Mês"] = df["Data"].dt.month
df["Ano"] = df["Data"].dt.year
df["Trimestre"] = df["Data"].dt.quarter
```

### 💵 Faixa de Receita

A variável `Faixa de Receita` é criada utilizando `np.select()`, classificando as transações em:

* **Baixa**
* **Média**
* **Alta**

---

## 📊 Agregações e segmentação

Foram utilizadas operações de agrupamento com `groupby()` para analisar os dados por diferentes dimensões.

Entre elas:

* mês;
* produto/tipo de madeira;
* faixa de receita;
* país/região.

Também foi criada uma segmentação simples dos clientes em:

🥉 **Bronze**
🥈 **Prata**
🥇 **Ouro**

A classificação utiliza uma função `lambda` aplicada ao gasto total de cada cliente.

---

## 🔢 Análise com NumPy

O projeto também utiliza **NumPy** para realizar operações vetorizadas sobre os dados.

Uma coluna de receita é convertida para um array:

```python
receitas = df["Receita Total"].to_numpy()
```

A partir desse array são calculadas estatísticas como:

```python
np.mean()
np.median()
np.std()
np.sum()
np.min()
np.max()
```

Também são utilizadas:

* filtragem booleana;
* operações vetorizadas;
* broadcasting;
* normalização dos valores.

A proposta é demonstrar como operações sobre arrays podem ser realizadas sem a necessidade de percorrer os dados manualmente com laços.

---

## 📈 Visualização dos dados

Foram desenvolvidas quatro visualizações principais, conforme os requisitos do projeto.

### 📉 1. Gráfico de linha

Utilizado para analisar a **receita ao longo dos meses**.

### 📊 2. Gráfico de barras

Utilizado para comparar os **produtos/tipos de madeira com maior receita**.

### 🔵 3. Gráfico de dispersão

Relaciona:

```text
Quantidade vendida × Receita
```

permitindo observar a relação entre volume de vendas e faturamento.

### 🖼️ 4. Painel 2×2

Foi criado um painel com quatro gráficos utilizando subplots:

```python
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
```

O painel utiliza também `fig.suptitle()` para apresentar um título geral.

As figuras são customizadas com:

* títulos;
* rótulos dos eixos;
* legendas;
* paleta de cores;
* tamanho adequado;
* organização do layout.

As visualizações são exportadas em formato PNG.

---

## 🧩 Organização do código

O projeto utiliza diferentes conceitos de programação em Python para organizar o fluxo de análise.

### Funções reutilizáveis

Foram criadas funções específicas para diferentes etapas do processo, como:

```python
gerar_data()
gerar_quantidade()
sujar_dataset()
inspecionar_dados()
limpar_dados()
criar_colunas_derivadas()
```

As funções possuem parâmetros e retornos de acordo com sua finalidade.

### Função como argumento

O projeto também demonstra o uso de uma função que recebe outra função como argumento:

```python
def processar_coluna(df, coluna, funcao_transformacao, nome_saida=None):
    ...
```

Essa abordagem permite reutilizar uma mesma estrutura para diferentes transformações.

### Programação Orientada a Objetos

O fluxo também foi organizado na classe:

```python
AnalisadorDeVendas
```

A classe possui:

* construtor `__init__`;
* atributos;
* métodos;
* utilização de `self`.

Entre as responsabilidades estão etapas como:

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

## 💾 Exportação dos resultados

Os resultados da análise são exportados para formatos estruturados.

### CSV

Os dados processados podem ser exportados utilizando:

```python
df.to_csv(...)
```

### JSON

Os resultados também são armazenados em JSON utilizando:

```python
json.dump(...)
```

O arquivo JSON é posteriormente lido novamente com:

```python
json.load(...)
```

para conferência dos dados gravados.

---

## 🛠️ Tecnologias e bibliotecas

### Linguagem

* 🐍 Python 3

### Bibliotecas

* **Pandas** — manipulação, limpeza e análise dos dados;
* **NumPy** — operações vetorizadas, agregações e broadcasting;
* **Matplotlib** — criação e exportação de gráficos;
* **Seaborn** — visualizações estatísticas;
* **JSON** — exportação e leitura dos resultados;
* **re** — padronização e limpeza de textos;
* **datetime** — geração e tratamento de datas;
* **random** — geração controlada de dados sintéticos.

---

## 📚 Conceitos de Python aplicados

Durante o desenvolvimento foram aplicados conceitos como:

* variáveis;
* estruturas condicionais;
* funções;
* parâmetros e retornos;
* docstrings;
* funções `lambda`;
* funções como argumentos;
* listas e dicionários;
* compreensão do fluxo de execução;
* programação orientada a objetos;
* classes;
* construtor `__init__`;
* atributos e métodos;
* `self`;
* tratamento e manipulação de arquivos;
* utilização de bibliotecas.

---

## 📊 Conceitos de análise de dados aplicados

O projeto também contempla:

* carregamento de CSV;
* inspeção de DataFrames;
* análise de valores nulos;
* limpeza de dados;
* tratamento de datas;
* expressões regulares;
* transformação de variáveis;
* criação de colunas derivadas;
* operações vetorizadas;
* `np.select`;
* `groupby`;
* agregações;
* segmentação de clientes;
* estatística descritiva;
* análise exploratória;
* visualização de dados;
* exportação de resultados.

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acesse a pasta

```bash
cd NOME_DO_REPOSITORIO
```

### 3. Instale as dependências

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Verifique o dataset

Certifique-se de que o arquivo:

```text
wood_prices_dataset.csv
```

está disponível no diretório esperado pelo notebook/script.

### 5. Execute o notebook

O projeto pode ser executado utilizando **Jupyter Notebook**, **JupyterLab** ou **Google Colab**.

Caso esteja utilizando Jupyter:

```bash
jupyter notebook
```

Em seguida, abra:

```text
Wood_SalesInsight_PY2.ipynb
```

e execute as células em ordem.

---

## 📁 Estrutura do projeto

```text
Wood-SalesInsight-PY/
│
├── Wood_SalesInsight_PY2.ipynb
├── wood_prices_dataset.csv
├── README.md
│
└── resultados/
    ├── *.csv
    ├── *.json
    └── *.png
```

> A estrutura final dos arquivos poderá ser ajustada conforme a organização adotada no repositório.

---

## 🎥 Vídeo de demonstração

Vídeo de demonstração do projeto:

**[🔗 Assistir ao vídeo](LINK_DO_VIDEO)**

> O vídeo apresenta o funcionamento do fluxo, decisões de implementação e oportunidades de melhoria identificadas durante o desenvolvimento.

---

## 📋 Kanban

O desenvolvimento do projeto foi organizado utilizando um quadro Kanban para acompanhar as etapas e tarefas.

**[📌 Acessar o quadro Kanban](LINK_DO_KANBAN)**

---

## 🔗 Repositório

**[💻 Acessar o repositório no GitHub](LINK_DO_GITHUB)**

---

## 🚀 Possíveis melhorias

Como próximos passos, o projeto poderia evoluir para uma aplicação mais próxima de um ambiente de produção, incluindo:

* automatização da atualização dos dados;
* separação do notebook em módulos Python;
* criação de testes automatizados;
* validações mais robustas dos dados;
* criação de um dashboard interativo;
* implementação de novos indicadores de negócio;
* utilização de dados reais de vendas;
* disponibilização da análise por meio de uma aplicação web ou API.

---

## 👩‍💻 Autora

**Ana Carolina Pereira Ruas**

Mini-projeto desenvolvido no curso **Desenvolvimento de IA para Análise Preditiva — Módulo 01**.

---

## 📌 Status

🟡 **Em desenvolvimento**

O projeto encontra-se em etapa de finalização, com o fluxo principal de análise implementado e os materiais de entrega sendo organizados.
