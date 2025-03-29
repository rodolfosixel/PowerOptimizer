import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as tick
import numpy as np
import openpyxl


def money_format(valor):
    valor_string = "{:,}".format(valor)

    valor_string = valor_string.replace('.', '_')
    valor_string = valor_string.replace(',', '.')
    valor_string = valor_string.replace('_', ',')

    return valor_string

if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define the months for the first column
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
          "Outubro", "Novembro", "Dezembro"]

# Define the column headers
columns = ["Meses", "Demanda na ponta", "Demanda Fora da Ponta", "Consumo na Ponta", "Consumo fora da ponta"]

# Create the data for the DataFrame (the first column contains the months, and the rest are sequential numbers)
data = [[months[i]] + [0.00 for j in range(4)] for i in range(12)]

# Create the DataFrame with the specified columns
dados_entrada = pd.DataFrame(data, columns=columns)

# Entrada Inicial de Estados
estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA","PB", "PE", "PI", "PR",
           "RJ", "RN", "RO", "RR", "RS", "SC", "SP", "SE", "TO"]


# Entrada Inicial de Concessionárias
def selecionar_concessionaria(estado):
    if estado == "AC":
        concessionarias = ["Energisa Acre"]
    elif estado == "AL":
        concessionarias = ["Equatorial Alagoas"]
    elif estado == "AP":
        concessionarias = ["CEA"]
    elif estado == "AM":
        concessionarias = ["Amazonas S/A"]
    elif estado == "BA":
        concessionarias = ["COELBA"]
    elif estado == "CE":
        concessionarias = ["Enel CE"]
    elif estado == "DF":
        concessionarias = ["Neoenergia Brasília"]
    elif estado == "ES":
        concessionarias = ["EDP Escelsa", "ELFSM"]
    elif estado == "GO":
        concessionarias = ["Enel GO", "Cia. Hidroelétrica São Patrício"]
    elif estado == "MA":
        concessionarias = ["Equatorial Energia Maranhão"]
    elif estado == "MT":
        concessionarias = ["Energisa Mato Grosso"]
    elif estado == "MS":
        concessionarias = ["Energisa Mato Grosso do Sul"]
    elif estado == "MG":
        concessionarias = ["CEMIG", "Energisa MG", "DME Poços de Caldas"]
    elif estado == "PA":
        concessionarias = ["Equatorial Energia Pará", "CERGAPA"]
    elif estado == "PB":
        concessionarias = ["Energisa Paraíba"]
    elif estado == "PE":
        concessionarias = ["Neoenergia Pernambuco"]
    elif estado == "PI":
        concessionarias = ["Equatorial Piauí"]
    elif estado == "PR":
        concessionarias = ["COPEL", "COCEL", "Forcel", "Cooperativa Castro", "CERAL Arapoti"]
    elif estado == "RJ":
        concessionarias = ["Light", "Enel RJ", "Energisa Nova Friburgo", "CERAL Araruama", "CERCI Papucaia",
                           "CERES"]
    elif estado == "RN":
        concessionarias = ["Neoenergia COSERN"]
    elif estado == "RO":
        concessionarias = ["CERON"]
    elif estado == "RR":
        concessionarias = ["Roraima Energia"]
    elif estado == "RS":
        concessionarias = ["CEEE", "RGE", "DEMEI Ijuí", "Hidropan", "Nova Palma Energia", "Eletrocar",
                           "MuxEnergia", "Cooperativa Centro Jacuí", "CERFOX", "CERGAL", "Ceriluz", "Cermissões",
                           "Certaja", "Certel", "Certhil", "Cooperluz", "Coopernorte", "Coopersul", "Coorsel", "Coprel",
                           "Creluz-D", "Creral"]
    elif estado == "SC":
        concessionarias = ["CELESC", "Cooperaliança", "DCELT", "Força e Luz João Cesa", "EFLUL",
                           "Cooperativa São Ludgero", "Cooperativa Jacinto Machado", "Cooperativa Praia Grande",
                           "Cooperativa Ceraça", "CERBRA Norte", "CEREJ", "CERGRAL", "CERMOFUL", "CERPALO",
                           "CERSAD", "Cersul", "Certrel", "Codesam", "Coopera", "Coopercocal", "Coopermila",
                           "Cooperzem",
                           "Iguaçu Energia"]
    elif estado == "SP":
        concessionarias = ["Enel SP", "CPFL", "CPFL Piratininga", "CPFL Santa Cruz", "Elektro",
                           "Energisa Sul Sudeste", "EDP SP", "CEDRAP", "CEDRI", "CEMIRIM", "CERIM", "CERIPA", "CERMC",
                           "CERNHE", "CERPRO", "CERRP", "Cervam", "Cetril", ]
    elif estado == "SE":
        concessionarias = ["Energisa Sergipe", "Sulgipe", "Cooperativa Centro Sul SE"]
    elif estado == "TO":
        concessionarias = ["Energisa Tocantins"]

    return concessionarias


