from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container
import pandas as pd

dropdown_empleo_english = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Employment and skills", header=True),
            dbc.DropdownMenuItem("Labor force participation rate", href="/empleo_english/labor-force-participation"),
            dbc.DropdownMenuItem("Employment rate", href="/empleo_english/employment-rate"),
            dbc.DropdownMenuItem("Unemployment rate", href="/empleo_english/unemployment-rate"),
            dbc.DropdownMenuItem("Labor informality rate", href="/empleo_english/informality-rate"),
            dbc.DropdownMenuItem("Weekly hours worked", href="/empleo_english/weekly-hours-worked"),
            dbc.DropdownMenuItem("Employers", href="/empleo_english/employers"),
            dbc.DropdownMenuItem("Wage earners", href="/empleo_english/wage-earners"),
            dbc.DropdownMenuItem("Self-employed", href="/empleo_english/self-employed"),
            dbc.DropdownMenuItem("Unpaid workers", href="/empleo_english/unpaid-workers"),
            dbc.DropdownMenuItem("Managers", href="/empleo_english/managers2"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Income", header=True),
            dbc.DropdownMenuItem("Average hourly wage", href="/empleo_english/average-hourly-wage"),
            dbc.DropdownMenuItem("Monthly labor income", href="/empleo_english/monthly-labor-income"),
            dbc.DropdownMenuItem("Gender wage gap (conditional)", href="/empleo_english/gender-wage-gap"),
            dbc.DropdownMenuItem("Percentage of adults with zero income", href="/empleo_english/autonomy"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Skills of the adult population", header=True),
            dbc.DropdownMenuItem("Years of education", href="/empleo_english/years-education"),
            dbc.DropdownMenuItem("Percentage of high-skilled adults", href="/empleo_english/high-skilled-adults"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicators",
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


navbar_empleo_english = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_empleo_english", n_clicks=0),
                        dbc.Collapse(
                            dropdown_empleo_english, 
                            className="ml-auto",
                            id="navbar-collapse_empleo_english",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/empleo_english/labor-force-participation",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
    expand=True,
)

df = pd.read_csv("datasets/empleo_english/participacion.csv")
df['indicador'] = df['indicador'].astype(str)
df['pais'] = df['pais'].astype(str)

dropdown_pais_empleo_english = dcc.Dropdown(
    options=[{'label': x, 'value': x} for x in df.pais.unique()],
    id="all-pages-dropdown-pais-empleo-english",
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
                2019:'2019',2020:'2020',2021:'2021',
                2022:'2022',2023:'2023'}

ranger_slider_year_empleo_english = dcc.RangeSlider(
        min=2000,
        max=2023,
        value=[2000,2023],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-empleo-english"
)