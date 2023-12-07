from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_familia_english = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Gaps between spouses", header=True),
            dbc.DropdownMenuItem("Age difference between spouses", href="/familia_english/age-difference"),
            dbc.DropdownMenuItem("Education difference between spouses", href="/familia_english/educational-difference"),
            dbc.DropdownMenuItem("Difference in hours worked between spouses", href="/familia_english/hours-difference"),
            dbc.DropdownMenuItem("Percentage of the spousal labor income contributed by each member", href="/familia_english/labor-income-percentage"),
            dbc.DropdownMenuItem("Percentage of individuals with equal or greater education than spouse who are inactive", href="/familia_english/more-education-percentage"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Autonomía", header=True),
            dbc.DropdownMenuItem("Percentage of adults with zero income", href="/familia_english/autonomy"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Household structure and headship", header=True),
            dbc.DropdownMenuItem("Self-reported female household headship", href="/familia_english/female-household-headship"),
            dbc.DropdownMenuItem("Economic female household headship", href="/familia_english/female-household-headship-econ"),
            dbc.DropdownMenuItem("Percentage of single-parent households", href="/familia_english/single-parent-percentage"),
            dbc.DropdownMenuItem("Early marriage", href="/familia_english/early-marriage"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Time use", header=True),
            dbc.DropdownMenuItem("Participation in household chores", href="/familia_english/household-chores-family"),
            dbc.DropdownMenuItem("Weekly hours allocated to household chores", href="/familia_english/hours-household-chores-family"),
            dbc.DropdownMenuItem("Participation in care activities", href="/familia_english/care-activities-family"),
            dbc.DropdownMenuItem("Weekly hours allocated to care activities", href="/familia_english/hours-care-activities-family"),
            dbc.DropdownMenuItem("Participation in childcare activities", href="/familia_english/childcare-activities-family"),
            dbc.DropdownMenuItem("Weekly hours allocated to childcare activities", href="/familia_english/hours-childcare-activities-family"),
            dbc.DropdownMenuItem("Participation in activities of support to other households", href="/familia_english/activities-support-family"),
            dbc.DropdownMenuItem("Weekly hours allocated to provide support to other households", href="/familia_english/hours-activities-support-family"),
            dbc.DropdownMenuItem("Participation in leisure activities", href="/familia_english/activities-leisure-family"),
            dbc.DropdownMenuItem("Weekly hours allocated to leisure activities", href="/familia_english/hours-activities-leisure-family"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Fertility (DHS)", header=True),
            dbc.DropdownMenuItem("Number of children per woman", href="/familia_english/children-per-woman"),
            dbc.DropdownMenuItem("Total fertility rate", href="/familia_english/total-fertility-rate"),
            dbc.DropdownMenuItem("Desired fertility rate", href="/familia_english/desired-fertility-rate"),
            dbc.DropdownMenuItem("Gap between actual and desired fertility", href="/familia_english/gap-fertility-desired"),
            dbc.DropdownMenuItem("Gap in desired fertility between spouses", href="/familia_english/gap-fertility-desired-spouse"),
            dbc.DropdownMenuItem("Percentage of women using contraception (any method)", href="/familia_english/method-contraception"),
            dbc.DropdownMenuItem("Percentage of women using modern contraceptive methods", href="/familia_english/modern-contraception-method"),
            dbc.DropdownMenuItem("Percentage of women without access to contraception", href="/familia_english/without-contraception-access"),
            dbc.DropdownMenuItem("Early pregnancy", href="/familia_english/early-pregnancy"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Fertility (MICS)", header=True),
            dbc.DropdownMenuItem("Number of children per woman", href="/familia_english/children-per-woman-mics"),
            dbc.DropdownMenuItem("Total fertility rate", href="/familia_english/total-fertility-rate-mics"),
            dbc.DropdownMenuItem("Percentage of women using contraception (any method)", href="/familia_english/method-contraception-mics"),
            dbc.DropdownMenuItem("Percentage of women using modern contraceptive methods", href="/familia_english/modern-contraception-method-mics"),
            dbc.DropdownMenuItem("Percentage of women without access to contraception", href="/familia_english/without-contraception-access-mics"),
            dbc.DropdownMenuItem("Early pregnancy", href="/familia_english/early-pregnancy-mics"),
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


navbar_familia_english = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_familia_english", n_clicks=0),
                        dbc.Collapse(
                            dropdown_familia_english, 
                            className="ml-auto",
                            id="navbar-collapse_familia_english",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/familia_english/age-difference/",
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
        id="all-pages-dropdown-pais-familia-english",
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

ranger_slider_year_familia_english = dcc.RangeSlider(
        min=2000,
        max=2022,
        value=[2000,2022],
        marks=mark_values,
        step=1,
        persistence=True,
        persistence_type = 'memory',
        id="all-pages-ranger-slider-year-familia-english"
)