def valor_ICMS(estado):
    if estado == "AC":
        icms = 0.17

    elif estado == "AL":
        icms = 0.17

    elif estado == "AP":
        icms = 0.18

    elif estado == "AM":
        icms = 0.18

    elif estado == "BA":
        icms = 0.18

    elif estado == "CE":
        icms = 0.18

    elif estado == "DF":
        icms = 0.18

    elif estado == "ES":
        icms = 0.17

    elif estado == "GO":
        icms = 0.17

    elif estado == "MA":
        icms = 0.18

    elif estado == "MT":
        icms = 0.17

    elif estado == "MS":
        icms = 0.17

    elif estado == "MG":
        icms = 0.18

    elif estado == "PA":
        icms = 0.17

    elif estado == "PB":
        icms = 0.18

    elif estado == "PE":
        icms = 0.18

    elif estado == "PI":
        icms = 0.18

    elif estado == "PR":
        icms = 0.18

    elif estado == "RJ":
        icms = 0.18

    elif estado == "RN":
        icms = 0.18

    elif estado == "RO":
        icms = 0.175

    elif estado == "RR":
        icms = 0.17

    elif estado == "RS":
        icms = 0.17

    elif estado == "SC":
        icms = 0.17

    elif estado == "SP":
        icms = 0.18

    elif estado == "SE":
        icms = 0.18

    elif estado == "TO":
        icms = 0.18

    return icms


def definir_sigla(value):
    if value == "Amazonas S/A":
        sigla = "AME"
    elif value == "Cooperativa Castro":
        sigla = "CASTRO-DIS"
    elif value == "CEA":
        sigla = "CEA"
    elif value == "Equatorial Alagoas":
        sigla = "Ceal"
    elif value == "Neoenergia Brasília":
        sigla = "Neoenergia Brasília"
    elif value == "CEDRAP":
        sigla = "Cedrap"
    elif value == "CEDRI":
        sigla = "Cedri"
    elif value == "CEEE":
        sigla = "CEEE-D"
    elif value == "Cooperativa São Ludgero":
        sigla = "Cegero"
    elif value == "Cooperativa Jacinto Machado":
        sigla = "Cejama"
    elif value == "CELESC":
        sigla = "Celesc-DIS"
    elif value == "Cooperativa Centro Jacuí":
        sigla = "CELETRO"
    elif value == "Equatorial Energia Pará":
        sigla = "EQUATORIAL PA"
    elif value == "Neoenergia Pernambuco":
        sigla = "Neoenergia PE"
    elif value == "Equatorial Energia Maranhão":
        sigla = "Equatorial MA"
    elif value == "CEMIG":
        sigla = "Cemig-D"
    elif value == "CEMIRIM":
        sigla = "Cemirim"
    elif value == "Equatorial Piauí":
        sigla = "Cepisa"
    elif value == "Cooperativa Praia Grande":
        sigla = "Ceprag"
    elif value == "Cooperativa Ceraça":
        sigla = "Ceraça"
    elif value == "CERAL Araruama":
        sigla = "CERAL ARARUAMA"
    elif value == "CERAL Arapoti":
        sigla = "Ceral DIS"
    elif value == "CERBRA Norte":
        sigla = "Cerbranorte"
    elif value == "CERCI Papucaia":
        sigla = "CERCI"
    elif value == "Cooperativa Centro Sul SE":
        sigla = "Cercos"
    elif value == "CEREJ":
        sigla = "Cerej"
    elif value == "CERES":
        sigla = "Ceres"
    elif value == "CERFOX":
        sigla = "Cerfox"
    elif value == "CERGAL":
        sigla = "Cergal"
    elif value == "CERGAPA":
        sigla = "Cergapa"
    elif value == "CERGRAL":
        sigla = "Cergral"
    elif value == "Ceriluz":
        sigla = "Ceriluz"
    elif value == "CERIM":
        sigla = "Cerim"
    elif value == "CERIPA":
        sigla = "Ceripa"
    elif value == "CERMC":
        sigla = "CERMC"
    elif value == "Cermissões":
        sigla = "Cermissões"
    elif value == "CERMOFUL":
        sigla = "Cermoful"
    elif value == "CERNHE":
        sigla = "Cernhe"
    elif value == "CERON":
        sigla = "Ceron"
    elif value == "CERPALO":
        sigla = "Cerpalo"
    elif value == "CERPRO":
        sigla = "Cerpro"
    elif value == "CERRP":
        sigla = "CERRP"
    elif value == "CERSAD":
        sigla = "Cersad"
    elif value == "Cia. Hdroelétrica São Patrício":
        sigla = "Chesp"
    elif value == "COCEL":
        sigla = "Cocel"
    elif value == "COELBA":
        sigla = "COELBA"
    elif value == "COPEL":
        sigla = "COPEL-DIS"
    elif value == "Neoenergia COSERN":
        sigla = "Cosern"
    elif value == "CPFL":
        sigla = "CPFL-PAULISTA"
    elif value == "Enel SP":
        sigla = "ELETROPAULO"
    elif value == "DEMEI Ijuí":
        sigla = "DEMEI"
    elif value == "DME Poços de Caldas":
        sigla = "DMED"
    elif value == "Energisa Paraíba":
        sigla = "EBO"
    elif value == "EDP Escelsa":
        sigla = "EDP ES"
    elif value == "Força e Luz João Cesa":
        sigla = "EFLJC"
    elif value == "EFLUL":
        sigla = "Eflul"
    elif value == "Energisa Acre":
        sigla = "EAC"
    elif value == "Energisa MG":
        sigla = "EMG"
    elif value == "Energisa Mato Grosso do Sul":
        sigla = "EMS"
    elif value == "Energisa Mato Grosso":
        sigla = "EMT"
    elif value == "Energisa Nova Friburgo":
        sigla = "ENF"
    elif value == "Energisa Paraíba":
        sigla = "EPB"
    elif value == "Energisa Sergipe":
        sigla = "ESE"
    elif value == "Energisa Sul Sudeste":
        sigla = "ESS"
    elif value == "Energisa Tocantis":
        sigla = "ETO"
    elif value == "Iguaçu Energia":
        sigla = "Ienergia"
    elif value == "Nova Palma Energia":
        sigla = "Uhenpal"
    else:
        sigla = (value)

    return sigla

