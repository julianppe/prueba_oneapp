from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_gender_roles_english = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Political", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Men make better political leaders than women do”", href="/gender_roles_english/men-better-political"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Half of Parliament members are women”", href="/gender_roles_english/half-parliament"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Labor", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “When jobs are scarce, men should have more right to a job than women”", href="/gender_roles_english/right-job"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Men make better business executives than women do”", href="/gender_roles_english/executives"),
            dbc.DropdownMenuItem("Adult population that thinks that employers do not hire women with children", href="/gender_roles_english/employers-donot-mothers"),
            dbc.DropdownMenuItem("Adult population that thinks that a team composed of men and women achieves better outcomes than a team composed of only men", href="/gender_roles_english/balance-team"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Education", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “A university education is more important for a boy than for a girl”", href="/gender_roles_english/university"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “women have the same capabilities for science and technology as men”", href="/gender_roles_english/science-capabilities"),
            dbc.DropdownMenuItem("Third-grade teachers who think that boys or girls learn faster math or language due to their innate characteristics", href="/gender_roles_english/learn-faster-3rd"),
            dbc.DropdownMenuItem("Third-grade teachers who think that boys or girls learn faster math or language due to their innate characteristics", href="/gender_roles_english/learn-faster-3rd-innate"),
            dbc.DropdownMenuItem("Sixth-grade teachers who think that boys or girls learn faster math, language or science due to their innate characteristics", href="/gender_roles_english/learn-faster-6th"),
            dbc.DropdownMenuItem("Percentage of 15 year-old students who expect to work in STEM-related occupations at the age of 30", href="/gender_roles_english/stem-15-english"),
            dbc.DropdownMenuItem("Percentage of 15 year-old students who expect to work in STEM-related occupations at the age of 30", href="/gender_roles_english/stem-15-english-innate"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Family", header=True),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “If a woman earns more money than her husband, it’s almost certain to cause problems”", href="/gender_roles_english/woman-earns-more"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “When a mother works for pay, the children suffer”", href="/gender_roles_english/mother-works"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Being a housewife is just as fulfilling as working for pay”", href="/gender_roles_english/housewife"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “Women have to work for pay only if their husband does not earn enough”", href="/gender_roles_english/woman-work-husband"),
            dbc.DropdownMenuItem("Adult population agreeing with the statement “It is better if man works and woman stays at home”", href="/gender_roles_english/woman-stays-man-work"),
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


navbar_gender_roles_english = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_gender_roles_english", n_clicks=0),
                        dbc.Collapse(
                            dropdown_gender_roles_english, 
                            className="ml-auto",
                            id="navbar-collapse_gender_roles_english",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/gender_roles_english/men-better-political",
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
        id="all-pages-dropdown-pais-gender-roles-english",
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

ranger_slider_year_gender_roles_english = dcc.RangeSlider(
        min=2000,
        max=2023,
        value=[2000,2023],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-gender-roles-english"
)
