from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_gender_violence_english = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Violencia doméstica", header=True),
            dbc.DropdownMenuItem("Percentage of women who have experienced psychological violence by a partner", href="/gender_violence_english/violence-psychological-domestic"),
            dbc.DropdownMenuItem("Percentage of women who have experienced physical violence by a partner", href="/gender_violence_english/violence-physical-domestic"),
            dbc.DropdownMenuItem("Percentage of women who have experienced sexual violence by their partner", href="/gender_violence_english/violence-sexual-domestic"),
            dbc.DropdownMenuItem("Percentage of women who have experienced some type of violence by a partner", href="/gender_violence_english/violence-domestic"),
            dbc.DropdownMenuItem("Percentage of the population agreeing it is justifiable for man to beat his wife", href="/gender_violence_english/justifiable-beat"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Violencia no doméstica", header=True),
            dbc.DropdownMenuItem("Percentage of women who have experienced physical violence by non-partners", href="/gender_violence_english/violence-physical-no-domestic"),
            dbc.DropdownMenuItem("Percentage of women who have experienced non-partner sexual violence", href="/gender_violence_english/violence-sexual-no-domestic"),
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


navbar_gender_violence_english = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_gender_violence_english", n_clicks=0),
                        dbc.Collapse(
                            dropdown_gender_violence_english, 
                            className="ml-auto",
                            id="navbar-collapse_gender_violence_english",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/gender_violence_english/violence-psychological-domestic",
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
        id="all-pages-dropdown-pais-gender-violence-english",
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
                2022:'2022',2023:'2023',2024:'2024'}

ranger_slider_year_gender_violence_english = dcc.RangeSlider(
        min=2000,
        max=2024,
        value=[2000,2024],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-gender-violence-english"
)
