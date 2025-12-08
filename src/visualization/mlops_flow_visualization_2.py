import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots(figsize=(13, 8))
ax.axis("off")

# Define box style
box_style = dict(boxstyle="round,pad=0.5", facecolor="#f0f8ff", edgecolor="black", linewidth=1.5)

# Define positions and labels for workflow (with artifacts)
positions = {
    "Templates": (0.1, 0.7),
    "Projects": (0.4, 0.7),
    "Pipelines": (0.7, 0.7),
    "Deployment": (0.4, 0.4),
    "Monitoring": (0.7, 0.4)
}
labels = {
    "Templates": "📑 Templates\n'MLOps Blueprint'\nArtifacts: infra.json, CI/CD.yaml",
    "Projects": "🏗️ Projects\n'MLOps Environment'\nArtifacts: repo (train.py, evaluate.py)",
    "Pipelines": "🔄 Pipelines\n'ML Workflow'\nArtifacts: claims.csv, preprocessing.py,\ntrain.py, evaluate.py, model.tar.gz",
    "Deployment": "🚀 Deployment\n'Staging → Prod'\nArtifacts: Model Registry entry,\nEndpoint config",
    "Monitoring": "📊 Monitoring\n'Drift Detection + Retraining'\nArtifacts: drift_report.json,\nmetrics.log, retrain_trigger"
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

plt.title("Insurance Risk Prediction with AWS SageMaker\nTemplates → Projects → Pipelines → Deployment → Monitoring (with Artifacts)",
          fontsize=14, weight="bold")
plt.show()