st.set_page_config(page_title="Otimização de Demanda", page_icon=":zap:", layout="wide", initial_sidebar_state="auto", menu_items=None)

with st.sidebar:
    st.write("Programa desenvolvido com objetivo de otimizar a demanda dos clientes do Grupo A")
    st.write("Em caso de dúvidas ou sugestões para melhoria, estou à disposição para contato")
    st.write("Email: rodolfosixel@gmail.com")
    st.write("---")
    st.write("Desenvolvido por: Rodolfo Almeida Sixel Juliani")
    st.write("---")
    st.write("Versão 0.1 (Beta)")



st.title("""Otimização de Demanda :zap:""")

st.header("""Entrada de dados""")

with st.expander(("Padrões para entrada de dados")):
    st.markdown((
        """
        É possível copiar e colar as colunas do Excel diretamente na planilha abaixo.
        
        É muito importante observar que o programa aceita apenas "." como separador decimal.
        
        Sugere-se uma conferência dos dados após colagem.
    """
    ))

sample_data = [
    {
        "mes": months[0],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[1],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[2],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[3],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[4],
        "demanda_ponta": 10.9,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[5],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[6],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[7],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[8],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[9],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[10],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
    {
        "mes": months[11],
        "demanda_ponta": 10,
        "demanda_fora_ponta": 20,
        "consumo_ponta": 300,
        "consumo_fora_ponta": 2000,
    },
]

config = {
    "mes": st.column_config.TextColumn("Mês", required=True),
    "demanda_ponta": st.column_config.NumberColumn("Demanda na ponta"),
    "demanda_fora_ponta": st.column_config.NumberColumn("Demanda fora da ponta"),
    "consumo_ponta": st.column_config.NumberColumn("Consumo na ponta"),
    "consumo_fora_ponta": st.column_config.NumberColumn("Consumo fora da ponta"),
}

file_path = 'Exemplo.xlsx'
# Provide download link for the existing Excel file
data_sheets = pd.read_excel('Exemplo.xlsx')

dados_entrada_planilhas = st.data_editor(sample_data, column_config=config, num_rows="dynamic")
vetor_demanda_ponta = []
vetor_demanda_fp = []
vetor_consumo_ponta= []
vetor_consumo_fp = []

for i in range (0, 12):
    vetor_demanda_ponta.append(dados_entrada_planilhas[i]['demanda_ponta'])
    vetor_demanda_fp.append(dados_entrada_planilhas[i]['demanda_fora_ponta'])
    vetor_consumo_ponta.append(dados_entrada_planilhas[i]['consumo_ponta'])
    vetor_consumo_fp.append(dados_entrada_planilhas[i]['consumo_fora_ponta'])


def obter_tarifas(cor):
    pis_cofins = 0.08  # valor padronizado de PIS e COFINS
    estado = estado_selecionado  # estado selecionado pelo usuario
    icms = valor_ICMS(estado)  # valor do ICMS para o estado selecionado

    impostos = round(pis_cofins + icms, 2)  # valor de impostos total

    impostos = 0

    conc = concessionaria_selecionada
    sigla = sigla_conc  # Sigla da concessionária
    grupo = 'A4'  # seleção do grupo de tarifação
    # excel_file = 'Tarifas_atualizadas.xlsx'  # Nome da planilha padrão
    excel_file = 'Tarifas_Teste_2025.xlsx'
    banco = pd.read_excel(excel_file)

    if cor == 'Verde':
        # filtro para concessionária, grupo e modalidade tarifária
        banco_novo = banco.loc[(banco['Sigla'] == sigla) & (banco['Subgrupo'] == grupo)
                               & (banco['Modalidade'] == 'Verde') & (banco['Detalhe'] == 'Não se aplica')
                               & (banco['Base Tarifária'] == 'Tarifa de Aplicação')]

        # filtro para valores de energia fora da ponta
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Fora ponta') & (banco_novo['Unidade'] == 'MWh')]

        # filtros e equação para determinar a tarifa de consumo fora da ponta (kWh) Tarifa = TE + TUSD
        preco_consumo_fp = (1 + impostos) * (float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE'])) / 1000

        # filtro para valores de energia na ponta
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Ponta') & (banco_novo['Unidade'] == 'MWh')]

        # filtros e equação para determinar a tarifa de consumo na ponta (kWh) Tarifa = TE + TUSD
        preco_consumo_ponta = (1 + impostos) * (
                    float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE'])) / 1000

        # filtro para valores de demanda (kW) > 'Não se aplica' é utilizado em Modalidade Verde
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Não se aplica') & (banco_novo['Unidade'] == 'kW')]

        # filtros e equação para determinar a tarifa de demanda
        preco_demanda_fp = (1 + impostos) * float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE'])

        # Multa = 2 * preço
        preco_demanda_ult_fp = 2 * preco_demanda_fp

        # se a Modalidade é verde, então demanda na ponta = 0
        preco_demanda_ponta = 0

        # Multa = 2 * preço
        preco_demanda_ult_ponta = 2 * preco_demanda_ponta

    elif cor == 'Azul':
        # filtro para concessionária, grupo e modalidade tarifária
        banco_novo = banco.loc[(banco['Sigla'] == sigla) & (banco['Subgrupo'] == grupo)
                               & (banco['Modalidade'] == 'Azul') & (banco['Detalhe'] == 'Não se aplica')
                               & (banco['Base Tarifária'] == 'Tarifa de Aplicação')]

        # filtro para valores de energia fora da ponta
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Fora ponta') & (banco_novo['Unidade'] == 'MWh')]

        # filtros e equação para determinar a tarifa de consumo fora da ponta (kWh) Tarifa = TE + TUSD
        preco_consumo_fp = round((1 + impostos) * (float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE'])) / 1000, 2)

        # filtro para valores de energia na ponta
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Ponta') & (banco_novo['Unidade'] == 'MWh')]

        # filtros e equação para determinar a tarifa de consumo na ponta (kWh) Tarifa = TE + TUSD
        preco_consumo_ponta = round((1 + impostos) * (
                    float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE'])) / 1000,2)

        # filtro para valores de demanda (kW) fora da ponta
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Fora ponta') & (banco_novo['Unidade'] == 'kW')]

        # filtros e equação para determinar a tarifa de demanda fora da ponta (kW) Tarifa = TE + TUSD
        preco_demanda_fp = round((1 + impostos) * float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE']), 2)

        # Multa = 2 * preço
        preco_demanda_ult_fp = round(2 * preco_demanda_fp, 2)

        # filtro para valores de demanda (kW) na ponta
        linha = banco_novo.loc[(banco_novo['Posto'] == 'Ponta') & (banco_novo['Unidade'] == 'kW')]

        # filtros e equação para determinar a tarifa de demanda na ponta (kW) Tarifa = TE + TUSD
        preco_demanda_ponta = round((1 + impostos) * (float(linha.iloc[0]['TUSD']) + float(linha.iloc[0]['TE'])), 2)

        # Multa = 2 * preço
        preco_demanda_ult_ponta = round(2 * preco_demanda_ponta, 2)

    else:  # definir os valores como zero caso a modalidade tarifária não tenha sido selecionada
        preco_demanda_fp = 0
        preco_demanda_ult_fp = 0
        preco_demanda_ponta = 0
        preco_demanda_ult_ponta = 0
        preco_consumo_fp = 0
        preco_consumo_ponta = 0

    tarifas = [preco_demanda_fp, preco_demanda_ult_fp, preco_demanda_ponta, preco_demanda_ult_ponta,
               preco_consumo_fp, preco_consumo_ponta]


    print(tarifas)
    return tarifas


def custo_atual():
    conc = concessionaria_selecionada
    custo_total = 0
    demanda_verde = float(demanda_contratada_verde)
    demanda_azul = float(demanda_contratada_azul)

    demanda_teste, demanda_contratada_teste = vetor_demanda_fp, demanda_verde  # receber valores de demanda
    # vetor_consumo_fp, vetor_consumo_ponta = vetoreceber_valores_consumo()
    demanda_ponta_teste, demanda_contratada_ponta_teste = vetor_demanda_ponta, demanda_azul

    if modalidade == "Verde":
        tarifa_vec = obter_tarifas(cor='Verde')  # definição de tarifas
        valor_fp = objetivo_fp(tarifa_vec, demanda_teste, demanda_verde)
        consumo, gasto_consumo_fp_verde, gasto_consumo_ponta_verde = gastos_consumo(tarifa_vec, vetor_consumo_fp,
                                                                                    vetor_consumo_ponta)
        custo_total = valor_fp + consumo
        custo_demanda = valor_fp

    elif modalidade == "Azul":
        tarifa_vec = obter_tarifas(cor='Azul')
        valor_fp = objetivo_fp(tarifa_vec, demanda_teste, demanda_verde)
        valor_ponta = objetivo_ponta(tarifa_vec, demanda_ponta_teste, demanda_azul)
        consumo, gasto_consumo_fp_azul, gasto_consumo_ponta_azul = gastos_consumo(tarifa_vec, vetor_consumo_fp,
                                                                                  vetor_consumo_ponta)
        custo_total = round(valor_fp + valor_ponta + consumo, 2)
        custo_demanda = round(valor_fp + valor_ponta, 2)

    return custo_total, custo_demanda


gasto_anual = 30


def objetivo_ponta(tarifas, vetor_demanda, x):
    tarifa_ponta = tarifas[2]
    multa_ponta = tarifas[3]
    f_obj = 0
    custo_demanda = 0
    custo_multa = 0
    vetor_demanda_ult_novo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    obj = []

    # preenchendo valores de demanda ultrapassada que geram multa
    for i in range(0, 12):
        if vetor_demanda[i] > 1.05 * x:
            vetor_demanda_ult_novo[i] = vetor_demanda[i] - x
        else:
            vetor_demanda_ult_novo[i] = 0

    for i in range(0, 12):
        # 1 - demanda < contratada ⇨ sem multa e valor faturado é o contratado
        if vetor_demanda[i] <= x:
            f_obj += tarifa_ponta * x
            obj.append(tarifa_ponta * x)
            custo_demanda += tarifa_ponta * x

        # 2 - demanda > 1.05 * contratada ⇨ com multa
        elif vetor_demanda[i] > 1.05 * x:
            f_obj += tarifa_ponta * vetor_demanda[i] + multa_ponta * vetor_demanda_ult_novo[i]
            obj.append(tarifa_ponta * vetor_demanda[i] + multa_ponta * vetor_demanda_ult_novo[i])
            custo_demanda += tarifa_ponta * vetor_demanda[i]
            custo_multa += multa_ponta * vetor_demanda_ult_novo[i]

        # 3 - demanda > contratada, mas não supera os 5% ⇨ sem multa e valor faturado é o medido
        elif x < vetor_demanda[i] < 1.05 * x:
            f_obj += tarifa_ponta * vetor_demanda[i]
            obj.append(tarifa_ponta * vetor_demanda[i])
            custo_demanda += tarifa_ponta * vetor_demanda[i]

    return f_obj


def objetivo_fp(tarifas, vetor_demanda, x):
    tarifa_fp = tarifas[0]
    multa_fp = tarifas[1]
    f_obj = 0  # valor de custo anual
    custo_demanda = 0
    custo_multa = 0
    vetor_demanda_ult_novo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    obj = []

    # criando vetor de demanda ultrapassada (caso seja 5% acima do valor contratado)
    for i in range(0, 12):
        if vetor_demanda[i] > 1.05 * x:
            vetor_demanda_ult_novo[i] = vetor_demanda[i] - x
        else:
            vetor_demanda_ult_novo[i] = 0

    for i in range(0, 12):  # adicionar os valores à função objetivo conforme a situação
        # 1 - demanda < contratada ⇨ sem multa e valor faturado é o contratado
        if vetor_demanda[i] <= x:
            f_obj += tarifa_fp * x
            obj.append(tarifa_fp * x)
            custo_demanda += tarifa_fp * x

        # 2 - demanda > 1.05 * contratada ⇨ com multa
        elif vetor_demanda[i] > 1.05 * x:
            f_obj += tarifa_fp * vetor_demanda[i] + multa_fp * vetor_demanda_ult_novo[i]
            obj.append(tarifa_fp * vetor_demanda[i] + multa_fp * vetor_demanda_ult_novo[i])
            custo_demanda += tarifa_fp * x
            # custo_multa = multa_fp * vetor_demanda_ult_novo[i]

        # 3 - demanda > contratada, mas não supera os 5% ⇨ sem multa e valor faturado é o medido
        elif x < vetor_demanda[i] < 1.05 * x:
            f_obj += tarifa_fp * vetor_demanda[i]
            obj.append(tarifa_fp * vetor_demanda[i])
            custo_demanda += tarifa_fp * x
    return f_obj


def gastos_consumo(tarifas, consumo_fp, consumo_ponta):
    gasto_consumo_fp = 0
    gasto_consumo_ponta = 0

    for i in range(0, 12):
        gasto_consumo_fp += tarifas[4] * consumo_fp[i]
        gasto_consumo_ponta += tarifas[5] * consumo_ponta[i]

    total = gasto_consumo_fp + gasto_consumo_ponta

    return total, gasto_consumo_fp, gasto_consumo_ponta

vec_otimo = []


def varredura(a, b, demanda_contratada):
    # Função para cálculo da melhor demanda utilizando busca extensiva por varredura
    # A função roda por todos os valores definidos dentro dos limites (a,b) e checa o custo total para cada demanda
    tarifas = obter_tarifas("Verde")

    otimo_varredura = objetivo_fp(tarifas, vetor_demanda_fp, float(demanda_contratada))
    demanda_otima = demanda_contratada
    for x in range(a, b):
        teste = objetivo_fp(tarifas, vetor_demanda_fp, x)
        vec_otimo.append(teste)

        if teste < otimo_varredura:
            otimo_varredura = objetivo_fp(tarifas, vetor_demanda_fp, x)
            demanda_otima = x

    # plot_otimo_verde(vec_otimo,demanda_otima)
    return otimo_varredura, demanda_otima


def varredura_azul(a, b, demanda_contratada, demanda_contratada_azul):
    # Função para cálculo da melhor demanda utilizando busca extensiva por varredura
    # A função roda por todos os valores definidos dentro dos limites (a,b) e checa o custo total para cada demanda
    tarifas = obter_tarifas("Verde")

    otimo_varredura_fp = objetivo_fp(tarifas, vetor_demanda_fp, float(demanda_contratada))
    demanda_otima_fp = demanda_contratada
    for x in range(a, b):
        teste = objetivo_fp(tarifas, vetor_demanda_fp, x)
        if teste < otimo_varredura_fp:
            otimo_varredura_fp = objetivo_fp(tarifas, vetor_demanda_fp, x)
            demanda_otima_fp = x

    tarifas = obter_tarifas("Azul")
    otimo_varredura_ponta = objetivo_ponta(tarifas, vetor_demanda_ponta, float(demanda_contratada_azul))
    demanda_otima_ponta = demanda_contratada_azul
    for x in range(a, b):
        teste = objetivo_ponta(tarifas, vetor_demanda_ponta, x)
        if teste < otimo_varredura_ponta:
            otimo_varredura_ponta = objetivo_ponta(tarifas, vetor_demanda_ponta, x)
            demanda_otima_ponta = x

    return otimo_varredura_fp, demanda_otima_fp, otimo_varredura_ponta, demanda_otima_ponta

def plot_otimo_verde(vec_otimo,demanda_otima):
    x = []
    for i in range (30,1000):
        x.append(i)

    x_max = 1.3*demanda_otima
    minimo = min(vec_otimo)
    plt.figure(figsize=(20, 10))
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.xlabel("Demanda (kW", fontsize=30)
    plt.ylabel("Valor (R$)", fontsize=30)
    plt.title('Simulação: Modalidade Tarifária Verde', fontsize=36)
    plt.ylim(0, minimo*1.6)
    plt.plot(x, vec_otimo, color='red', ls='--', label='Custo por demanda', linewidth=4)
    # plt.plot( , color='red', ls='--', label='Custo por demanda', linewidth=4)
    plt.xlim(30, x_max)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.legend(fontsize=30, loc=4)
    fig = plt.gcf()
    st.pyplot(fig=fig)
    fig.savefig('Demanda_Teste.png', format='png')  # salvar o gráfico em png
    fig.savefig('Demanda_Teste.pdf', format='pdf', bbox_inches='tight')  # salvar o gráfico em pdf
    print("Grafico Verde gerado com sucesso")


def plotar_verde(demanda_contratada, demanda_otima, demanda_fp):
    # Função para plotar o gráfico que simula a situação verde. Demanda contratada, ótima e perfil de consumo
    demanda_cont_vec = []
    demanda_otima_vec = []
    maximo = 1.2 * max(demanda_fp)  # valor arbitrário para ajustar escala
    for i in range(0, 12):
        demanda_cont_vec.append(float(demanda_contratada))
        demanda_otima_vec.append(demanda_otima)

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    plt.figure(figsize=(20, 10))
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.xlabel("Meses", fontsize=30)
    plt.ylabel("Demanda de Potência (kW)", fontsize=30)
    plt.title('Simulação: Modalidade Tarifária Verde', fontsize=36)
    plt.ylim(0, maximo)
    plt.plot(x, demanda_cont_vec, color='red', ls='--', label='Demanda Atual', linewidth=4)
    plt.plot(x, demanda_otima_vec, color='forestgreen', ls='-', label='Demanda Sugerida', linewidth=4)
    plt.plot(x, demanda_fp, color='blue', label='Demanda Medida', linestyle='dashdot', linewidth=4)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], fontsize=30)
    plt.xlim(1, 12)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.legend(fontsize=30, loc=4)
    fig = plt.gcf()
    st.pyplot(fig=fig)
    fig.savefig('Demanda_Verde.png', format='png')  # salvar o gráfico em png
    fig.savefig('Demanda_Verde.pdf', format='pdf', bbox_inches='tight')  # salvar o gráfico em pdf
    print("Grafico Verde gerado com sucesso")


def plotar_azul(demanda_contratada_ponta, demanda_otima_ponta, demanda_fp):
    demanda_cont_vec = []
    demanda_otima_vec = []
    maximo = 1.2 * max(demanda_fp)  # valor arbitrário para limite do gráfico
    for i in range(0, 12):
        demanda_cont_vec.append(float(demanda_contratada_ponta))
        demanda_otima_vec.append(demanda_otima_ponta)

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    plt.figure(figsize=(20, 10))
    plt.xlabel("Meses", fontsize=30)  # título do eixo x
    plt.ylabel("Demanda de Potência na Ponta (kW)", fontsize=30)  # título do eixo y
    plt.title('Simulação: Modalidade Tarifária Azul', fontsize=36)  # título do gráfico
    plt.ylim(0, maximo)
    plt.plot(x, demanda_cont_vec, color='red', ls='--', label='Demanda na Ponta Atual', linewidth=4)
    plt.plot(x, demanda_otima_vec, color='forestgreen', ls='-', label='Demanda na Ponta Sugerida', linewidth=4)
    plt.plot(x, demanda_fp, color='blue', label='Demanda Medida', linestyle='dashdot', linewidth=4)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], fontsize=30)
    plt.xlim(1, 12)
    plt.yticks(fontsize=30)
    plt.legend(fontsize=30, loc=4)
    fig = plt.gcf()
    st.pyplot(fig=fig)
    fig.savefig('Demanda_Azul.png', format='png')  # salvar em png
    fig.savefig('Demanda_Azul.pdf', format='pdf', bbox_inches='tight') # salvar em pdf
    print("Grafico Azul gerado com sucesso")


def plotar_completo(demanda_total_verde, demanda_total_azul, gasto_consumo_fp_verde, \
                    gasto_consumo_ponta_verde, gasto_consumo_fp_azul, gasto_consumo_ponta_azul):
    # Plotar o gráfico com os custos totais das modalidades verde e azuk para comparação

    plt.figure(figsize=(15, 20))
    fig, ax = plt.subplots()
    ticker = tick.EngFormatter(unit='')
    ax.yaxis.set_major_formatter(ticker)
    wide = 0.4

    cmap_verde = ['darkgreen', 'lime', 'green', 'palegreen']
    cmap_azul = ['navy', 'blue', 'cornflowerblue', 'darkturquoise']

    x1 = np.array([5, 6])  # posição dos valores acumulados
    x2 = np.array([1, 2, 3, 4])
    x3 = np.array([7, 8, 9, 10])

    y1 = np.array([demanda_total_verde, demanda_total_verde])  # demanda fora da ponta
    y2 = np.array([gasto_consumo_fp_verde, gasto_consumo_fp_azul])  # consumo fora da ponta
    y3 = np.array([0, demanda_total_azul])  # demanda na ponta
    y4 = np.array([gasto_consumo_ponta_verde, gasto_consumo_ponta_azul])  # consumo na ponta

    y_verde = np.array([demanda_total_verde, gasto_consumo_fp_verde, 0, gasto_consumo_ponta_verde])
    y_azul = np.array([demanda_total_verde, gasto_consumo_fp_azul, demanda_total_azul, gasto_consumo_ponta_azul])

    plt.bar(5, y1[0], width=wide, bottom=0, color='darkgreen')
    plt.bar(5, y2[0], width=wide, bottom=y1[0], color='lime')
    plt.bar(5, y3[0], width=wide, bottom=y1[0] + y2[0], color='green')
    plt.bar(5, y4[0], width=wide, bottom=y1[0] + y2[0] + y3[0], color='palegreen')

    plt.bar(6, y1[1], width=wide, bottom=0, color='navy')
    plt.bar(6, y2[1], width=wide, bottom=y1[1], color='blue')
    plt.bar(6, y3[1], width=wide, bottom=y1[1] + y2[1], color='cornflowerblue')
    plt.bar(6, y4[1], width=wide, bottom=y1[1] + y2[1] + y3[1], color='darkturquoise')

    plt.bar(x2, y_verde, width=wide, color=cmap_verde)
    plt.bar(x3, y_azul, width=wide, color=cmap_azul)

    # plt.xlabel("Modalidade Tarifária")
    plt.ylabel("Valor Total (R$)")
    plt.legend(["Demanda FP", "Energia FP", "Demanda Ponta", "Energia Ponta",
                "Demanda FP", "Energia FP", "Demanda Ponta", "Energia Ponta"])
    plt.title("Comparação de Custos")
    plt.xticks([3, 8], ['Modalidade Verde', 'Modalidade Azul'])
    # plt.show()
    # plt.yticks(fontsize=24)
    for x1, y1 in zip(x2, y_verde):
        ax.annotate('%.1f' % (y1), xy=(x1 - 0.5, y1 + 0.2))

    for x1, y1 in zip(x3, y_azul):
        ax.annotate('%.1f' % (y1), xy=(x1 - 0.5, y1 + 0.2))

    fig = plt.gcf()
    st.pyplot(fig)
    fig.savefig('Grafico_Comparativo.png', format='png')
    fig.savefig('Grafico_Comparativo.pdf', format='pdf', bbox_inches='tight')
    print("Grafico Comparativo gerado com sucesso")


st.write("---")

st.header("Situação Atual e Importação de Tarifas")

with st.expander(("Passo a passo")):
    st.markdown((
        """
        1. Selecionar modalidade tarifária
         
        2. Inserir valores de demanda contratada - utilizar " . " como separador decimal
        
        3. Selecionar o estado e a concessionária de interesse
        
        4. Importar as tarifas (Botão Importar Tarifas) da concessionária e checar valores
        
        5. Calcular o gasto anual (Botão "Calcular gasto anual") atual da Unidade consumidora  
        
    """
    ))

coluna1, coluna2 = st.columns(2)


with coluna1:

    modalidade = st.radio("Modalidade Tarifária", ["Azul", "Verde"])

    disable = False

    if modalidade == "Verde":
        disable = True

    demanda_contratada_verde = st.text_input("Demanda Contratada Fora da Ponta (kW):", "00.00", key="dcfp")
    demanda_contratada_azul = st.text_input("Demanda Contratada Ponta (kW):",
                                            "00.00", disabled=disable, key="dcp")

    options_selectbox1 = estados
    estado_selecionado = st.selectbox("Selecione o estado", options_selectbox1, index=0)
    # estado_selecionado = 'CE'

    options_selectbox2 = selecionar_concessionaria(estado_selecionado)
    concessionaria_selecionada = st.selectbox("Selecione a concessionária", options_selectbox2, index=0)
    # concessionaria_selecionada = "ENEL CE"

    icms = valor_ICMS(estado_selecionado)
    sigla_conc = definir_sigla(concessionaria_selecionada)

    # st.write(f"Sigla da concessionária: {sigla}")

    demanda_fp_valor = 0

with coluna2:
    if st.button("Importar tarifas :heavy_dollar_sign:", key="botao_tarifas"):
        tarifas_verde = obter_tarifas("Verde")
        tarifas_azul = obter_tarifas("Azul")


        st.text_input("Demanda Fora da Ponta (R$/kW)", round(tarifas_verde[0], 2), key="input_tarifas1")
        # st.text_input("Demanda Ponta Verde (R$/kW):", tarifas_verde[2], key="input_tarifas2")
        st.text_input("Demanda Ponta Azul (R$/kW):", round(tarifas_azul[2], 2), key="input_tarifas3")
        st.text_input("Consumo Fora da Ponta (R$/kWh):", round(tarifas_verde[4], 2), key="input_tarifas4")
        st.text_input(f"Consumo Ponta Verde (R$/kWh):", round(tarifas_verde[5], 2), key="input_tarifas5")
        st.text_input(f"Consumo Ponta Azul (R$/kWh):", round(tarifas_azul[5], 2), key="input_tarifa6")

    st.write("---")

    if st.button("Calcular gasto anual :dollar:"):
        custo_total, custo_demanda = custo_atual()
        custo_demanda_string = money_format(round(custo_demanda, 2))
        st.write(f"Gasto anual TUSD demanda: R$ {custo_demanda_string}")



def imprimir_dados():
    print(vetor_consumo_fp)
    print(vetor_consumo_ponta)
    print(vetor_demanda_fp)
    print(vetor_demanda_ponta)

    st.write(vetor_consumo_fp)
    st.write(vetor_demanda_fp)
    st.write(vetor_consumo_ponta)
    st.write(vetor_demanda_ponta)


st.write("---")

st.header("""Simulação e Resultados :bar_chart: :moneybag:""")

with st.expander(("Como realizar as simulações")):
    st.markdown((
        """
        O programa realizará as simulações de demanda contratada de acordo com os dados de entrada, exibindo a demanda ótima a ser contratada, a economia anual obtida e os gráficos de otimização.
        
        Existem 3 possibilidades de simulação de acordo com o interesse do usuário:

        1. Simular Verde: Otimização apenas da demanda fora da ponta.
        
        2. Simular Azul: Otimização apenas da demanda na ponta.

        3. Simulação Completa: Otimização da demanda fora da ponta e da demanda fora da ponta. O programa realiza o cálculo do custo total na modalidade azul e na modalidade verde e exibe a melhor opção.
    """
    ))


if st.button("Simular Verde :large_green_square:"):
    st.write("---")
    valor_otimo, demanda_otima_verde = varredura(30, 1000, demanda_contratada_verde)
    custo_soma, custo_demanda = custo_atual()
    economia_verde = custo_demanda - valor_otimo

    valor_otimo_string = money_format(round(valor_otimo, 2))
    st.write(f'Valor ótimo: R$ {valor_otimo_string}')
    st.write(f'Demanda Sugerida Fora da Ponta: {demanda_otima_verde} kW')

    economia_string = money_format(round(economia_verde, 2))
    st.write(f'Economia: R$ {economia_string}')

    plotar_verde(demanda_contratada_verde, demanda_otima_verde, vetor_demanda_fp)


if st.button("Simular Azul :large_blue_square:"):
    st.write("---")
    valor_otimo, demanda_otima_verde, valor_otimo_azul, demanda_otima_azul = \
        varredura_azul(30, 1000, demanda_contratada_verde, demanda_contratada_azul)

    custo_soma, custo_demanda = custo_atual()
    economia_azul = custo_demanda - valor_otimo
    st.write(f'Valor ótimo: R$ {round(valor_otimo_azul, 2)}')
    st.write(f'Demanda Sugerida na Ponta: {demanda_otima_azul} kW')
    st.write(f'Economia: R$ {round(economia_azul, 2)}')
    plotar_azul(demanda_contratada_azul, demanda_otima_azul, vetor_demanda_ponta)


if st.button("Simular Completo :heavy_check_mark: "):
    st.write("---")

    valor_otimo, demanda_otima_verde, valor_otimo_azul, demanda_otima_azul = \
        varredura_azul(30, 1000, demanda_contratada_verde, demanda_contratada_azul)

    tarifas_verde = obter_tarifas("Verde")

    total_verde, gasto_consumo_fp_verde, gasto_consumo_ponta_verde = \
        gastos_consumo(tarifas_verde, vetor_consumo_fp, vetor_consumo_ponta)
    custo_total_verde = valor_otimo + total_verde

    tarifas_azul = obter_tarifas("Azul")

    total_azul, gasto_consumo_fp_azul, gasto_consumo_ponta_azul = \
        gastos_consumo(tarifas_azul, vetor_consumo_fp, vetor_consumo_ponta)
    custo_total_azul = valor_otimo_azul + valor_otimo + total_azul

    if custo_total_verde < custo_total_azul:
        modalidade_sugerida = "Verde"
        custo_otimo = custo_total_verde
        demanda_sugerida_ponta = "-"
    else:
        modalidade_sugerida = "Azul"
        custo_otimo = custo_total_azul
        demanda_sugerida_ponta = demanda_otima_azul

    custo_soma, custo_demanda = custo_atual()
    economia = custo_soma - custo_otimo
    custo_soma_string = money_format(round(custo_soma, 2))
    st.write(f'Custo Atual: R$ {custo_soma_string}')

    custo_verde_string = money_format(round(custo_total_verde, 2))
    st.write(f'Valor Total Verde: R$ {custo_verde_string}')

    custo_azul_string = money_format(round(custo_total_azul, 2))
    st.write(f'Valor Total Azul: R$ {custo_azul_string}')

    st.write(f'Demanda Ótima Fora da Ponta: {demanda_otima_verde} kW')
    st.write(f'Demanda Ótima na Ponta: {demanda_sugerida_ponta} kW')
    st.write(f'Modalidade Sugerida: {modalidade_sugerida}')

    economia_round =  money_format(round(economia, 2))
    st.write(f'Economia: R$ {economia_round}')


    plotar_verde(demanda_contratada_verde, demanda_otima_verde, vetor_demanda_fp)
    plotar_azul(demanda_contratada_azul, demanda_otima_azul, vetor_demanda_ponta)
    plotar_completo(valor_otimo, valor_otimo_azul, gasto_consumo_fp_verde, gasto_consumo_ponta_verde,
                    gasto_consumo_fp_azul, gasto_consumo_ponta_azul)

