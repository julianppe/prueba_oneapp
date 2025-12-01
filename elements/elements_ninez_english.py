from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_ninez_english = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Schooling", header=True),
            dbc.DropdownMenuItem("Pre-primary enrollment rate (5 Year old)", href="/ninez_english/enrollment-rate-pre-primary-5"),
            dbc.DropdownMenuItem("Pre-primary enrollment rate (3-5 Year old)", href="/ninez_english/enrollment-rate-pre-primary-35"),
            dbc.DropdownMenuItem("Primary net enrollment rate", href="/ninez_english/net-enrollment-primary"),
            dbc.DropdownMenuItem("Secondary net enrollment rate", href="/ninez_english/net-enrollment-secondary"),
            dbc.DropdownMenuItem("Tertiary net enrollment rate", href="/ninez_english/net-enrollment-tertiary"),
            dbc.DropdownMenuItem("Primary completion rate", href="/ninez_english/primary-completion-rate"),
            dbc.DropdownMenuItem("Secondary completion rate", href="/ninez_english/secondary-completion-rate"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Activities and time use", header=True),
            dbc.DropdownMenuItem("Participation in care activities", href="/ninez_english/participation-care-activities"),
            dbc.DropdownMenuItem("Weekly hours allocated to care activities", href="/ninez_english/hours-care-activities"),
            dbc.DropdownMenuItem("Participation in childcare activities", href="/ninez_english/participation-childcare-activities"),
            dbc.DropdownMenuItem("Weekly hours allocated to childcare activities", href="/ninez_english/hours-childcare-activities"),
            dbc.DropdownMenuItem("Youth neither in school nor economically active", href="/ninez_english/youth-neither-school-active"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Test Scores", header=True),
            dbc.DropdownMenuItem("Average score in standardized tests for 3rd grade students", href="/ninez_english/score-3rd"),
            dbc.DropdownMenuItem("Average score in standardized tests for 6th grade students", href="/ninez_english/score-6th"),
            dbc.DropdownMenuItem("Average score in standardized tests for 15 year-old students", href="/ninez_english/score-15"),
            dbc.DropdownMenuItem("Ratio of standardized tests scores for 3rd grade students", href="/ninez_english/ratio-3rd-english"),
            dbc.DropdownMenuItem("Ratio of standardized tests scores for 6th grade students", href="/ninez_english/ratio-6th-english"),
            dbc.DropdownMenuItem("Ratio of standardized tests scores for 15 year-old students", href="/ninez_english/ratio-15-english"),
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores in 3rd grade", href="/ninez_english/women-10-low-3rd"),
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores in 6th grade", href="/ninez_english/women-10-low-6th"),
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores for 15 year-old students", href="/ninez_english/women-10-low-15"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores in 3rd grade", href="/ninez_english/women-10-high-3rd"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores in 6th grade", href="/ninez_english/women-10-high-6th"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores for 15 year-old students", href="/ninez_english/women-10-high-15"),
            dbc.DropdownMenuItem("Percentage of women among 15 year-old functionally-illiterate students", href="/ninez_english/women-illiterate-functionally"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Non-cognitive abilities", header=True),
            dbc.DropdownMenuItem("Sixth grade students responding yes to 'I follow class rules and regulations.'", href="/ninez_english/follow-rules-6th"),
            dbc.DropdownMenuItem("Sixth grade students responding yes to 'I ask the teacher for help when I don't understand what to do.'", href="/ninez_english/ask-for-help-6th"),
            dbc.DropdownMenuItem("Sixth grade students responding yes to 'Before turning in an assignment or test I check it well.'", href="/ninez_english/double-check-6th"),
            dbc.DropdownMenuItem("Sixth grade students responding yes to 'I wait my turn to speak in class.'", href="/ninez_english/wait-to-speak-6th"),
            dbc.DropdownMenuItem("Sixth grade students responding yes to 'Even if things don't work out for me, I keep trying'.", href="/ninez_english/keep-trying-6th"),
            dbc.DropdownMenuItem("Self-regulation index for 6th grade students", href="/ninez_english/hse-index-6th"),
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


navbar_ninez_english = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_ninez_english", n_clicks=0),
                        dbc.Collapse(
                            dropdown_ninez_english, 
                            className="ml-auto",
                            id="navbar-collapse_ninez_english",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/ninez_english/enrollment-rate-pre-primary-5",
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
        id="all-pages-dropdown-pais-ninez-english",
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

ranger_slider_year_ninez_english = dcc.RangeSlider(
        min=2000,
        max=2024,
        value=[2000,2024],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-ninez-english"
)
