import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html, register_page, no_update
from dash_extensions.enrich import Output, Input, State, callback

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/diferencia-edad',  # '/' is home page and it represents the url
                   name='Diferencia de edad entre conyuges',  # name of page, commonly used as name of link
                   title='Diferencia de edad entre conyuges',  # title that appears on browser's tab
                   #image='pg1.png',  # image in the assets folder
                   #description='Histograms are the new bar charts.'
)

# page 1 data
#df = pd.read_csv("https://raw.githubusercontent.com/julianppe/data/main/participacion.csv")
df = pd.read_csv("datasets/diferencia_edad.csv")
df['indicador'] = df['indicador'].astype(str)
df['pais'] = df['pais'].astype(str)
df['comparacion_por'] = df['comparacion_por'].astype(str)
df['ano'] = df['ano'].astype(int)

df['valor'] = df['valor'].round(decimals = 2)
# Armar loop:
mark_values = {2000:'2000',2001:'2001',2002:'2002',
                2003:'2003',2004:'2004',2005:'2005',
                2006:'2006',2007:'2007',2008:'2008',
                2009:'2009',2010:'2010',2011:'2011',
                2012:'2012',2015:'2015',2016:'2016',
                2013:'2013',2014:'2014',2015:'2015',
                2016:'2016',2017:'2017',2018:'2018',
                2019:'2019',2020:'2020',2021:'2021'}

# Para ordenar dropdown:
list_comparacion_por = list(df['comparacion_por'].unique())
list_comparacion_por_orden = list(df['comparacion_por_orden'].unique())
list_comparacion_por_ordenada = [x for _,x in sorted(zip(list_comparacion_por_orden,list_comparacion_por))]

layout = html.Div(
    [
        dbc.Row([
        dbc.Col([
            dcc.Dropdown(options=[{'label': x, 'value': x} for x in df.pais.unique()], multi=True, className="bg-light", id='page1_familia_spanish-pais_elect')
        ], width=6),
        dbc.Col([
            dcc.Dropdown(options=[{'label': x, 'value': x} for x in list_comparacion_por_ordenada], multi=False, className="bg-light", persistence=True, persistence_type='memory', value='Total', id='page1_familia_spanish-comparacion_por_elect')
        ], width=6),
    ]),
        dbc.Row([
        dbc.Col([
            dcc.Graph(id='page1_familia_spanish-line', config={'displayModeBar':False})
        ], width=12),
    ]),
        dbc.Row([
        dbc.Col([
        dcc.RangeSlider(id='page1_familia_spanish-the_year',
                min=2000,
                max=2021,
                value=[2000,2021],
                marks=mark_values,
                step=1,
                persistence=True,
                persistence_type='memory')
        ], width=12),
    ])
])

@callback(
    Output('page1_familia_spanish-pais_elect', 'value'),
    Output("store", "data"),
    Input('page1_familia_spanish-pais_elect', 'value'),
    State("store", "data"),
)

def sync_dropdowns(dd_pais, store_pais):
    if dd_pais is None:
        return store_pais, no_update
    return dd_pais, dd_pais

@callback(
    Output('page1_familia_spanish-line', 'figure'),
    Input('page1_familia_spanish-pais_elect', 'value'),
    Input('page1_familia_spanish-comparacion_por_elect', 'value'),
    [Input('page1_familia_spanish-the_year','value')]
)

def update_graphs(pais_v, comparacion_por_v, years_chosen):
    dff = df.copy() # Copiamos la base original.
    # Slider range de años:
    dff = dff[(dff['ano']>=years_chosen[0])&(dff['ano']<=years_chosen[1])]
    # Dropdown de pais:
    if type(pais_v) == str:
        pais_v = [pais_v]
    dff = dff[dff['pais'].isin(pais_v)]
    # Dropdown de comparación:
    dff = dff.query(f"comparacion_por == '{comparacion_por_v}'")
    # Seleccion de indicador, detalle indicador y disclaimer.
    indicador = dff['indicador'].iat[0]
    detalle_indicador_v = dff['detalle_indicador'].iat[0]
    disclaimer = dff['disclaimer'].iat[0]
    # Grafico con IC:
    if comparacion_por_v == 'Brecha mujeres - hombres':
        fig_line = px.line(dff, x='ano', y='valor', color='pais2', error_y='valor_errorestandar',
        symbol= 'desagregacion',
        labels=dict(ano="Año", valor="", pais2="País", indicador="Indicador", desagregacion="Desagregación")).update_xaxes(type='category').update_layout(margin=dict(l=10, r=10, t=10, b=10))
    else:
        fig_line = px.line(dff, x='ano', y='valor', color='pais2',
        line_dash= 'desagregacion', symbol= 'desagregacion',
        labels=dict(ano="Año", valor="", pais2="País", indicador="Indicador", desagregacion="Desagregación")).update_xaxes(type='category').update_layout(margin=dict(l=10, r=10, t=10, b=10))
    fig_line.update_traces(line=dict(width=2), 
        marker={'size': 10})
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