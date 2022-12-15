import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container
from elements.elements_empleo_spanish import dropdown_empleo_spanish, navbar_empleo_spanish
from elements.elements_empleo_english import dropdown_empleo_english, navbar_empleo_english
from flask import Flask

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

server = Flask(__name__)


GENLAC_LOGO = "/assets/genlac.png"


app_empleo_spanish = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/empleo_spanish",
    server=server,
    use_pages=True,
    #prevent_initial_callbacks=True,
    #suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/empleo_spanish/'
)

app_empleo_spanish.layout = html.Div(
    [
        #dcc.Store(id="store_empleo_spanish", storage_type='local', data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar_empleo_spanish # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)

app_empleo_english = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/empleo_english",
    server=server,
    use_pages=True,
    #prevent_initial_callbacks=True,
    #suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/empleo_english/'
)

app_empleo_english.layout = html.Div(
    [
        #dcc.Store(id="store_empleo_english", storage_type='local', data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar_empleo_english # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


#server.run()

if __name__ == "__main__":
    app_empleo_spanish.run_server()
    app_empleo_english.run_server()

