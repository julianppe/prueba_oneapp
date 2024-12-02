import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from elements.elements_familia_spanish import ranger_slider_year_familia_spanish
from dash import dcc, html, register_page, ctx, no_update
from dash_extensions.enrich import Output, Input, State, callback
from elements.elements_familia_spanish import generate_dropdown
dash.register_page(__name__,
                   path='/hijos-por-mujer-mics',  # represents the url text
                   name='Número de hijos por mujer',  # name of page, commonly used as name of link
                   title='Número de hijos por mujer'  # epresents the title of browser's tab
)

# page 1 data
df = pd.read_csv("datasets/familia_spanish/numero_hijos_vivos_mics.csv")
df['indicador'] = df['indicador'].astype(str)
df['pais'] = df['pais'].astype(str)
df['comparacion_por'] = df['comparacion_por'].astype(str)
df['ano'] = df['ano'].astype(int)
df['valor'] = df['valor'].round(decimals = 2)

options = list(df['pais'].unique())
dropdown = generate_dropdown(options)

# Para ordenar dropdown:
list_comparacion_por = list(df['comparacion_por'].unique())
list_comparacion_por_orden = list(df['comparacion_por_orden'].unique())
list_comparacion_por_ordenada = [x for _,x in sorted(zip(list_comparacion_por_orden,list_comparacion_por))]

layout = html.Div([
        dbc.Row([
        dbc.Col([
            dropdown,
        ], width=6),
        dbc.Col([
            dcc.Dropdown(options=[{'label': x, 'value': x} for x in list_comparacion_por_ordenada], multi=False, persistence=True, persistence_type='memory', value='Mujeres', id='page29_familia_spanish-comparacion_por_elect')
        ], width=6),
    ]),
        dbc.Row([
        dbc.Col([
            dcc.Graph(id='page29_familia_spanish-line', config={'displayModeBar':False})
        ], width=12),
    ]),
        dbc.Row([
        dbc.Col([
            ranger_slider_year_familia_spanish,
        ], width=12),
    ]),
])



@callback(
    Output('page29_familia_spanish-line', 'figure'),
    Input('all-pages-dropdown-pais-familia-spanish', 'value'),
    Input('page29_familia_spanish-comparacion_por_elect', 'value'),
    [Input('all-pages-ranger-slider-year-familia-spanish','value')]
)


def update_graphs(pais_v, comparacion_por_v, years_chosen):
    dff = df.copy()
    print(years_chosen)
    dff=dff[(dff['ano']>=years_chosen[0])&(dff['ano']<=years_chosen[1])]
    if type(pais_v) == str:
        pais_v = [pais_v]
    dff = dff[dff['pais'].isin(pais_v)]
    dff = dff.query(f"comparacion_por == '{comparacion_por_v}'")
    indicador = dff['indicador'].iat[0]
    detalle_indicador_v = dff['detalle_indicador'].iat[0]
    disclaimer = dff['disclaimer'].iat[0]
    if comparacion_por_v == 'Brecha mujeres - hombres':
        fig_line = px.line(dff, x='ano', y='valor', color='pais', error_y='valor_errorestandar',
        symbol= 'desagregacion',
        labels=dict(ano="Año", valor="", pais="País", indicador="Indicador", desagregacion="Desagregación")).update_xaxes(type='category').update_layout(margin=dict(l=10, r=10, t=10, b=10))
    else:
        fig_line = px.bar(dff, x='ano', y='valor', color='pais', pattern_shape='desagregacion', barmode='group', pattern_shape_sequence=["", "x", "."], 
        labels=dict(ano="Año", valor="", pais="País", indicador="Indicador", desagregacion="Desagregación")).update_xaxes(type='category', categoryorder='category ascending').update_layout(margin=dict(l=10, r=10, t=10, b=10))
    fig_line.update_layout(
        xaxis=dict( 
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            gridcolor = 'rgb(230, 230, 230)',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            gridcolor = 'rgb(230, 230, 230)',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=25,
            r=25,
            t=65,
            b=120,
        ),
        legend=dict(orientation = "h", yanchor="bottom",y=-0.35,xanchor="left", x=0, font=dict(size= 12)),
        showlegend=True,
        plot_bgcolor='white',
        legend_title='',
    )

    annotations = []

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.10,
                                  xanchor='left', yanchor='bottom',
                                  text=indicador,
                                  font=dict(family='Arial',
                                            size=22,
                                            color='rgb(37,37,37)'),
                                  showarrow=False))
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.03,
                                  xanchor='left', yanchor='bottom',
                                  text=detalle_indicador_v,
                                  font=dict(family='Arial',
                                            size=15,
                                            color='rgb(37,37,37)'),
                                  showarrow=False))
    #Source
    annotations.append(dict(xref='paper', yref='paper', x=0.001, y=-0.40,
                                  xanchor='left', yanchor='bottom',
                                  text=disclaimer,
                                  font=dict(family='Arial',
                                            size=10,
                                            color='rgb(82, 82, 82)'),
                                  showarrow=False))

    fig_line.update_layout(annotations=annotations)
    return fig_line