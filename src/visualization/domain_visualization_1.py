from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Create a new presentation
prs = Presentation()

# Define slide layout (Title and Content)
slide_layout = prs.slide_layouts[5]  # blank slide
slide = prs.slides.add_slide(slide_layout)

# Title box
title_box = slide.shapes.add_textbox(Inches(1), Inches(0.2), Inches(8), Inches(1))
title_tf = title_box.text_frame
title_run = title_tf.paragraphs[0].add_run()
title_run.text = "Amazon SageMaker Domain Alignment with MLOps Lifecycle"
title_run.font.size = Pt(28)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(0, 51, 102)

# Core Domain box
domain_box = slide.shapes.add_shape(
    1, Inches(3), Inches(1.2), Inches(4), Inches(1.2)  # Rectangle
)
domain_box.text = "SageMaker Domain\n- User Profiles\n- Networking (VPC)\n- IAM & SSO\n- Central Storage\n- Governance & Audit"
domain_box.text_frame.paragraphs[0].font.size = Pt(14)

# Arrows and stage boxes
stages = [
    ("Data Management", "- S3, Feature Store\n- Data Wrangler\n- Lineage Tracking", RGBColor(102, 204, 255)),
    ("Experimentation & Training", "- Studio IDEs\n- Experiments Tracking\n- Distributed Training", RGBColor(153, 204, 255)),
    ("Model Registry & Governance", "- Model Registry\n- Lineage Tracking\n- Approval Workflows", RGBColor(204, 229, 255)),
    ("Deployment & Inference", "- Endpoint Hosting\n- Multi-model/Container\n- CI/CD Integration", RGBColor(255, 229, 204)),
    ("Monitoring & Feedback", "- Model Monitor\n- CloudWatch Metrics\n- Retraining Triggers", RGBColor(255, 204, 204)),
]

left = 0.5
top = 3
for i, (title, content, color) in enumerate(stages):
    box = slide.shapes.add_shape(1, Inches(left), Inches(top), Inches(3), Inches(1.2))
    box.text = f"{title}\n{content}"
    # Fill color
    fill = box.fill
    fill.solid()
    fill.fore_color.rgb = color
    # Font size
    for p in box.text_frame.paragraphs:
        for run in p.runs:
            run.font.size = Pt(12)
    left += 3.5
    if left > 8:
        left = 0.5
        top += 1.5

# Save file
file_path = "/mnt/data/sagemaker_domain_mlopslifecycle.pptx"
prs.save(file_path)

file_path
