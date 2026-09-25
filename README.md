# 🔎 Verificador de Defasagem Escolar

Aplicação desenvolvida em **Python e Streamlit** para realizar a classificação da **defasagem escolar** de um estudante utilizando um modelo de **Regressão Logística (Logistic Regression)**.

O projeto foi desenvolvido como parte do trabalho acadêmico da especialização em **Data Analytics**, utilizando dados educacionais para aplicar conceitos de tratamento de dados, análise exploratória e Machine Learning.

## 🎯 Objetivo

O objetivo do projeto é utilizar informações acadêmicas, educacionais e sociodemográficas para classificar a possível categoria de defasagem escolar de um estudante.

A aplicação recebe as informações do aluno por meio de um formulário e utiliza o modelo treinado para:

- Classificar a categoria de defasagem;
- Apresentar a probabilidade associada à classificação;
- Apresentar as probabilidades das demais categorias.

> **Importante:** a aplicação possui finalidade exclusivamente acadêmica e experimental. Os resultados não devem ser utilizados como diagnóstico ou como única fonte para tomada de decisões educacionais.

---

## 🧠 Machine Learning

O problema foi tratado como uma tarefa de **classificação multiclasse**, pois a variável `Defasagem` possui diferentes categorias.

O modelo utilizado foi:

**Logistic Regression — Regressão Logística**

A escolha foi feita considerando a natureza categórica da variável-alvo e a necessidade de realizar uma classificação entre múltiplas categorias.

O modelo foi treinado utilizando as seguintes variáveis:

| Variável |
|---|
| Ano nasc |
| Idade |
| Gênero |
| Ano ingresso |
| INDE - Índice de Desenvolvimento Educacional |
| IAA - Índice de Autoavaliação |
| IEG - Índice de Engajamento |
| IPS - Índice Psicossocial |
| IDA - Índice de Desempenho Acadêmico |
| Matemática |
| Português |
| Inglês |
| IPV - Índice de Ponto de Virada |
| IAN - Índice de Adequação ao Nível |
| Instituição de ensino |

A variável-alvo utilizada no treinamento foi:

```text
Defasagem
```

---

## 📊 Categorias de Defasagem

A variável `Defasagem` apresenta as seguintes categorias:

```text
-5
-4
-3
-2
-1
 0
 1
 2
 3
```

Por se tratar de uma classificação multiclasse, o modelo estima a probabilidade de cada uma dessas categorias para os dados informados pelo usuário.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas** — manipulação e tratamento dos dados
- **Scikit-learn** — treinamento do modelo de Machine Learning
- **Joblib** — armazenamento e carregamento do modelo
- **Streamlit** — desenvolvimento da aplicação web
- **Git/GitHub** — versionamento e disponibilização do projeto

---

## 📁 Estrutura do projeto

```text
├── app.py
├── modelo_defasagem.joblib
├── colunas_modelo.joblib
├── requirements.txt
└── README.md
```

### Arquivos principais

**`app.py`**

Código responsável pela aplicação Streamlit, incluindo:

- formulário de entrada;
- tratamento dos dados informados;
- carregamento do modelo;
- classificação;
- cálculo das probabilidades;
- apresentação dos resultados.

**`modelo_defasagem.joblib`**

Modelo de Regressão Logística treinado e salvo utilizando Joblib.

**`colunas_modelo.joblib`**

Lista das colunas utilizadas durante o treinamento do modelo. Esse arquivo garante que os dados fornecidos pela aplicação sejam organizados na mesma ordem esperada pelo modelo.

**`requirements.txt`**

Lista das bibliotecas necessárias para executar a aplicação.

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as dependências

Recomenda-se utilizar um ambiente virtual.

No Windows:

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

### 3. Executar o Streamlit

```bash
python -m streamlit run app.py
```

Após a execução, o Streamlit disponibilizará o endereço local da aplicação, normalmente:

```text
http://localhost:8501
```

---

## 🔬 Funcionamento da aplicação

O usuário informa os dados do estudante por meio do formulário.

A aplicação cria um `DataFrame` contendo as informações:

```python
dados_usuario = pd.DataFrame({
    ...
})
```

Em seguida, as colunas são reorganizadas de acordo com aquelas utilizadas durante o treinamento:

```python
dados_usuario = dados_usuario.reindex(
    columns=colunas_modelo,
    fill_value=0
)
```

O modelo realiza a classificação:

```python
previsao = modelo.predict(dados_usuario)[0]
```

E também calcula as probabilidades de cada categoria:

```python
probabilidades = modelo.predict_proba(dados_usuario)[0]
```

A aplicação apresenta ao usuário a categoria prevista e a probabilidade associada.

---

## 📌 Tratamento dos dados

Antes do treinamento, os dados passaram por etapas de preparação, incluindo:

- tratamento de valores ausentes;
- conversão das variáveis para formatos numéricos;
- transformação da variável de gênero em valores numéricos;
- codificação da instituição de ensino;
- seleção das variáveis utilizadas pelo modelo.

As variáveis categóricas foram convertidas para representação numérica para que pudessem ser utilizadas pelo algoritmo de Machine Learning.

---

## ⚠️ Limitações

O projeto possui finalidade acadêmica e apresenta algumas limitações importantes.

A distribuição das categorias de `Defasagem` não é uniforme. Algumas categorias possuem quantidade significativamente menor de registros que outras.

Além disso, a classificação representa uma estimativa produzida pelo modelo a partir dos dados utilizados em seu treinamento. Portanto, o resultado não deve ser interpretado como uma avaliação definitiva do estudante.

Também é importante destacar que **correlação entre variáveis não implica causalidade**. A utilização de determinados indicadores no modelo não significa que eles sejam, isoladamente, responsáveis pela ocorrência de uma determinada categoria de defasagem.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido como parte da especialização em **Data Analytics**, com aplicação prática dos conceitos de:

- análise e tratamento de dados;
- estatística descritiva;
- análise de correlação;
- preparação de dados para Machine Learning;
- classificação supervisionada;
- Regressão Logística;
- avaliação de modelos;
- desenvolvimento de aplicações com Streamlit.

---

## 👨‍💻 Autor

**Luiz Felipe Marinho**

Projeto acadêmico desenvolvido para aplicação prática de conceitos de **Data Analytics e Machine Learning**.