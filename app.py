import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

fig1 = go.Figure(go.Venn(
    subsets=[set(depressed.index), set(anxious.index), set(panicking.index)],
    set_labels=("Depressed", "Anxious", "Having Panic Attacks"),
    set_colors=("orange", "purple", "green"),
    opacity=0.9
))
fig1.update_layout(title="Conditions")

fig2 = go.Figure()

for gender, gender_count in gender_counts.items():
    fig2.add_trace(go.Bar(
        x=labels,
        y=gender_count,
        name=gender,
        marker_color=colors,
        text=gender_count,
        textposition='auto',
    ))

fig2.update_layout(title="Condition by Gender", xaxis=dict(tickangle=20), barmode='stack')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Your Visualizations'),

    html.Div(children=[
        dcc.Graph(
            id='venn-diagram',
            figure=fig1
        ),
        dcc.Graph(
            id='bar-chart',
            figure=fig2
        )
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)
