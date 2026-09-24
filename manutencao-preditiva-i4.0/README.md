# 🛠️ Sistema de Manutenção Preditiva na Indústria 4.0

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 1. Visão Geral do Problema
Em um parque fabril moderno monitorado por múltiplos sensores, paradas não planejadas na linha de produção causam expressivos prejuízos financeiros. Este projeto desenvolve um **Pipeline de Ciência de Dados Preditivo** capaz de identificar previamente máquinas em iminência de falha mecânica (`falha_maquina = 1`), permitindo a manutenção proativa.

## 🏗️ 2. Arquitetura do Pipeline
O projeto segue o fluxo rigoroso de Ciência de Dados:
1. **EDA (Análise Exploratória):** Análise de correlações e diagnóstico de desbalanceamento severo (3,39% de falhas).
2. **Data Prep:** Imputação por mediana e limpeza de duplicados.
3. **Feature Engineering:** Construção da variável física de potência ($\text{Potência} = \text{RPM} \times \text{Torque}$).
4. **Tratamento de Vazamento de Dados:** Aplicação de Under-Sampling e Padronização exclusivamente no conjunto de treino.
5. **Combate ao Overfitting:** Poda de árvore (`max_depth`) e calibração de vizinhos no KNN (`n_neighbors`).

## 📊 3. Resultados dos Modelos
| Modelo | Configuração / Hiperparâmetro | Acurácia Treino | Acurácia Teste |
| :--- | :--- | :---: | :---: |
| **KNN** | $K = 3$ | 91.33% | 84.40% |
| **KNN** | **$K = 5$ (Melhor KNN)** | **88.93%** | **85.40%** |
| **KNN** | $K = 7$ | 88.38% | 84.80% |
| **Árvore de Decisão** | **`max_depth=3` (Melhor Modelo)** | **86.90%** | **89.15%** |
| **Árvore de Decisão** | `max_depth=5` | 94.46% | 88.50% |
| **Árvore de Decisão** | `max_depth=None` (Overfitting) | 100.00% | 86.15% |

### 🏆 Modelo Vencedor: Árvore de Decisão (`max_depth=3`) com 89.15% de acurácia em teste.

## 🚀 4. Como Executar o Projeto

### Pré-requisitos
- Python 3.9+ instalado
- Git instalado

### Passo a Passo
```bash
# 1. Clonar o repositório
git clone [https://github.com/carolinaruas-star/manutencao-preditiva-i4.0.git](https://github.com/carolinaruas-star/manutencao-preditiva-i4.0.git)
cd manutencao-preditiva-i4.0

# 2. Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Executar o Jupyter Notebook
jupyter notebook notebooks/pipeline_manutencao_preditiva.ipynb