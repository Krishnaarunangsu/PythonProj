import matplotlib.pyplot as plt

# Create a figure
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis("off")

# Title
plt.text(0.5, 1.05, "Amazon SageMaker Domain Alignment with MLOps Lifecycle",
         fontsize=18, fontweight="bold", ha="center", color="#003366")

# Draw SageMaker Domain box
domain_box = plt.Rectangle((0.35, 0.8), 0.3, 0.12, fc="#cce6ff", ec="black")
ax.add_patch(domain_box)
plt.text(0.5, 0.86, "SageMaker Domain", fontsize=14, ha="center", fontweight="bold")
plt.text(0.5, 0.82,
         "- User Profiles\n- Networking (VPC)\n- IAM & SSO\n- Storage (EFS, S3)\n- Governance & Audit",
         fontsize=10, ha="center", va="top")

# Stages definitions
stages = [
    ("Data Management", "- S3, Feature Store\n- Data Wrangler\n- Lineage Tracking", "#66ccff"),
    ("Experimentation & Training", "- Studio IDEs\n- Experiments\n- Distributed Training", "#99ccff"),
    ("Model Registry & Governance", "- Model Registry\n- Lineage\n- Approval Workflows", "#cce6ff"),
    ("Deployment & Inference", "- Endpoint Hosting\n- Multi-model\n- CI/CD Integration", "#ffe6cc"),
    ("Monitoring & Feedback", "- Model Monitor\n- CloudWatch\n- Retraining Triggers", "#ffcccc"),
]

# Plot stage boxes horizontally
x_positions = [0.05, 0.25, 0.45, 0.65, 0.85]
y_position = 0.45

for (title, content, color), x in zip(stages, x_positions):
    box = plt.Rectangle((x, y_position), 0.18, 0.18, fc=color, ec="black")
    ax.add_patch(box)
    plt.text(x+0.09, y_position+0.14, title, fontsize=11, ha="center", fontweight="bold")
    plt.text(x+0.09, y_position+0.02, content, fontsize=9, ha="center", va="top")

# Save PNG
png_path = "/mnt/data/sagemaker_domain_mlopslifecycle.png"
plt.savefig(png_path, bbox_inches="tight")
plt.close()

png_path
