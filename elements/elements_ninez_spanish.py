from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_ninez_spanish = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Escolarización", header=True),
            dbc.DropdownMenuItem("Tasa de escolarización pre-primaria (5 años)", href="/ninez_spanish/tasa-escolarizacion-pre-primaria-5"),
            dbc.DropdownMenuItem("Tasa de escolarización pre-primaria (3 a 5 años)", href="/ninez_spanish/tasa-escolarizacion-pre-primaria-35"),
            dbc.DropdownMenuItem("Tasa neta de escolarización primaria", href="/ninez_spanish/tasa-neta-escolarizacion-primaria"),
            dbc.DropdownMenuItem("Tasa neta de escolarización secundaria", href="/ninez_spanish/tasa-neta-escolarizacion-secundaria"),
            dbc.DropdownMenuItem("Tasa neta de escolarización terciaria", href="/ninez_spanish/tasa-neta-escolarizacion-terciaria"),
            dbc.DropdownMenuItem("Tasa de finalización del nivel primario", href="/ninez_spanish/tasa-finalizacion-primario"),
            dbc.DropdownMenuItem("Tasa de finalización del nivel secundario", href="/ninez_spanish/tasa-finalizacion-secundario"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Actividades y uso del tiempo", header=True),
            dbc.DropdownMenuItem("Participación en actividades de cuidado", href="/ninez_spanish/participacion-actividades-cuidado-ninez"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado", href="/ninez_spanish/horas-actividades-cuidado-ninez"),
            dbc.DropdownMenuItem("Participación en actividades de cuidado de niños", href="/ninez_spanish/participacion-actividades-cuidado-ninos-ninez"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado de niños", href="/ninez_spanish/horas-actividades-cuidado-ninos-ninez"),
            dbc.DropdownMenuItem("Porcentaje de jóvenes de 15 a 24 fuera de la escuela y del mercado laboral", href="/ninez_spanish/jovenes-fuera-escuela-trabajo"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Puntajes en pruebas", header=True),
            dbc.DropdownMenuItem("Puntaje promedio en pruebas estandarizadas para alumnos de tercer grado", href="/ninez_spanish/puntajes-tercero"),
            dbc.DropdownMenuItem("Puntaje promedio en pruebas estandarizadas para alumnos de sexto grado", href="/ninez_spanish/puntajes-sexto"),
            dbc.DropdownMenuItem("Puntaje promedio en pruebas estandarizadas para alumnos de 15 años", href="/ninez_spanish/puntajes-15"),
            dbc.DropdownMenuItem("Ratio de puntajes en pruebas estandarizadas para alumnos de tercer grado", href="/ninez_spanish/ratio-tercero"),
            dbc.DropdownMenuItem("Ratio de puntajes en pruebas estandarizadas para alumnos de sexto grado", href="/ninez_spanish/ratio-sexto"),
            dbc.DropdownMenuItem("Ratio de puntajes en pruebas estandarizadas para alumnos de 15 años", href="/ninez_spanish/ratio-15"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más bajo de puntajes en tercer grado", href="/ninez_spanish/mujeres-10-bajo-tercero"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más bajo de puntajes en sexto grado", href="/ninez_spanish/mujeres-10-bajo-sexto"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más bajo de puntajes de alumnos de 15 años", href="/ninez_spanish/mujeres-bajo-10-15"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más alto de puntajes en tercer grado", href="/ninez_spanish/mujeres-10-alto-tercero"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más alto de puntajes en sexto grado", href="/ninez_spanish/mujeres-10-alto-sexto"),
            dbc.DropdownMenuItem("Porcentaje de mujeres en el 10% más alto de puntajes de alumnos de 15 años", href="/ninez_spanish/mujeres-10-alto-15"),
            dbc.DropdownMenuItem("Porcentaje de mujeres entre los alumnos de 15 años analfabetos funcionales", href="/ninez_spanish/mujeres-analfabeta-funcional"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Habilidades no cognitivas", header=True),
            dbc.DropdownMenuItem("Alumnos de sexto grado que responde que si a 'Sigo las normas y reglas de la clase.'", href="/ninez_spanish/sigue-normas-6to"),
            dbc.DropdownMenuItem("Alumnos de sexto grado que responde que si a 'Pido ayuda al profesor cuando no entiendo lo que hay que hacer.'", href="/ninez_spanish/pide-ayuda-6to"),
            dbc.DropdownMenuItem("Alumnos de sexto grado que responde que si a 'Antes de entregar una tarea o examen lo reviso bien.'", href="/ninez_spanish/revisa-bien-6to"),
            dbc.DropdownMenuItem("Alumnos de sexto grado que responde que si a 'Espero mi turno para hablar en clases.'", href="/ninez_spanish/espera-para-hablar-6to"),
            dbc.DropdownMenuItem("Alumnos de sexto grado que responde que si a 'Aunque las cosas no me resulten, sigo intentándolo'", href="/ninez_spanish/sigue-intentando-6to"),
            dbc.DropdownMenuItem("Índice de autoregulación para alumnos de sexto grado", href="/ninez_spanish/hse-indice-6to"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicadores",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar_ninez_spanish = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_ninez_spanish", n_clicks=0),
                        dbc.Collapse(
                            dropdown_ninez_spanish, 
                            className="ml-auto",
                            id="navbar-collapse_ninez_spanish",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/ninez_spanish/tasa-escolarizacion-pre-primaria-5",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
    expand=True,
)

def generate_dropdown(options):
    dropdown = dcc.Dropdown(
        options=[{'label': option, 'value': option} for option in options],
        value="Argentina",
        id="all-pages-dropdown-pais-ninez-spanish",
        persistence=True,
        persistence_type = 'memory',
        multi=True,
        className="bg-light",
    )
    return dropdown

# Armar loop:
mark_values = {2000:'2000',2001:'2001',2002:'2002',
                2003:'2003',2004:'2004',2005:'2005',
                2006:'2006',2007:'2007',2008:'2008',
                2009:'2009',2010:'2010',2011:'2011',
                2012:'2012',2015:'2015',2016:'2016',
                2013:'2013',2014:'2014',2015:'2015',
                2016:'2016',2017:'2017',2018:'2018',
                2019:'2019',2020:'2020',2021:'2021',
                2022:'2022'}

ranger_slider_year_ninez_spanish = dcc.RangeSlider(
        min=2000,
        max=2022,
        value=[2000,2022],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-ninez-spanish"
)
