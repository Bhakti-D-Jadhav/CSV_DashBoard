# Import ReportLab components for creating PDF documents
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph,
    Spacer, Table, TableStyle,
    Image, PageBreak
)

# Import colors and predefined styles
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Import datetime to display report generation date
from datetime import datetime


# Create a PDF report containing dataset information and charts
def create_pdf_report(df, bar, line, pie=None):

    # Create a PDF document
    doc = SimpleDocTemplate("dashboard_report.pdf")

    # Load default text styles
    styles = getSampleStyleSheet()

    # List to store all PDF elements
    elements = []

    # Get dataset information
    rows, cols = df.shape
    missing = df.isnull().sum().sum()

    # Create report title table
    title = Table([["CSV DASHBOARD REPORT"]], [520])

    # Apply styling to the title
    title.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1),
         colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, -1),
         colors.white),
        ("ALIGN", (0, 0), (-1, -1),
         "CENTER")
    ]))

    # Create dataset overview table
    overview = Table([
        ["Rows", rows],
        ["Columns", cols],
        ["Missing Values", missing]
    ], [250, 250])

    # Apply styling to overview table
    overview.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1),
         colors.lightblue),
        ("GRID", (0, 0), (-1, -1),
         1, colors.grey)
    ]))

    # Create summary text
    summary = (
        f"• Rows: {rows}<br/>"
        f"• Columns: {cols}<br/>"
        f"• Missing Values: {missing}"
    )

    # Add elements to the PDF
    elements += [
        title,
        Spacer(1, 20),

        # Display report generation date
        Paragraph(
            f"Generated on: "
            f"{datetime.now():%d %B %Y}",
            styles["Normal"]
        ),

        Spacer(1, 15),

        # Add dataset overview section
        Paragraph(
            "Dataset Overview",
            styles["Heading2"]
        ),
        overview,

        Spacer(1, 15),

        # Add summary section
        Paragraph(
            "Summary",
            styles["Heading2"]
        ),
        Paragraph(
            summary,
            styles["BodyText"]
        ),

        Spacer(1, 20),

        # Add bar chart image
        
        Image(bar, 420, 220),

        Spacer(1, 15),

        # Add line chart image
        Image(line, 420, 220)
    ]

    # Add pie chart on a new page if available
    if pie:
        elements.append(PageBreak())
        elements.append(
            Image(
                pie,
                width=420,
                height=300
            )
        )

    # Build and save the PDF document
    doc.build(elements)

    # Return the generated PDF file name
    return "dashboard_report.pdf"