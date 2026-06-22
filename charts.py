# Import Plotly Express for creating interactive charts
import plotly.express as px


# Create a bar chart using selected X and Y columns
def create_bar_chart(df, x, y):

    # Generate bar chart
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=f"{y} by {x}",
        color=y,
        color_continuous_scale="Blues"
    )

    # Customize chart layout
    fig.update_layout(
        height=500,
        title_x=0.5  # Center-align title
    )

    return fig


# Create a line chart to show trends in the data
def create_line_chart(df, x, y):

    # Generate line chart with markers
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=f"{y} Trend"
    )

    # Customize line and marker appearance
    fig.update_traces(
        line=dict(color="#1f77b4", width=4),
        marker=dict(color="#ff7f0e", size=8)
    )

    # Customize chart layout
    fig.update_layout(
        height=500,
        title_x=0.5  # Center-align title
    )

    return fig


# Create a pie chart for categorical data distribution
def create_pie_chart(df, col):

    # Count occurrences of each category
    pie = df[col].value_counts().reset_index()

    # Rename columns
    pie.columns = [col, "Count"]

    # Generate pie chart
    fig = px.pie(
        pie,
        names=col,
        values="Count",
        title=f"{col} Distribution",
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    return fig