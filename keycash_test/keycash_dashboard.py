#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from google.cloud import bigquery
import dash
import dash_core_components as dcc
from dash import html


# In[5]:


client = bigquery.Client.from_service_account_json("key.json")


# In[6]:


df = client.query("SELECT * FROM `keycashtest.keycash_dataset.CREDIT_PER_DAY`").    result().    to_dataframe()

df = df.sort_values(by = 'day')


# In[7]:


#sns.lineplot(data = df, x = 'day', y = 'soma_credito')
app = dash.Dash(__name__)


# In[9]:


app.layout = html.Div(
    children=[
        html.H1(children="Soma de Crédito por Dia",),
        html.P(
            children="Algumas análises relacionadas a soma de crédito por dia. As informações são coletadas de um DataWarehouse no GCP e mostradas nesse dashboard",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df["day"],
                        "y": df["soma_credito"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Soma de Crédito por Dia - Linhas"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": df["day"],
                        "y": df["soma_credito"],
                        "type": "bars",
                    },
                ],
                "layout": {"title": "Soma de Crédito por Dia - Barras"},
            },
        ),
    ]
)


# In[12]:


if __name__ == "__main__":
    app.run_server(debug=True)



