# 🎯 Desafios — Wood SalesInsight PY

> **Curso:** Desenvolvimento de IA para Análise Preditiva — Módulo 01
> **Professor:** Lucas Lima
> **Aluna:** Ana Carolina Pereira Ruas

Este arquivo reúne as **perguntas de negócio, respostas, resultados e insights** obtidos durante a análise do projeto.

---

## 1️⃣ Como as vendas se comportam ao longo do tempo?

As vendas apresentam **sazonalidade clara**, com pico no final do ano e queda expressiva no meio do ano.

### 📅 Receita por mês

| Período     |   Receita Total |
| ----------- | --------------: |
| 🏆 Dezembro | R$ 4.159.927,34 |
| 🥈 Novembro | R$ 4.046.512,22 |
| 🥉 Outubro  | R$ 3.537.311,39 |
| Janeiro     | R$ 3.420.395,41 |
| Março       | R$ 3.390.268,20 |
| ...         |             ... |
| 📉 Agosto   | R$ 1.104.783,32 |

### 💡 Insight

Os meses de **outubro a dezembro** concentram o maior volume de vendas, enquanto o período de **abril a setembro** representa a baixa temporada.

O agrupamento por trimestre confirmou esse padrão: **Q4 é consistentemente o trimestre mais forte**, tanto em 2023 quanto em 2024.

---

## 2️⃣ Quais produtos e categorias geram mais receita?

### 🪵 Top 5 Produtos — Tipo de Madeira

| Posição | Produto   |   Receita Total |
| ------: | --------- | --------------: |
|   🥇 1º | Bordo     | R$ 4.085.499,69 |
|   🥈 2º | Mogno     | R$ 3.995.897,72 |
|   🥉 3º | Pinho     | R$ 3.826.678,29 |
|      4º | Carvalho  | R$ 3.710.823,47 |
|      5º | Jacarandá | R$ 3.708.628,74 |

### 📦 Receita por Categoria — Fonte de Fornecimento

| Categoria |    Receita Total | Nº de Vendas |
| --------- | ---------------: | -----------: |
| Importado | R$ 14.274.863,09 |          373 |
| Local     | R$ 14.247.342,83 |          340 |

### 💡 Insight

O **Bordo** lidera a receita entre os produtos.

Entre as categorias, existe um equilíbrio muito próximo entre **Importado** e **Local**, indicando que ambas as fontes de fornecimento possuem demanda relevante no portfólio.

> **Nota:** Neste projeto, a categoria utilizada nas métricas e visualizações principais é **Fonte de Fornecimento**, com as classificações **Local** e **Importado**. A coluna **Faixa de Receita** permanece no dataset derivado para análises específicas.

---

## 3️⃣ Quais regiões têm melhor desempenho?

| País         |   Receita Total | Ticket Médio | Nº de Vendas |
| ------------ | --------------: | -----------: | -----------: |
| 🥇 India     | R$ 3.545.841,48 | R$ 47.916,78 |           74 |
| 🥈 Brazil    | R$ 3.320.820,88 | R$ 38.170,35 |           87 |
| 🥉 Russia    | R$ 3.260.178,78 | R$ 40.752,23 |           80 |
| Indonesia    | R$ 2.777.532,89 | R$ 42.731,28 |           65 |
| Australia    | R$ 2.766.655,75 | R$ 36.403,37 |           76 |
| China        | R$ 2.762.471,16 | R$ 37.330,69 |           74 |
| Germany      | R$ 2.731.249,23 | R$ 36.416,66 |           75 |
| Canada       | R$ 2.726.656,97 | R$ 42.604,02 |           64 |
| USA          | R$ 2.450.798,38 | R$ 37.704,59 |           65 |
| South Africa | R$ 2.180.000,40 | R$ 41.132,08 |           53 |

### 💡 Insight

A **Índia** lidera tanto em receita total quanto em ticket médio — ou seja, apresenta o maior valor por transação entre as regiões analisadas.

O **Brasil** aparece em segundo lugar em receita, mas apresenta um dos menores tickets médios, compensado pelo maior número de vendas (**87 transações**).

Isso indica a existência de estratégias comerciais diferentes entre as regiões.

---

## 4️⃣ Quais clientes são mais valiosos?

A segmentação foi realizada com base nos **quartis do dataset**, definindo três faixas:

| Segmento  | Critério                            |
| --------- | ----------------------------------- |
| 🥇 Ouro   | Gasto acima de R$ 550.000           |
| 🥈 Prata  | Gasto entre R$ 460.000 e R$ 550.000 |
| 🥉 Bronze | Gasto abaixo de R$ 460.000          |

### 🏆 Top 10 Clientes

