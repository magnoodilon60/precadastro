from datetime import datetime
import streamlit as st
import streamlit_shadcn_ui as ui
import controllers.precadControllers as precadControllers
import models.precadmanual as precadastro
# from services.database import cursor
# import pandas as pd

st.title('Cadastro de Pacientes')

dt = ui.date_picker(key="date_picker", label="Data do Pré-Cadastro")

with st.form(key='Include_Paciente'):
    input_NumPac = st.text_input(label="Insira o NumPac para o dia seguinte: ")
    input_DataColeta = st.write("Date:", dt)
    #input_DataColeta = st.text_input(label="Insira a Data da Coleta Ex: 2024-02-11 ")
    #input_HoraColeta = st.text_input(label="Insira o nome da empresa: ")
    #input_DataEntrega = st.selectbox("Selecione o Setor: ", ["Bioquimica", "Hormonio", "Hematologia", "Urina - parasitologia", "Microbiologia"])
    input_button_submit = st.form_submit_button('Cadastrar')


if input_button_submit:
    data = datetime.now()
    precadastro.NumPac = input_NumPac
    precadastro.DataColeta = input_DataColeta
    precadastro.HoraColeta = '07:00'
    precadastro.DataEntrega = input_DataColeta
    precadastro.HoraEntrega = '11:00' #data.date() dia do cadastro
    precadastro.DataFatura = input_DataColeta # data.strftime('%H:%M') #hora do cadastro
    precadastro.DataEntregaApoio = input_DataColeta + ' ' +  precadastro.HoraColeta#data.strftime('%H:%M') #hora do cadastro

    precadControllers.Incluir(precadastro)
    st.success("Pré Cadastrado realizado com Sucesso!!!")