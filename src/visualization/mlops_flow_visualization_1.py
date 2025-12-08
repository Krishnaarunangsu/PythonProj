import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(figsize=(12, 7))
ax.axis("off")

# Define box style
box_style = dict(boxstyle="round,pad=0.5", facecolor="#e6f2ff", edgecolor="black", linewidth=1.5)

# Define positions and labels for workflow
positions = {
    "Templates": (0.1, 0.7),
    "Projects": (0.4, 0.7),
    "Pipelines": (0.7, 0.7),
    "Deployment": (0.4, 0.4),
    "Monitoring": (0.7, 0.4)
}
labels = {
    "Templates": "📑 Templates\n(MLOps Blueprints)\n[Platform Engineer]",
    "Projects": "🏗️ Projects\n(MLOps Environment)\n[Data Scientist Launches]",
    "Pipelines": "🔄 Pipelines\n(ML Workflow Orchestration)\n[Training, Eval, Register]",
    "Deployment": "🚀 Deployment\n(Staging → Prod)\n[CI/CD + Model Registry]",
    "Monitoring": "📊 Monitoring\n(Model Monitor, Drift Detection)\n[Automated Retraining]"
}

# Draw boxes
for key, (x, y) in positions.items():
    ax.text(x, y, labels[key], ha="center", va="center", fontsize=10,
            bbox=box_style)

# Draw arrows
arrowprops = dict(arrowstyle="->", color="black", linewidth=1.5)

# Templates → Projects → Pipelines
ax.annotate("", xy=positions["Projects"], xytext=positions["Templates"], arrowprops=arrowprops)
ax.annotate("", xy=positions["Pipelines"], xytext=positions["Projects"], arrowprops=arrowprops)

# Pipelines → Deployment
ax.annotate("", xy=positions["Deployment"], xytext=positions["Pipelines"], arrowprops=arrowprops)

# Deployment → Monitoring
ax.annotate("", xy=positions["Monitoring"], xytext=positions["Deployment"], arrowprops=arrowprops)

# Monitoring → Pipelines (feedback loop)
ax.annotate("", xy=positions["Pipelines"], xytext=positions["Monitoring"], arrowprops=arrowprops)

plt.title("AWS SageMaker: Templates → Projects → Pipelines → Deployment → Monitoring", fontsize=14, weight="bold")
plt.show()
