import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a basic architecture diagram for DevOps contextual flow using matplotlib
fig, ax = plt.subplots(figsize=(14, 8))
ax.axis('off')

# Define boxes and their coordinates
boxes = {
    "Developer": (0.1, 0.8),
    "Source Control (GitHub/GitLab)": (0.3, 0.8),
    "CI Tool (Jenkins/\nGitHub Actions/\nGitLab CI)": (0.5, 0.8),
    "Automated Testing": (0.7, 0.8),
    "Artifact Repository (S3/\nDocker Hub/\nJFrog)": (0.5, 0.6),
    "CD Tool (ArgoCD/\nSpinnaker)": (0.3, 0.4),
    "Container Registry": (0.5, 0.4),
    "Kubernetes Cluster\n(EKS/GKE/AKS)": (0.7, 0.4),
    "Monitoring & Logging\n(Prometheus/Grafana/\nELK/CloudWatch)": (0.5, 0.2),
}

# Draw boxes
for text, (x, y) in boxes.items():
    ax.add_patch(mpatches.FancyBboxPatch((x, y), 0.18, 0.1,
                                         boxstyle="round,pad=0.02",
                                         edgecolor='black', facecolor='lightblue'))
    ax.text(x + 0.09, y + 0.05, text, ha='center', va='center', fontsize=9)

# Draw arrows to indicate flow
connections = [
    ("Developer", "Source Control (GitHub/GitLab)"),
    ("Source Control (GitHub/GitLab)", "CI Tool (Jenkins/\nGitHub Actions/\nGitLab CI)"),
    ("CI Tool (Jenkins/\nGitHub Actions/\nGitLab CI)", "Automated Testing"),
    ("CI Tool (Jenkins/\nGitHub Actions/\nGitLab CI)", "Artifact Repository (S3/\nDocker Hub/\nJFrog)"),
    ("Artifact Repository (S3/\nDocker Hub/\nJFrog)", "CD Tool (ArgoCD/\nSpinnaker)"),
    ("Artifact Repository (S3/\nDocker Hub/\nJFrog)", "Container Registry"),
    ("CD Tool (ArgoCD/\nSpinnaker)", "Kubernetes Cluster\n(EKS/GKE/AKS)"),
    ("Container Registry", "Kubernetes Cluster\n(EKS/GKE/AKS)"),
    ("Kubernetes Cluster\n(EKS/GKE/AKS)", "Monitoring & Logging\n(Prometheus/Grafana/\nELK/CloudWatch)"),
]

box_centers = {k: (x + 0.09, y + 0.05) for k, (x, y) in boxes.items()}

for src, dst in connections:
    sx, sy = box_centers[src]
    dx, dy = box_centers[dst]
    ax.annotate("", xy=(dx, dy), xytext=(sx, sy),
                arrowprops=dict(arrowstyle="->", color='gray'))

plt.title("DevOps Contextual Architecture Diagram", fontsize=14)
plt.tight_layout()
plt.show()
