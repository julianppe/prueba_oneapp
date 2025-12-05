import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

from elements.elements_empleo_spanish import (
    dropdown_pais_empleo_spanish
)

from dash import register_page
from dash_extensions.enrich import Output, Input, State, callback


# ============================================================
# REGISTRO DE LA PÁGINA
# ============================================================

dash.register_page(
    __name__,
    path='/horas_trabajadas',  
    name='Efecto maternidad sobre horas trabajadas',  
    title='Efecto maternidad sobre horas trabajadas'
)

# ============================================================
# CARGA DE DATOS
# ============================================================

df = pd.read_csv("datasets/empleo_spanish/horas_trabajadas_mat.csv")

# Asegurar tipos correctos
df['indicador'] = df['indicador'].astype(str)
df['pais'] = df['pais'].astype(str)
df['comparacion_por'] = df['comparacion_por'].astype(str)
df['ano'] = df['ano'].astype(int)
df['gap'] = df['gap'].astype(float)

# Redondeo si querés (opcional)
df['gap'] = df['gap'].round(2)

# Para ordenar el dropdown
lista_comparacion_por = list(df['comparacion_por'].unique())
lista_orden = list(df['comparacion_por_orden'].unique())
lista_comparacion_por_ordenada = [
    x for _, x in sorted(zip(lista_orden, lista_comparacion_por))
]

# ============================================================
# LAYOUT
# ============================================================

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dropdown_pais_empleo_spanish,
        ], width=6),
        dbc.Col([
            dcc.Dropdown(
                options=[{'label': x, 'value': x} for x in lista_comparacion_por_ordenada],
                multi=False,
                persistence=True,
                persistence_type='memory',
                value=lista_comparacion_por_ordenada[0],
                id='page_maternidad_horas_trabajadas-comparacion_por'
            )
        ], width=6),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='page_maternidad_horas_trabajadas-line',
                config={'displayModeBar': False}
            )
        ], width=12),
    ]),
])

# ============================================================
# CALLBACK
# ============================================================

@callback(
    Output('page_maternidad_horas_trabajadas-line', 'figure'),
    Input('all-pages-dropdown-pais-empleo-spanish', 'value'),
    Input('page_maternidad_horas_trabajadas-comparacion_por', 'value')
)
def update_graph(pais_v, comparacion_por_v):

    dff = df.copy()

    # Aceptar 1 país o lista
    if isinstance(pais_v, str):
        pais_v = [pais_v]

    dff = dff[dff['pais'].isin(pais_v)]
    dff = dff.query("comparacion_por == @comparacion_por_v")

    # Tomar textos
    indicador_titulo = dff['indicador'].iat[0]
    detalle = dff['detalle_indicador'].iat[0]
    detalle_largo = (
    "Efectos del nacimiento del primer hijo (con intervalos de confianza al 95%) " 
    "estimados a partir de un estudio de eventos con pseudo-paneles a nivel de individuos.<br>"
    + "Cada punto representa el cambio porcentual en en las horas trabajadas semanales en el "
    "año indicado en relación con el año anterior al nacimiento (normalizado a cero), "
    "controlando por efectos fijos de cohorte y año."
    )
    disclaimer = dff['disclaimer'].iat[0]

    fig = px.line(
        dff,
        x='ano',
        y='gap',
        color='pais2',
        error_y=dff['boundH'] - dff['gap'],
        error_y_minus=dff['gap'] - dff['boundL'],
        line_dash='desagregacion',
        symbol='desagregacion',
        labels=dict(
            ano="Años desde el nacimiento",
            gap="",
            pais2="País",
            desagregacion="Desagregación"
        )
    )

    fig.update_xaxes(type='category')
    fig.update_traces(line=dict(width=2), marker={'size': 10})

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            gridcolor='rgb(230, 230, 230)',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')
        ),
        yaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            gridcolor='rgb(230, 230, 230)',
            tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')
        ),
        autosize=True,
        margin=dict(l=25, r=25, t=65, b=120),
        plot_bgcolor='white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.35,
            xanchor="left",
            x=0,
            font=dict(size=12),
        ),
        legend_title='',
    )

    # Anotaciones
    annotations = [
        dict(
            xref='paper', yref='paper', x=0.0, y=1.12,
            xanchor='left', yanchor='bottom',
            text=indicador_titulo,
            font=dict(family='Arial', size=22, color='rgb(37,37,37)'),
            showarrow=False
        ),
        dict(
            xref='paper', yref='paper', x=0.0, y=1.00,
            xanchor='left', yanchor='bottom',
            text=detalle_largo,
            align='left',
            font=dict(family='Arial', size=14, color='rgb(37,37,37)'),
            showarrow=False
        ),
        dict(
            xref='paper', yref='paper', x=0.001, y=-0.40,
            xanchor='left', yanchor='bottom',
            text=disclaimer,
            font=dict(family='Arial', size=10, color='rgb(82,82,82)'),
            showarrow=False
        )
    ]

    fig.update_layout(annotations=annotations)

    return fig
