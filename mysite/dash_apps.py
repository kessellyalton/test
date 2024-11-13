# myapp/dash_apps.py

from django_plotly_dash import DjangoDash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E", "F"],
    "Values1": [10, 20, 30, 40, 50, 60],
    "Values2": [15, 25, 35, 45, 55, 65],
})

# Initialize the Dash app
app = DjangoDash("DynamicDashboard")

# Define the layout
app.layout = html.Div(
    children=[
        html.H2("Interactive Dashboard with 2 Inputs and 3 Outputs"),

        # Row 1 with 6 columns for inputs
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label("Select X-Axis Value:"),
                        dcc.Dropdown(
                            id="x-axis-dropdown",
                            options=[{"label": col, "value": col} for col in df.columns],
                            value="Category"
                        )
                    ],
                    className="col-6"
                ),
                html.Div(
                    children=[
                        html.Label("Select Y-Axis Value:"),
                        dcc.Dropdown(
                            id="y-axis-dropdown",
                            options=[{"label": col, "value": col} for col in ["Values1", "Values2"]],
                            value="Values1"
                        )
                    ],
                    className="col-6"
                )
            ],
            className="row"
        ),

        # Row 2 with 6 columns for graphs
        html.Div(
            children=[
                html.Div(dcc.Graph(id="bar-chart"), className="col-4"),
                html.Div(dcc.Graph(id="scatter-plot"), className="col-4"),
                html.Div(dcc.Graph(id="line-chart"), className="col-4")
            ],
            className="row"
        )
    ],
    style={"width": "100%"}
)

# Define callback for interactive graph updates
@app.callback(
    [Output("bar-chart", "figure"), Output("scatter-plot", "figure"), Output("line-chart", "figure")],
    [Input("x-axis-dropdown", "value"), Input("y-axis-dropdown", "value")]
)
def update_graphs(x_axis, y_axis):
    # Bar chart
    bar_chart = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart of {y_axis} by {x_axis}")

    # Scatter plot
    scatter_plot = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot of {y_axis} vs {x_axis}")

    # Line chart
    line_chart = px.line(df, x=x_axis, y=y_axis, title=f"Line Chart of {y_axis} by {x_axis}")

    return bar_chart, scatter_plot, line_chart
