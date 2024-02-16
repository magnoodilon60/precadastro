from datetime import datetime
import streamlit as st
import controllers.precadControllers as precadControllers
import models.precadmanual as precadastro
import hmac

# No meia o titulo da pagina
st.set_page_config(
    page_title="Ajuste Pré-cadaastro")

# chama a função de login
# secrets.check_password()

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

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