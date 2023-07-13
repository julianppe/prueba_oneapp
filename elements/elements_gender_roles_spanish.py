from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_gender_roles_spanish = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Ámbito político", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “Los hombres son mejores líderes políticos que las mujeres”", href="/gender_roles_spanish/hombres-mejores-lideres"),
            dbc.DropdownMenuItem("Población de acuerdo con que la mitad de los miembros del parlamento sean mujeres", href="/gender_roles_spanish/equidad-parlamento"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ámbito laboral", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “ante la escasez de empleo, los hombres deberían tener más derecho a un empleo que las mujeres”", href="/gender_roles_spanish/derecho-empleo"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “los hombres son mejores empresarios que las mujeres”", href="/gender_roles_spanish/empresarios"),
            dbc.DropdownMenuItem("Población adulta que opina que los empresarios no contratan a mujeres con niños", href="/gender_roles_spanish/empleador-nocontrata-madres"),
            dbc.DropdownMenuItem("Población adulta que opina que un equipo de trabajo formado por hombres y mujeres logra mejores resultados que un equipo formado solo por hombres", href="/gender_roles_spanish/equipo-balance"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ámbito educativo", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “la educación universitaria es más importante para un varón que para una mujer”", href="/gender_roles_spanish/universidad"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “las mujeres tienen las mismas capacidades que los hombres para la ciencia y la tecnología”", href="/gender_roles_spanish/capacidad-ciencia"),
            dbc.DropdownMenuItem("Docentes de 3er grado que opinan que niños o niñas aprenden más rápido matemática o lengua debido a características innatas", href="/gender_roles_spanish/aprenden-rapido-3ro"),
            dbc.DropdownMenuItem("Docentes de 6to grado que opinan que niños o niñas aprenden más rápido matemática, lengua o ciencias debido a características innatas", href="/gender_roles_spanish/aprenden-rapido-6to"),
            dbc.DropdownMenuItem("Porcentaje de alumnos de 15 años que espera trabajar en ocupaciones relacionadas a STEM a los 30 años", href="/gender_roles_spanish/stem-15"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ámbito familiar", header=True),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “si una mujer gana más dinero que su marido, es casi seguro que causará problemas”", href="/gender_roles_spanish/mujer-gana-mas"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “cuando una madre trabaja, sus hijos sufren”", href="/gender_roles_spanish/madre-trabaja"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “ser ama de casa es tan gratificante como tener un trabajo remunerado”", href="/gender_roles_spanish/ama-de-casa"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “las mujeres deben trabajar sólo si la pareja no gana suficiente”", href="/gender_roles_spanish/mujer-trabaja-pareja"),
            dbc.DropdownMenuItem("Población adulta de acuerdo con la frase “es mejor que la mujer se concentre en el hogar y el hombre en el trabajo”", href="/gender_roles_spanish/mujer-casa-hombre-trabajo"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que piensan que está justificado que los maridos golpeen a sus esposas en algunas situaciones", href="/gender_roles_spanish/justifica-golpear"),
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


navbar_gender_roles_spanish = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_gender_roles_spanish", n_clicks=0),
                        dbc.Collapse(
                            dropdown_gender_roles_spanish, 
                            className="ml-auto",
                            id="navbar-collapse_gender_roles_spanish",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/gender_roles_spanish/hombres-mejores-lideres",
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
        id="all-pages-dropdown-pais-gender-roles-spanish",
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
                2019:'2019',2020:'2020',2021:'2021'}

ranger_slider_year_gender_roles_spanish = dcc.RangeSlider(
        min=2000,
        max=2021,
        value=[2000,2021],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-gender-roles-spanish"
)
