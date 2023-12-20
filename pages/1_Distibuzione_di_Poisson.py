import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="statistica_SN",
    page_icon="🪶",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


choose = option_menu(None,["Teoria", "Esempi", "Prova con I tuoi dati"],
                     icons=['book', 'bi-lightbulb', 'kanban',],
                     menu_icon="app-indicator", default_index=0,
                      orientation="horizontal",
                     
                     
                     styles={
                        "container": {"padding": "10!important"},
                        "icon": {"color": "red", "font-size": "25px"}, 
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
                    }
                    )

if choose == "Teoria":

    col1, col2 = st.columns([1,2])
    st.image("https://www.maa.org/sites/default/files/images/upload_library/1/Portraits/poisson.jpg", caption='Siméon Denis Poisson')

    

    body = """La variabile casuale discreta di Poisson serve a modellare i fenomeni aleatori che
            avvengono nel tempo, o nello spazio, quando ci si trova di fronte a fenomeni del tipo:
            numero di eventi nell’intervallo di tempo, oppure numero di eventi per misura lineare, o
            numero di eventi per misura di superficie, ecc.. è possibili modellarli con la v.c. di Poisson.
            Poiché è una variabile discreta, la sua applicazione principale è quando ci si trova di fronte
            a dati di conteggio, cosa che avviene molto spesso nelle scienze naturali, inoltre gli eventi
            devono avvenire indipendentemente l’uno dall’altro, non devono influenzarsi a vicenda. Ad
            esempio: il numero di morti in un anno, il numero di incidenti a km, il numero di colonie a
            kmq, ecc.."""

    
    col1.markdown(body, unsafe_allow_html=False,  help=None)
    col2.subheader("Bibliografia", anchor=None, help=None, divider=False)

if choose == "Teoria":

    st.write("qui qualche esempio")

if choose == "..inserisci i tuoi dati":

    uploaded_files = st.file_uploader("", accept_multiple_files=True)
