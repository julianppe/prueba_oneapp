from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_gender_violence_spanish = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Violencia doméstica", header=True),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia psicologica por parte de su pareja", href="/gender_violence_spanish/violencia-psicologica-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia física doméstica", href="/gender_violence_spanish/violencia-fisica-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia sexual doméstica", href="/gender_violence_spanish/violencia-sexual-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado algún tipo de violencia doméstica", href="/gender_violence_spanish/violencia-domestica"),
            dbc.DropdownMenuItem("Porcentaje de la población que piensa que está justificado que los hombres golpeen a sus esposas", href="/gender_violence_spanish/justifica-golpear"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Violencia no doméstica", header=True),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han sufrido violencia física no domestica", href="/gender_violence_spanish/violencia-fisica-no-domestica"),
            dbc.DropdownMenuItem("Porcentaje de mujeres que han experimentado violencia sexual no doméstica", href="/gender_violence_spanish/violencia-sexual-no-domestica"),
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


navbar_gender_violence_spanish = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_gender_violence_spanish", n_clicks=0),
                        dbc.Collapse(
                            dropdown_gender_violence_spanish, 
                            className="ml-auto",
                            id="navbar-collapse_gender_violence_spanish",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/gender_violence_spanish/violencia-psicologica-domestica",
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
        value="Bolivia",
        id="all-pages-dropdown-pais-gender-violence-spanish",
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
                2022:'2022',2023:'2023'}

ranger_slider_year_gender_violence_spanish = dcc.RangeSlider(
        min=2000,
        max=2023,
        value=[2000,2023],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-gender-violence-spanish"
)
