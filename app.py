import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="statistica_SN",
    page_icon="🪶",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
    choose = option_menu("Menú", ["Teoria", "Esempi", "Prova con I tuoi dati"],
                         icons=['book', 'bi-lightbulb', 'kanban',],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                            "container": {"padding": "5!important", "background-color": "#fafafa"},
                            "icon": {"color": "red", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "#02ab21"},
                        }
                        )
