from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Create a presentation
prs = Presentation()
slide_layout = prs.slide_layouts[5]  # Blank layout
slide = prs.slides.add_slide(slide_layout)

# Define positions
left_positions = [0.2, 2.5, 5.0, 7.5, 10.0, 12.5]
top = 2

# Define personas and lifecycle stages
personas = [
    ("Data Engineer", "Prepares Data\n(SM Data Wrangler, Feature Store)"),
    ("Data Scientist", "Builds Models\n(SM Studio, Experiments, Clarify)"),
    ("ML Engineer", "Trains & Deploys\n(SM Pipelines, Endpoints, Registry)"),
    ("IT Admin", "Secures & Monitors\n(IAM, VPC, CloudWatch, Model Monitor)"),
    ("Business Analyst", "Consumes Insights\n(SM Canvas, Autopilot)")
]

# Title
title_shape = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12), Inches(1))
title_tf = title_shape.text_frame
title_run = title_tf.paragraphs[0].add_run()
title_run.text = "AWS SageMaker Personas Across ML Lifecycle"
title_run.font.size = Pt(32)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(0, 51, 102)

# Add persona boxes
for idx, (persona, desc) in enumerate(personas):
    left = Inches(0.5 + idx * 2.5)
    width = Inches(2.3)
    height = Inches(2)
    shape = slide.shapes.add_shape(
        1, left, Inches(top), width, height  # Rectangle
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(224, 235, 255)
    shape.line.color.rgb = RGBColor(0, 51, 102)

    # Add text inside
    tf = shape.text_frame
    p1 = tf.add_paragraph()
    p1.text = persona
    p1.font.bold = True
    p1.font.size = Pt(18)
    p1.font.color.rgb = RGBColor(0, 51, 102)

    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(12)
    p2.font.color.rgb = RGBColor(0, 0, 0)

# Save PPTX
file_path = "C:\\Arunangsu\\sagemaker_personas_lifecycle.pptx"
prs.save(file_path)
file_path
