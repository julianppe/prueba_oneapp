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
)