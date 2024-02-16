from datetime import datetime
import streamlit as st
import controllers.precadControllers as precadControllers
import models.precadmanual as precadastro
import services.secrets as secrets


# No meia o titulo da pagina
st.set_page_config(
    page_title="Ajuste Pré-cadaastro")

# chama a função de login
secrets.check_password()


#titulo central da pagina
st.title('Ajustar Pré-cadastro de Pacientes')

with st.form(key='Include_Paciente'):
    input_NumPac = st.text_input(label="Insira o NumPac para o dia seguinte: ")
    input_DataColeta = st.date_input(label="Escolha a Data da Coleta: ")
    input_DataColeta = (str(input_DataColeta))
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