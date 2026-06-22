# Import required libraries
import streamlit as st
import pandas as pd

# Import custom modules
from data_processor import *
from charts import *
from report_generator import *

# Configure Streamlit page settings
st.set_page_config(
    page_title="CSV Dashboard Generator",
    page_icon="📊",
    layout="wide"
)

# Display application title and caption
st.title("📊 CSV Dashboard Generator")
st.caption("Upload a CSV file and generate reports")

# Create columns to center the file uploader
l, c, r = st.columns([2, 3, 2])

# File upload section
with c:
    file = st.file_uploader(
        "Choose CSV File",
        type="csv"  # Accept only CSV files
    )

# Execute only when a file is uploaded
if file:

    # Read uploaded CSV file into DataFrame
    df = pd.read_csv(file)

    # Get dataset information
    rows, cols, missing = get_dataset_info(df)

    # Display dataset metrics
    a, b, c = st.columns(3)
    a.metric("📄 Rows", rows)
    b.metric("📊 Columns", cols)
    c.metric("⚠ Missing", missing)

    # Show first 10 rows of dataset
    with st.expander("📋 Dataset Preview"):
        st.dataframe(
            df.head(10),
            use_container_width=True
        )

    # Display summary statistics
    st.subheader("📈 Summary Statistics")
    st.dataframe(
        get_summary_statistics(df),
        use_container_width=True
    )

    # Get numerical columns
    num = df.select_dtypes(
        include="number"
    ).columns

    # Get categorical columns
    cat = df.select_dtypes(
        include="object"
    ).columns

    # Generate charts if numerical columns exist
    if len(num):

        # Select columns for X and Y axes
        x = st.selectbox("X Axis", df.columns)
        y = st.selectbox("Y Axis", num)

        # Create bar and line charts
        bar = create_bar_chart(df, x, y)
        line = create_line_chart(df, x, y)

        # Display charts side by side
        c1, c2 = st.columns(2)
        c1.plotly_chart(bar, use_container_width=True)
        c2.plotly_chart(line, use_container_width=True)

        # Initialize pie chart path
        pie_path = None

        # Create pie chart if categorical columns exist
        if len(cat):
            p = st.selectbox("Pie Category", cat)
            pie = create_pie_chart(df, p)

            # Display pie chart
            st.plotly_chart(
                pie,
                use_container_width=True
            )

            # Save pie chart as image
            pie.write_image(
                "pie.png",
                width=1200,
                height=800,
                scale=2
            )
            pie_path = "pie.png"

        # Save bar chart as image
        bar.write_image(
            "bar.png",
            width=1200,
            height=700,
            scale=2
        )

        # Save line chart as image
        line.write_image(
            "line.png",
            width=1200,
            height=700,
            scale=2
        )

        # Generate PDF report with charts
        pdf = create_pdf_report(
            df,
            "bar.png",
            "line.png",
            pie_path
        )

        # Display download button on the right side
        _, _, right = st.columns([4, 1, 2])

        with right:
            with open(pdf, "rb") as f:
                st.download_button(
                    "📄 Download Report",
                    f,
                    "dashboard_report.pdf"
                )