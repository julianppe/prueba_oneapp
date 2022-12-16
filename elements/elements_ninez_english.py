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
            dbc.DropdownMenuItem("Percentage of women among the bottom 10% test scores for 15 year-old students", href="/ninez_english/women-high-10-15"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores in 3rd grade", href="/ninez_english/women-10-high-3rd"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores in 6th grade", href="/ninez_english/women-10-high-6th"),
            dbc.DropdownMenuItem("Percentage of women among the top 10% test scores for 15 year-old students", href="/ninez_english/women-10-high-15"),
            dbc.DropdownMenuItem("Percentage of women among 15 year-old functionally-illiterate students", href="/ninez_english/women-illiterate-functionally"),
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
                href="/ninez_english/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)