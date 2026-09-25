import streamlit as st
import pandas as pd
import joblib


# ============================================================
# CARREGANDO MODELO
# ============================================================

modelo = joblib.load('modelo_defasagem.joblib')
colunas_modelo = joblib.load('colunas_modelo.joblib')


# ============================================================
# TÍTULO
# ============================================================

st.title('🔎 Verificador de Defasagem Escolar')

st.write(
    'Preencha as informações abaixo para que o modelo '
    'realize a classificação da defasagem escolar.'
)


# ============================================================
# DADOS DO ALUNO
# ============================================================

ano_nasc = st.number_input(
    'Ano de nascimento',
    min_value=1996,
    max_value=2017,
    value=2011,
    step=1
)

idade = st.number_input(
    'Idade',
    min_value=7,
    max_value=27,
    value=12,
    step=1
)

genero_opcao = st.selectbox(
    'Gênero',
    ['Feminino', 'Masculino']
)

genero = {
    'Feminino': 0,
    'Masculino': 1
}[genero_opcao]


ano_ingresso = st.number_input(
    'Ano de ingresso',
    min_value=2016,
    max_value=2024,
    value=2022,
    step=1
)


# ============================================================
# INDICADORES
# ============================================================

inde = st.number_input(
    'INDE - Índice de Desenvolvimento Educacional',
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

iaa = st.number_input(
    'IAA - Índice de Autoavaliação',
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

ieg = st.number_input(
    'IEG - Índice de Engajamento',
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

ips = st.number_input(
    'IPS - Índice Psicossocial',
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

ida = st.number_input(
    'IDA - Índice de Desempenho Acadêmico',
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

matematica = st.number_input(
    'Nota de Matemática',
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

portugues = st.number_input(
    'Nota de Português',
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

ingles = st.number_input(
    'Nota de Inglês',
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)

ipv = st.number_input(
    'IPV - Índice de Ponto de Virada',
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

ian = st.selectbox(
    'IAN - Índice de Adequação ao Nível',
    [2.5, 5.0, 10.0]
)


# ============================================================
# INSTITUIÇÃO DE ENSINO
# ============================================================

instituicoes = {
    'Nenhuma das opções acima': 5,
    'Bolsista Universitário *Formado (a)': 1,
    'Concluiu o 3º EM': 2,
    'Escola JP II': 3,
    'Escola Pública': 4,
    'Privada': 6,
    'Privada *Parcerias com Bolsa 100%': 7,
    'Privada - Pagamento por Empresa Parceira': 8,
    'Privada - Programa de Apadrinhamento': 9,
    'Privada - Programa de apadrinhamento': 10,
    'Pública': 11,
    'Rede Decisão': 12
}

instituicao_opcao = st.selectbox(
    'Instituição de ensino',
    list(instituicoes.keys())
)

instituicao = instituicoes[instituicao_opcao]


# ============================================================
# DATAFRAME PARA O MODELO
# ============================================================

dados_usuario = pd.DataFrame({
    'Ano nasc': [ano_nasc],
    'Idade': [idade],
    'Gênero': [genero],
    'Ano ingresso': [ano_ingresso],
    'INDE_Indice_Desenv_Educacional': [inde],
    'IAA_Indice_Autoavaliacao': [iaa],
    'IEG_Indice_Engajamento': [ieg],
    'IPS_Indice_Psicossocial': [ips],
    'IDA_Indice_Desempenho_Academico': [ida],
    'Matematica': [matematica],
    'Portugues': [portugues],
    'Ingles': [ingles],
    'IPV_Indice_Ponto_Virada': [ipv],
    'IAN_Indice_Adequacao_Nivel': [ian],
    'Instituição_ensino_encoder': [instituicao]
})


# Garante exatamente as mesmas colunas utilizadas no treinamento
dados_usuario = dados_usuario.reindex(
    columns=colunas_modelo,
    fill_value=0
)


# ============================================================
# PREVISÃO
# ============================================================

if st.button('🔎 Verificar'):

    previsao = modelo.predict(dados_usuario)[0]

    probabilidades = modelo.predict_proba(dados_usuario)[0]

    confianca = probabilidades.max()

    st.success(
        f'📊 Defasagem prevista: {previsao}'
    )

    st.write(
        f'**Probabilidade da classificação:** '
        f'{confianca:.2%}'
    )

    st.subheader('Probabilidade por categoria')

    probabilidades_df = pd.DataFrame({
        'Defasagem': modelo.classes_,
        'Probabilidade': probabilidades
    })

    probabilidades_df['Probabilidade'] = (
        probabilidades_df['Probabilidade'] * 100
    )

    probabilidades_df = probabilidades_df.sort_values(
        'Probabilidade',
        ascending=False
    )

    st.dataframe(
        probabilidades_df,
        hide_index=True
    )