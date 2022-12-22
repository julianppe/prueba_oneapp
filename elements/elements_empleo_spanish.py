from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

dropdown_empleo_spanish = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Empleo y calificación", header=True),
            dbc.DropdownMenuItem("Tasa de participación laboral", href="/empleo_spanish/participacion-laboral"),
            dbc.DropdownMenuItem("Tasa de empleo", href="/empleo_spanish/tasa-de-empleo"),
            dbc.DropdownMenuItem("Tasa de desempleo", href="/empleo_spanish/tasa-de-desempleo"),
            dbc.DropdownMenuItem("Tasa de informalidad laboral", href="/empleo_spanish/tasa-de-informalidad-laboral"),
            dbc.DropdownMenuItem("Horas semanales en trabajo remunerado", href="/empleo_spanish/horas-de-trabajo"),
            dbc.DropdownMenuItem("Empleadores", href="/empleo_spanish/empleador"),
            dbc.DropdownMenuItem("Asalariados", href="/empleo_spanish/asalariados"),
            dbc.DropdownMenuItem("Cuentapropista", href="/empleo_spanish/cuentapropista"),
            dbc.DropdownMenuItem("No remunerado", href="/empleo_spanish/no-remunerado"),
            dbc.DropdownMenuItem("Managers", href="/empleo_spanish/managers"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Ingresos", header=True),
            dbc.DropdownMenuItem("Salario horario promedio", href="/empleo_spanish/salario-horario"),
            dbc.DropdownMenuItem("Ingreso laboral mensual", href="/empleo_spanish/ingreso-laboral"),
            dbc.DropdownMenuItem("Brecha salarial por género condicionada", href="/empleo_spanish/brecha-salarial-genero"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Calificación de la población adulta", header=True),
            dbc.DropdownMenuItem("Años de educación", href="/empleo_spanish/anios-educacion"),
            dbc.DropdownMenuItem("Porcentaje de adultos con calificación alta", href="/empleo_spanish/adultos-con-alta-calificacion"),
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

navbar_empleo_spanish = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler_empleo_spanish", n_clicks=0),
                        dbc.Collapse(
                            dropdown_empleo_spanish, 
                            className="ml-auto",
                            id="navbar-collapse_empleo_spanish",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/empleo_spanish/participacion-laboral",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
    expand=True,
)
