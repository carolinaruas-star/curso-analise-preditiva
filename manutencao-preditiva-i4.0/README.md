# 🏭 Pipeline de Análise Preditiva para Manutenção de Máquinas

<!-- Badges do Projeto -->
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Imbalanced-Learn](https://img.shields.io/badge/Imbalanced--Learn_(SMOTE)-1F425F?style=for-the-badge&logo=python&logoColor=white)
![License MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

## 📋 Visão Geral do Projeto

Este projeto implementa um **pipeline de Machine Learning ponta a ponta** para prever falhas mecânicas em equipamentos de um parque fabril monitorado por sensores. O objetivo é **evitar paradas não planejadas na produção** através da previsão antecipada de quebras.

**Contexto:** Indústria 4.0 - Manutenção Preditiva com dados de 10.000 registros de operação industrial.

---
## 🎥 Vídeo de Apresentação do Projeto

Para conferir a explicação detalhada sobre o funcionamento do pipeline, metodologia aplicada e demonstração dos resultados obtidos, acesse o vídeo demonstrativo através do link abaixo:

🔗 **[Clique aqui para assistir ao vídeo do projeto no Google Drive](https://drive.google.com/drive/folders/1atl-3xEVKKrwX8Tg4PxNLnFmYZveCqna?usp=sharing)**

> **Nota para o Professor:** O link acima direciona para o arquivo de vídeo hospedado no Google Drive com as permissões de acesso liberadas para visualização.

---

## 🎯 Problema Resolvido

Um parque fabril enfrenta:
- ❌ Paradas inesperadas de produção
- ❌ Custo elevado de manutenção corretiva
- ❌ Falta de visibilidade sobre saúde dos equipamentos

**Solução:** Modelo de classificação binária que prediz `falha_maquina` (1 = Falha, 0 = Normal) baseado em:
- Temperatura do ar e do processo
- Velocidade de rotação e torque
- Desgaste da ferramenta
- **Feature engineered:** Potência = RPM × Torque (Nm)

---

## 🛠️ Tecnologias e Técnicas Utilizadas

### Linguagem e Ambiente
- **Python 3.12** via Jupyter Notebook
- **Controle de Versão:** Git/GitHub com branches de desenvolvimento

### Bibliotecas Principais
```
pandas       - Manipulação de dados tabular
numpy        - Computações numéricas
scikit-learn - Modelagem (KNN, Árvore de Decisão, StandardScaler)
imbalanced-learn (SMOTE) - Balanceamento de dados desbalanceados
matplotlib/seaborn - Visualização de dados
```

### Metodologia de Ciência de Dados

#### **Fase 1: Análise Exploratória (EDA)**
- Dimensionalidade: 10.000 linhas × 14 colunas
- Tipos de dados: Numéricos (contínuos e discretos) + Categóricos
- **Descoberta:** Dataset desbalanceado (96.5% vs 3.5% de falhas)
- 3 gráficos analíticos:
  1. Histogramas de distribuição (variáveis contínuas)
  2. Gráfico de barras (desbalanceamento da classe alvo)
  3. Matriz de correlação de Pearson (relações entre variáveis)

#### **Fase 2: Data Prep**
- Remoção de duplicados: 0 registros deletados (sem duplicatas)
- Imputação de dados ausentes (~5%): Utilizado **Mediana** (robusta a outliers)
  - Justificativa: Distribuição normal das variáveis, falhas de sensor isoladas
- Análise de Outliers: Mantidos (relevantes para padrões de falha em contexto industrial)

#### **Fase 3: Feature Engineering**
- Nova variável: **Potência (W)** = Velocidade (RPM) × Torque (Nm)
- Correlação com falha: r = +0.40 (moderada e positiva)
- Captura relação não-linear entre preditores

#### **Fase 4: Divisão e Balanceamento**
- Split: 80% Treino / 20% Teste com **stratify=y** (mantém proporção de classes)
- **SMOTE (Synthetic Minority Over-sampling):** Aplicado APENAS no treino
  - Antes: 9268 (classe 0) vs 284 (classe 1)
  - Depois: 9268 (classe 0) vs 9268 (classe 1) → 50%/50%
  - Previne **data leakage**: teste mantém distribuição original para avaliação realista

#### **Fase 5: Escalonamento (StandardScaler)**
- **KNN:** Variáveis escaladas (μ=0, σ=1)
  - Motivo: Algoritmo baseado em distância; sensível a magnitude das variáveis
- **Árvore de Decisão:** Dados sem escala
  - Motivo: Decision trees baseiam-se em valores reais; escala é irrelevante

#### **Fase 6: Ajuste de Hiperparâmetros**

**KNN - Testados K = [3, 5, 7]**
| K | Treino | Teste | Status |
|---|--------|-------|--------|
| 3 | ↑↑ Alto | ↓↓ Baixo | ⚠️ OVERFITTING |
| 5 | ↑ Alto | ↑ Moderado-Alto | ✅ **IDEAL** |
| 7 | ↑ Moderado | ↑ Moderado | ✅ OK |

**Árvore - Testados max_depth = [3, 5, None]**
| Depth | Treino | Teste | Status |
|-------|--------|-------|--------|
| 3 | ↓ Baixo | ↓ Baixo | ⚠️ UNDERFITTING |
| 5 | ↑ Alto | ↑ Moderado-Alto | ✅ **IDEAL** |
| None | ↑↑↑ Muito Alto | ↓↓ Baixo | ⚠️ SEVERE OVERFITTING |

#### **Fase 7: Avaliação e Veredito Final**
- **Métrica Principal:** Acurácia no conjunto de TESTE
- Comparação quantitativa: KNN vs Árvore
- Recomendação: Modelo com maior acurácia + melhor generalização
- Análise: Recall importante (não quer perder falhas reais!)

---

## 📊 Estrutura do Repositório

```
pipeline-manutencao-preditiva/
│
├── README.md                          # Documentação (este arquivo)
├── requirements.txt                   # Dependências Python
│
├── notebook/
│   └── pipeline_manutencao_preditiva.ipynb    # Código completo (7 fases)
│
├── data/
│   └── manutencao_preditiva.csv       # Dataset de entrada
│
└── resultados/
    ├── grafico_1_distribuicao.png     # Histogramas de distribuição
    ├── grafico_2_desbalanceamento.png # Taxa de falhas vs normal
    ├── grafico_3_correlacao.png       # Matriz de correlação
    └── modelo_final.pkl               # Modelo serializado (joblib)
```

---

## 🚀 Como Executar o Sistema

### Pré-requisitos
- Python 3.8+
- pip ou conda (gerenciador de pacotes)

### Passo 1: Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/pipeline-manutencao-preditiva.git
cd pipeline-manutencao-preditiva
```

### Passo 2: Criar Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### Passo 3: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Notebook Jupyter
```bash
jupyter notebook notebook/pipeline_manutencao_preditiva.ipynb
```

### Passo 5: Executar todas as 7 fases
- Execute cada célula em ordem (Shift + Enter)
- O notebook é estruturado linearmente pelas 7 fases
- Siga as explicações técnicas em cada seção

### Passo 6: Interpretar Resultados
- Observe a acurácia dos dois modelos
- Veja qual é recomendado
- Analise os gráficos e matrizes de confusão

---

## 📈 Resultados Esperados

Após executar todo o pipeline, você obterá:

1. **3 Gráficos de Análise Exploratória**
   - Distribuição de variáveis preditoras
   - Taxa de desbalanceamento (96.5% vs 3.5%)
   - Matriz de correlação de Pearson

2. **Dois Modelos Treinados e Avaliados**
   - KNN (K=5) com StandardScaler
   - Árvore de Decisão (max_depth=5) sem escala

3. **Métricas de Desempenho**
   - Acurácia no teste para ambos
   - Classification Report (Precisão, Recall, F1)
   - Matrizes de Confusão

4. **Recomendação Clara**
   - Qual modelo usar em produção
   - Justificativa técnica
   - Próximos passos

---

## 🔧 Melhorias Futuras

Potenciais otimizações para versões futuras:

### 1. **Ensemble de Modelos**
   - Combinar KNN + Árvore + Regressão Logística
   - Aumentar robustez via votação
   - Reduzir variância

### 2. **Hyperparameter Tuning Avançado**
   - GridSearchCV ou RandomizedSearchCV
   - Testar mais intervalos de parâmetros
   - Cross-validation mais rigorosa

### 3. **Feature Selection**
   - Usar SelectKBest ou RFE
   - Remover variáveis não-preditivas
   - Reduzir dimensionalidade

### 4. **Coleta de Mais Dados**
   - 10.000 registros é pequeno
   - Aumentar dataset para melhor generalização
   - Coletar mais exemplos de falhas (classe minoritária)

### 5. **Monitoramento em Produção**
   - Drift detection (dados mudam ao longo do tempo)
   - Retreinamento automático
   - Logging de predições

### 6. **Explicabilidade (XAI)**
   - SHAP values (entender contribuição de cada variável)
   - LIME (explicações locais)
   - Regras extraídas da árvore

### 7. **Incorporar Dados Temporais**
   - Séries temporais (histórico de falhas)
   - Lag features (valores passados)
   - Tendências (aumenta/diminui ao longo do tempo)

---

## 📊 Fluxo de Branches (Git Workflow)

```
main
├── develop
│   ├── feature/eda              [Fase 1: EDA]
│   ├── feature/data-prep        [Fase 2: Data Prep]
│   ├── feature/feature-engineering [Fase 3: Feature Engineering]
│   ├── feature/train-test-split [Fase 4: Divisão e Balanceamento]
│   ├── feature/scaling          [Fase 5: Escalonamento]
│   ├── feature/hyperparameter-tuning [Fase 6: Ajuste de Parâmetros]
│   └── feature/evaluation       [Fase 7: Avaliação]
```

**Padrão de Commit:**
```
- "implementa análise exploratória com 3 gráficos"
- "corrige imputação de valores ausentes com mediana"
- "cria feature potencia via engenharia de dados"
```

---

<div align="center">

## 👩‍💻 Autora

**Ana Carolina Pereira Ruas**  
Engenheira Florestal  
**Foco em Dados, Machine Learning, IA Generativa, LLMs, Agentes e Cloud**  
</div>

Data de Conclusão: Julho de 2026  
Disciplina: Desenvolvimento de IA para Análise Preditiva [T3]

---

## 📄 Licença

Este projeto é fornecido para fins educacionais como parte do currículo de Ciência de Dados.

---

## 📞 Suporte e Dúvidas

Para dúvidas técnicas sobre o pipeline:
1. Revise as células de texto explicativo do notebook
2. Consulte os comentários no código (justificativas técnicas)
3. Verifique a documentação das bibliotecas: 
   - [Scikit-learn Docs](https://scikit-learn.org/)
   - [Pandas Docs](https://pandas.pydata.org/)
   - [Imbalanced-learn Docs](https://imbalanced-learn.org/)

---

## 🎓 Conceitos Técnicos Abordados

- ✅ Análise Exploratória de Dados (EDA)
- ✅ Tratamento de Missing Values (Imputação)
- ✅ Detecção e Análise de Outliers (IQR)
- ✅ Feature Engineering (Criação de novas variáveis)
- ✅ Desbalanceamento de Classes e SMOTE
- ✅ Data Leakage Prevention (treino/teste isolados)
- ✅ Normalização/Escalonamento (StandardScaler)
- ✅ Algoritmos: KNN e Árvore de Decisão
- ✅ Ajuste de Hiperparâmetros (Grid Search manual)
- ✅ Identificação e Combate ao Overfitting
- ✅ Avaliação de Modelos (Acurácia, Precisão, Recall)

---

## 📌 Notas Importantes

1. **Reprodutibilidade:** Uso de `random_state=42` garante resultados consistentes entre execuções
2. **Caminhos Relativos:** Dados localizados em pasta `/data` com caminhos relativos (funciona em qualquer máquina)
3. **Sem IA Generativa:** Pipeline desenvolvido de forma autônoma conforme requisitos
4. **Validação:** Teste com dados reais, não apenas métricas de laboratório

---

**Última Atualização:** Julho 2026  
**Status:** ✅ Completo e Validado

---
⭐ *Repositório desenvolvido como parte dos estudos do Curso Análise e Desenvolvimento de IA oferecido pelo SENAI/SC*
