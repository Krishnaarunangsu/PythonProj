import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define stages
stages = {
    "Stage 1\nAWS + ML Basics": [
        "IAM, S3, EC2, ECR, CloudWatch",
        "CloudFormation/Terraform",
        "ML Basics, Metrics, Model Packaging"
    ],
    "Stage 2\nSageMaker Core": [
        "Data Prep: Studio, Processing, Feature Store",
        "Training: Built-in + Custom + Distributed",
        "Deployment: Real-time, Batch, MME, MCE"
    ],
    "Stage 3\nMLOps Essentials": [
        "Experiments & Lineage",
        "Model Registry",
        "SageMaker Pipelines + CI/CD"
    ],
    "Stage 4\nAdvanced MLOps": [
        "Monitoring: Model Monitor, Clarify",
        "Scaling: HPO, Autoscaling, Spot Training",
        "Custom Deployment: EKS, BYOC, API Gateway"
    ],
    "Stage 5\nEnterprise MLOps": [
        "IaC with Terraform/CDK",
        "Multi-Account (Dev, Test, Prod)",
        "Security: VPC, KMS, Compliance"
    ],
    "Stage 6\nExpert Architectures": [
        "Domain-Specific (Healthcare, BFSI, Retail)",
        "Hybrid Pipelines: Snowflake, Bedrock",
        "Multi-Cloud/EKS + SageMaker"
    ]
}

# Plot
fig, ax = plt.subplots(figsize=(12, 10))
ax.axis("off")

# Colors for stages
colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#009688", "#F44336"]

# Draw boxes and arrows
y = 0.9
for i, (stage, tasks) in enumerate(stages.items()):
    # Draw rectangle
    ax.add_patch(mpatches.Rectangle((0.05, y - 0.1), 0.9, 0.09,
                                    facecolor=colors[i], alpha=0.7, edgecolor="black"))
    ax.text(0.5, y - 0.055, stage, ha="center", va="center", fontsize=12, fontweight="bold", color="white")

    # Add tasks
    text = "\n".join(tasks)
    ax.text(0.5, y - 0.16, text, ha="center", va="top", fontsize=10)

    # Draw arrow to next stage
    if i < len(stages) - 1:
        ax.annotate("", xy=(0.5, y - 0.22), xytext=(0.5, y - 0.28),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
        y -= 0.28

plt.tight_layout()
plt.show()
