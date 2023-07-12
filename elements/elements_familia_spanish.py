from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container
import pandas as pd

dropdown_familia_spanish = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Brechas entre cónyuges", header=True),
            dbc.DropdownMenuItem("Diferencia de edad entre conyuges", href="/familia_spanish/diferencia-edad"),
            dbc.DropdownMenuItem("Diferencia educativa entre conyuges", href="/familia_spanish/diferencia-educativa"),
            dbc.DropdownMenuItem("Diferencia de horas trabajadas entre cónyuges", href="/familia_spanish/diferencia-horas"),
            dbc.DropdownMenuItem("Porcentaje del ingreso de la pareja aportado por cada miembro", href="/familia_spanish/porcen-ingreso-pareja"),
            dbc.DropdownMenuItem("Porcentaje de personas más o igualmente educadas que su pareja que se encuentran inactivas", href="/familia_spanish/porcentaje-mas-educacion"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Autonomía", header=True),
            dbc.DropdownMenuItem("Porcentaje de adultos sin ingresos propios", href="/familia_spanish/autonomia"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Estructura y jefatura de hogar", header=True),
            dbc.DropdownMenuItem("Jefatura de hogar femenina auto-reportada", href="/familia_spanish/jefatura-hogar-auto"),
            dbc.DropdownMenuItem("Jefatura de hogar femenina según definición económica", href="/familia_spanish/jefatura-hogar-econ"),
            dbc.DropdownMenuItem("Porcentaje de hogares monoparentales", href="/familia_spanish/porcen-hog-mono"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Uso del tiempo", header=True),
            dbc.DropdownMenuItem("Participación en tareas domésticas", href="/familia_spanish/tareas-domesticas-familia"),
            dbc.DropdownMenuItem("Horas semanales en tareas domésticas", href="/familia_spanish/horas-tareas-domesticas-familia"),
            dbc.DropdownMenuItem("Participación en actividades de cuidado", href="/familia_spanish/actividades-cuidado-familia"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado", href="/familia_spanish/horas-actividades-cuidado-familia"),
            dbc.DropdownMenuItem("Participación en actividades de cuidado de niños", href="/familia_spanish/actividades-cuidado-ninos-familia"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de cuidado de niños", href="/familia_spanish/horas-actividades-cuidado-ninos-familia"),
            dbc.DropdownMenuItem("Participación en actividades de apoyo a otros hogares", href="/familia_spanish/actividades-apoyo-familia"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de apoyo a otros hogares", href="/familia_spanish/horas-actividades-apoyo-familia"),
            dbc.DropdownMenuItem("Participación en actividades de ocio", href="/familia_spanish/actividades-ocio-familia"),
            dbc.DropdownMenuItem("Horas semanales dedicadas a actividades de ocio", href="/familia_spanish/horas-actividades-ocio-familia"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Fecundidad", header=True),
            dbc.DropdownMenuItem("Número de hijos por mujer", href="/familia_spanish/hijos-por-mujer"),
            dbc.DropdownMenuItem("Tasa de fecundidad total", href="/familia_spanish/tasa-fecundidad-total"),
            dbc.DropdownMenuItem("Tasa de fecundidad deseada", href="/familia_spanish/tasa-fecundidad-deseada"),
            dbc.DropdownMenuItem("Brecha entre fecundidad y fecundidad deseada", href="/familia_spanish/brecha-fecundidad-deseada"),
            dbc.DropdownMenuItem("Brecha de fecundidad deseada entre cónyuges", href="/familia_spanish/brecha-fecundidad-deseada-conyuges"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que utilizan métodos anticonceptivos (cualquier método)", href="/familia_spanish/metodo-anticonceptivos"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que utilizan métodos anticonceptivos modernos", href="/familia_spanish/metodo-anticonceptivos-modernos"),
            dbc.DropdownMenuItem("Porcentaje de mujeres sin acceso a métodos anticonceptivos", href="/familia_spanish/metodo-anticonceptivos-sinacceso"),
            dbc.DropdownMenuItem("Fecundidad adolescente", href="/familia_spanish/fecundidad-adolescente"),
            dbc.DropdownMenuItem("Matrimonio precoz", href="/familia_spanish/matrimonio-precoz"),
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


navbar_familia_spanish = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_familia_spanish", n_clicks=0),
                        dbc.Collapse(
                            dropdown_familia_spanish, 
                            className="ml-auto",
                            id="navbar-collapse_familia_spanish",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/familia_spanish/diferencia-edad",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
    expand=True,
)

df = pd.read_csv("datasets/familia_spanish/diferencia_edad.csv")
df['indicador'] = df['indicador'].astype(str)
df['pais'] = df['pais'].astype(str)
df['comparacion_por'] = df['comparacion_por'].astype(str)
df['ano'] = df['ano'].astype(int)

dropdown_pais_familia_spanish = dcc.Dropdown(
    options=[{'label': x, 'value': x} for x in df.pais.unique()],
    id="all-pages-dropdown-pais-familia-spanish",
    persistence=True,
    persistence_type = 'memory',
    multi=True,
    value="Argentina",
    className="bg-light"
)


df2 = pd.read_csv("datasets/familia_spanish/tareas_domesticas.csv")
df2['indicador'] = df['indicador'].astype(str)
df2['pais'] = df['pais'].astype(str)

dropdown_pais_familia_spanish2 = dcc.Dropdown(
    options=[{'label': x, 'value': x} for x in df2.pais.unique()],
    id="all-pages-dropdown-pais-familia-spanish2",
    persistence=True,
    persistence_type = 'memory',
    multi=True,
    value="Argentina",
    className="bg-light"
)

# Armar loop:
mark_values = {2000:'2000',2001:'2001',2002:'2002',
                2003:'2003',2004:'2004',2005:'2005',
                2006:'2006',2007:'2007',2008:'2008',
                2009:'2009',2010:'2010',2011:'2011',
                2012:'2012',2015:'2015',2016:'2016',
                2013:'2013',2014:'2014',2015:'2015',
                2016:'2016',2017:'2017',2018:'2018',
                2019:'2019',2020:'2020',2021:'2021'}

ranger_slider_year_familia_spanish = dcc.RangeSlider(
        min=2000,
        max=2021,
        value=[2000,2021],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-familia-spanish"
)
