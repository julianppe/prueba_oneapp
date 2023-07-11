from dash import dcc
import pandas as pd

df = pd.read_csv("datasets/empleo_spanish/participacion.csv")
df['pais'] = df['pais'].astype(str)
app_spanning_input = dcc.Dropdown(
    options=['Argentina','Bolivia', 'Brasil'],
    id="all-pages-pais",
    multi=True, 
    value="Argentina", 
    className="bg-light",
    persistence=True,
    persistence_type = 'memory',
)
