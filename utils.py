from dash import dcc

app_spanning_input = dcc.Dropdown(
    options=[{'label': x, 'value': x} for x in df.pais.unique()],
    id="all-pages-pais",
    multi=True, 
    value="Argentina", 
    className="bg-light",
    persistence=True,
    persistence_type = 'memory',
)
