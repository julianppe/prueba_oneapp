import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container
# Importamos los navbars y dropdowns:
from elements.elements_empleo_spanish import dropdown_empleo_spanish, navbar_empleo_spanish
from elements.elements_empleo_english import dropdown_empleo_english, navbar_empleo_english
from elements.elements_familia_spanish import dropdown_familia_spanish, navbar_familia_spanish
from elements.elements_familia_english import dropdown_familia_english, navbar_familia_english
from elements.elements_ninez_spanish import dropdown_ninez_spanish, navbar_ninez_spanish
from elements.elements_ninez_english import dropdown_ninez_english, navbar_ninez_english
from elements.elements_gender_roles_spanish import dropdown_gender_roles_spanish, navbar_gender_roles_spanish
from elements.elements_gender_roles_english import dropdown_gender_roles_english, navbar_gender_roles_english
from elements.elements_gender_violence_spanish import dropdown_gender_violence_spanish, navbar_gender_violence_spanish
from elements.elements_gender_violence_english import dropdown_gender_violence_english, navbar_gender_violence_english

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
    external_stylesheets=external_stylesheets,
    #prevent_initial_callbacks=True,
    #suppress_callback_exceptions=True,
    url_base_pathname='/empleo_spanish/'
)

app_empleo_spanish.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
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
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("¡Atención!"),
                dbc.ModalBody("Los datos pueden presentar problemas de comparabilidad."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en español
@app_empleo_spanish.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_empleo_english = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/empleo_english",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/empleo_english/'
)

app_empleo_english.layout = html.Div(
    [
        dcc.Store(id="store_1", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
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
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("Warning!"),
                dbc.ModalBody("The data may present comparability issues."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_empleo_english.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_familia_spanish = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/familia_spanish",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/familia_spanish/'
)

app_familia_spanish.layout = html.Div(
    [
        dcc.Store(id="store_2", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_familia_spanish # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("¡Atención!"),
                dbc.ModalBody("Los datos pueden presentar problemas de comparabilidad."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_familia_spanish.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_familia_english = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/familia_english",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/familia_english/'
)

app_familia_english.layout = html.Div(
    [
        dcc.Store(id="store_3", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_familia_english # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("Warning!"),
                dbc.ModalBody("The data may present comparability issues."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_familia_english.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_ninez_spanish = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/ninez_spanish",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/ninez_spanish/'
)

app_ninez_spanish.layout = html.Div(
    [
        dcc.Store(id="store_4", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_ninez_spanish # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("¡Atención!"),
                dbc.ModalBody("Los datos pueden presentar problemas de comparabilidad."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_ninez_spanish.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_ninez_english = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/ninez_english",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/ninez_english/'
)

app_ninez_english.layout = html.Div(
    [
        dcc.Store(id="store_5", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_ninez_english # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("Warning!"),
                dbc.ModalBody("The data may present comparability issues."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_ninez_english.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_gender_roles_spanish = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/gender_roles_spanish",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/gender_roles_spanish/'
)

app_gender_roles_spanish.layout = html.Div(
    [
        dcc.Store(id="store_6", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_gender_roles_spanish # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("¡Atención!"),
                dbc.ModalBody("Los datos pueden presentar problemas de comparabilidad."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_gender_roles_spanish.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_gender_roles_english = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/gender_roles_english",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/gender_roles_english/'
)

app_gender_roles_english.layout = html.Div(
    [
        dcc.Store(id="store_7", data='Argentina'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_gender_roles_english # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("Warning!"),
                dbc.ModalBody("The data may present comparability issues."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_gender_roles_english.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_gender_violence_spanish = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/gender_violence_spanish",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/gender_violence_spanish/'
)

app_gender_violence_spanish.layout = html.Div(
    [
        dcc.Store(id="store_8", data='Bolivia'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_gender_violence_spanish # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("¡Atención!"),
                dbc.ModalBody("Los datos pueden presentar problemas de comparabilidad."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_gender_violence_spanish.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)
def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró

app_gender_violence_english = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    pages_folder="pages/gender_violence_english",
    server=server,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    url_base_pathname='/gender_violence_english/'
)

app_gender_violence_english.layout = html.Div(
    [
        dcc.Store(id="store_9", data='Bolivia'),
        dcc.Store(id="store-popup", data=False),  # Almacena si el pop-up fue cerrado
        dbc.Container([
    dbc.Row(
        [
            navbar_gender_violence_english # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True),

        # Modal (pop-up)
        dbc.Modal(
            [
                dbc.ModalHeader("Warning!"),
                dbc.ModalBody("The data may present comparability issues."),
                dbc.ModalFooter(
                    dbc.Button("Cerrar", id="close-popup", className="ml-auto")
                ),
            ],
            id="popup-modal",
            is_open=False,  # El modal se controla mediante el estado
        ),
    ]
)

# Callback para controlar el pop-up en inglés
@app_gender_violence_english.callback(
    Output("popup-modal", "is_open"),
    Output("store-popup", "data"),
    Input("close-popup", "n_clicks"),
    State("store-popup", "data"),
)

def toggle_popup_english(n_clicks, popup_shown):
    if n_clicks:
        return False, True  # Cierra el pop-up y marca que ya se cerró
    if popup_shown:
        return False, True  # Si ya se cerró una vez, no lo muestra más
    return True, popup_shown  # Muestra el pop-up si nunca se cerró


if __name__ == "__main__":
    app_empleo_spanish.run_server()
    app_empleo_english.run_server()
    app_familia_spanish.run_server()
    app_familia_english.run_server()
    app_ninez_spanish.run_server()
    app_ninez_english.run_server()
    app_gender_roles_spanish.run_server()
    app_gender_roles_english.run_server()
    app_gender_violence_spanish.run_server()
    app_gender_violence_english.run_server()