| Cliente     |   Gasto Total | Segmento |
| ----------- | ------------: | -------- |
| Cliente_032 | R$ 973.908,57 | 🥇 Ouro  |
| Cliente_037 | R$ 950.129,50 | 🥇 Ouro  |
| Cliente_001 | R$ 909.257,19 | 🥇 Ouro  |
| Cliente_008 | R$ 907.998,27 | 🥇 Ouro  |
| Cliente_017 | R$ 887.255,49 | 🥇 Ouro  |
| Cliente_035 | R$ 860.287,90 | 🥇 Ouro  |
| Cliente_049 | R$ 811.945,63 | 🥇 Ouro  |
| Cliente_023 | R$ 795.674,90 | 🥇 Ouro  |
| Cliente_034 | R$ 780.088,37 | 🥇 Ouro  |
| Cliente_018 | R$ 766.108,90 | 🥇 Ouro  |

### 📊 Distribuição por Segmento

| Segmento  | Quantidade de Clientes |
| --------- | ---------------------: |
| 🥇 Ouro   |                     25 |
| 🥉 Bronze |                     16 |
| 🥈 Prata  |                      9 |

### 💡 Insight

Metade da base de clientes (**25 de 50**) está no segmento **Ouro**, indicando uma carteira com alto valor concentrado.

Os clientes **Bronze** representam 32% da base e podem ser considerados candidatos a estratégias de **upsell**.

### ⚠️ Nota metodológica

O dataset original não possuía uma coluna de cliente.

Por isso, foram criados 50 identificadores sintéticos:

```text
Cliente_001
...
Cliente_050
```

As faixas de segmentação foram recalibradas utilizando os quartis reais dos dados, pois os valores originalmente sugeridos de **R$ 5 mil / R$ 15 mil** resultariam em todos os clientes classificados como Ouro.

---

## 5️⃣ Existe relação entre quantidade vendida e receita?

**Sim — há relação direta e positiva.**

A receita foi calculada como:

```text
Receita Total = Quantidade × Preço (BRL)
```

Isso estabelece, por construção, uma relação positiva entre quantidade e receita.

### 📊 Estatísticas da Receita

| Estatística              |         Valor |
| ------------------------ | ------------: |
| 📊 Média                 |  R$ 40.003,09 |
| 📍 Mediana               |  R$ 26.449,50 |
| 📉 Mínimo                |     R$ 525,65 |
| 📈 Máximo                | R$ 201.599,30 |
| 📐 Desvio Padrão         |  R$ 38.218,79 |
| ⬆️ Vendas acima da média |  259 (36,33%) |

### 💡 Insight

A mediana (**R$ 26.449**) é significativamente menor que a média (**R$ 40.003**), indicando **assimetria positiva**.

Isso significa que existem algumas transações com receitas muito altas que elevam a média.

O desvio padrão de aproximadamente **R$ 38 mil** demonstra uma grande dispersão dos valores de receita.

A quantidade vendida possui impacto importante na receita por transação, especialmente em produtos com maior preço unitário, como **Mogno** e **Bordo**.

---

# 📌 Síntese dos Principais Insights

A análise permite destacar os seguintes pontos:

### 📅 Sazonalidade

O final do ano apresenta maior concentração de receita, especialmente no **Q4**.

### 🌳 Produtos

O **Bordo** apresentou a maior receita entre os tipos de madeira analisados.

### 📦 Fornecimento

As categorias **Importado** e **Local** apresentam desempenho bastante equilibrado.

### 🌎 Regiões

A **Índia** apresentou o melhor desempenho em receita total e ticket médio.

O **Brasil** apresentou a segunda maior receita e o maior número de transações entre os países analisados.

### 👥 Clientes

A segmentação revelou uma concentração relevante de clientes no grupo **Ouro**.

### 💰 Receita

A diferença entre média e mediana indica uma distribuição assimétrica, com algumas transações de alto valor influenciando o resultado geral.

### 📦 Quantidade × Receita

Existe uma relação positiva entre quantidade vendida e receita, uma vez que a receita é calculada diretamente pelo produto entre quantidade e preço unitário.

---

# 📊 Indicadores de Apoio

Os principais indicadores utilizados durante o desafio foram:

```text
Receita Total
Quantidade Vendida
Número de Vendas
Ticket Médio
Média
Mediana
Desvio Padrão
Mínimo
Máximo
Percentis
Vendas acima da média
Segmentação de Clientes
```

---

# 🧠 Conclusão do Desafio

A análise demonstra como uma base de dados inicialmente voltada a preços de madeira pode ser adaptada para um cenário de análise de vendas.

A combinação de **Pandas**, **NumPy**, **Matplotlib** e **Seaborn** permitiu transformar os dados em indicadores capazes de responder às principais questões de negócio.

Os resultados destacam:

* sazonalidade nas vendas;
* diferenças de desempenho entre produtos;
* equilíbrio entre fontes de fornecimento;
* diferenças regionais;
* concentração de valor em determinados clientes;
* relação entre volume e receita;
* assimetria na distribuição dos valores de venda.

Os detalhes técnicos de implementação, estrutura do projeto, requisitos funcionais e instruções de execução estão documentados no **README.md**.
