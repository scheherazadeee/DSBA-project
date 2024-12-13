from flask import Flask, render_template, jsonify
import plotly.express as px
import plotly.io as pio
import pandas as pd
import plotly.graph_objects as go
from fastapi import FastAPI
import streamlit as st
import streamlit.components.v1 as components



app = Flask(__name__)


# Load your dataset
df = pd.read_csv('/Users/macbookair/Desktop/python/project/modified_dataset1.csv')

charts_html = {}


@app.route('/')
def index():
    global charts_html

    # Generate the first Plotly chart for Sleep Efficiency Counts
    sleep_efficiency_counts = df['Sleep efficiency'].value_counts().sort_index()

    fig1 = px.line(
        sleep_efficiency_counts, 
        x=sleep_efficiency_counts.index, 
        y=sleep_efficiency_counts.values,
        title='Count of Each Sleep Efficiency Value',
        labels={'x': 'Sleep Efficiency', 'y': 'Count'},
        line_shape='spline',
        line_dash_sequence=['solid'],
    )

    fig1.update_traces(
        fill='tozeroy',
        fillcolor='rgba(255, 99, 71, 0.2)',
        line=dict(color='pink', width=2)
    )

    fig1.update_layout(
        xaxis_title='Sleep Efficiency',
        yaxis_title='Count',
        font={'size': 10, 'family': 'Arial', 'color': '#4d4d4d'}, 
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor='rgba(255, 255, 255, 0.8)',
            font_size=8,
            font_family='Arial',
            font_color='black'
        ),
        template='plotly_white',
        showlegend=False,
        margin=dict(l=50, r=50, b=50, t=70)
    )

    # Convert the figure to HTML to embed in the template
    graph_html1 = pio.to_html(fig1, full_html=False)

    
    good_lifestyle_avg = df.groupby('Good lifestyle')['Sleep efficiency'].mean()
    bad_lifestyle_avg = df.groupby('Bad lifestyle')['Sleep efficiency'].mean()

    x_labels = [1, 2, 3, 4, 5]
    good_lifestyle_values = good_lifestyle_avg.loc[x_labels].values
    bad_lifestyle_values = bad_lifestyle_avg.loc[x_labels].values

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=x_labels,
        y=good_lifestyle_values,
        mode='lines+markers',
        name='Good Lifestyle',
        line=dict(color='skyblue', width=2),
        marker=dict(symbol='circle', size=8)
    ))


    fig2.add_trace(go.Scatter(
        x=x_labels,
        y=bad_lifestyle_values,
        mode='lines+markers',
        name='Bad Lifestyle',
        line=dict(color='pink', width=2),
        marker=dict(symbol='square', size=8)
    ))


    fig2.update_layout(
        title="Comparison of Sleep Efficiency by Lifestyle (Good vs Bad)",
        xaxis_title="Lifestyle Level",
        yaxis_title="Average Sleep Efficiency",
        template="plotly_white",
        legend_title="Lifestyle Type",
        hovermode="closest",
        legend=dict(x=0.8, y=0.7),
        plot_bgcolor='white',
        showlegend=True
    )

    graph_html2 = pio.to_html(fig2, full_html=False)

    fig3 = go.Figure()

    fig3.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Good lifestyle'] == 1],
        name='Good Lifestyle 1',
        boxmean=True,
        marker_color='skyblue',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig3.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Good lifestyle'] == 2],
        name='Good Lifestyle 2',
        boxmean=True,
        marker_color='lightblue',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig3.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Good lifestyle'] == 3],
        name='Good Lifestyle 3',
        boxmean=True,
        marker_color='skyblue',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig3.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Good lifestyle'] == 4],
        name='Good Lifestyle 4',
        boxmean=True,
        marker_color='blue',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig3.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Good lifestyle'] == 5],
        name='Good Lifestyle 5',
        boxmean=True,
        marker_color='darkblue',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig3.update_layout(
        title="Good Lifestyle vs Sleep Efficiency",
        xaxis_title="Good Lifestyle Level",
        template='plotly_white',
        yaxis_title="Sleep Efficiency",
        showlegend=False,
        width=800,
        boxgap=0.3,
    )
    graph_html3 = pio.to_html(fig3, full_html=False)



    fig4 = go.Figure()

    fig4.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Bad lifestyle'] == 1],
        name='Bad Lifestyle 1',
        boxmean=True,
        marker_color='pink',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig4.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Bad lifestyle'] == 2],
        name='Bad Lifestyle 2',
        boxmean=True,
        marker_color='lightpink',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig4.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Bad lifestyle'] == 3],
        name='Bad Lifestyle 3',
        boxmean=True,
        marker_color='salmon',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig4.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Bad lifestyle'] == 4],
        name='Bad Lifestyle 4',
        boxmean=True,
        marker_color='red',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig4.add_trace(go.Box(
        y=df['Sleep efficiency'][df['Bad lifestyle'] == 5],
        name='Bad Lifestyle 5',
        boxmean=True,
        marker_color='darkred',
        boxpoints='all',
        jitter=0.05,
        width=0.4,
    ))

    fig4.update_layout(
        title="Bad Lifestyle vs Sleep Efficiency",
        template='plotly_white',
        xaxis_title="Bad Lifestyle Level",
        yaxis_title="Sleep Efficiency",
        showlegend=False,
        width=800,
        boxgap=0.3, 
    )
    
    graph_html4 = pio.to_html(fig4, full_html=False)


    available_columns = ['Sleep efficiency', 'Alcohol consumption', 'Smoking status', 'Exercise frequency', 'Bedtime', 'Wakeup time']

    # Dictionary to hold the HTML representations of the charts
    charts_html = {}

    # Loop through each column and generate a histogram chart
    for column in available_columns:
        fig = px.histogram(df, x=column, nbins=30,
                        title=f'Distribution of {column}',
                        labels={column: column},
                        color_discrete_sequence=["skyblue"])
        fig.update_layout(
            xaxis_title=column,
            yaxis_title='Count',
            template='plotly_white',
            hovermode="x unified",
            bargap=0.2,
            margin=dict(l=50, r=50, b=50, t=70)
        )
        # Convert the figure to HTML and store it in the dictionary
        charts_html[column] = pio.to_html(fig, full_html=False)
    return render_template('index.html', 
                            graph_html1=graph_html1,
                            graph_html2=graph_html2,
                            graph_html3=graph_html3,
                            graph_html4=graph_html4,
                            charts_html=charts_html, 
                            available_columns=available_columns)






if __name__ == "__main__":
    app.run(debug=True)

