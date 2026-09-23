import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAM_DIR = os.path.join(BASE_DIR, "presentation_assets")
os.makedirs(DIAGRAM_DIR, exist_ok=True)

# Styling defaults
NAVY = "#0F2240"
TEAL = "#0D9488"
BLUE = "#2563EB"
LIGHT_BG = "#F1F5F9"
BORDER_COLOR = "#CBD5E1"
TEXT_COLOR = "#1E293B"

def create_problem_flow():
    fig, ax = plt.subplots(figsize=(8, 2.5), dpi=200)
    ax.set_facecolor("#FFFFFF")
    ax.axis('off')
    
    steps = ["Patient Presentation", "GI Symptoms", "Clinical Examination", "Specialist / Endoscopy"]
    n = len(steps)
    box_w, box_h = 1.6, 0.8
    spacing = 0.4
    
    for i, step in enumerate(steps):
        x = i * (box_w + spacing) + 0.2
        y = 0.85
        
        # Draw Box
        rect = patches.FancyBboxPatch(
            (x, y), box_w, box_h, boxstyle="round,pad=0.05",
            facecolor="#F8FAFC", edgecolor=NAVY, linewidth=1.5
        )
        ax.add_patch(rect)
        
        ax.text(x + box_w/2, y + box_h/2, step, ha='center', va='center',
                fontsize=9, fontweight='bold', color=NAVY, wrap=True)
                
        if i < n - 1:
            ax.annotate("", xy=(x + box_w + spacing - 0.05, y + box_h/2),
                        xytext=(x + box_w + 0.05, y + box_h/2),
                        arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.5))
                        
    ax.set_xlim(0, n * box_w + (n-1)*spacing + 0.4)
    ax.set_ylim(0.5, 2.0)
    plt.tight_layout()
    path = os.path.join(DIAGRAM_DIR, "problem_flow.png")
    plt.savefig(path, bbox_inches='tight', transparent=True)
    plt.close()
    return path

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.set_facecolor("#FFFFFF")
    ax.axis('off')
    
    # Path 1: Tongue
    ax.add_patch(patches.FancyBboxPatch((0.5, 3.8), 2.2, 0.8, boxstyle="round,pad=0.03", facecolor="#F0FDF4", edgecolor="#16A34A", lw=1.5))
    ax.text(1.6, 4.2, "Tongue Image (TMC)\n[224x224 RGB]", ha='center', va='center', fontsize=9, fontweight='bold', color="#15803D")
    
    ax.annotate("", xy=(3.5, 4.2), xytext=(2.7, 4.2), arrowprops=dict(arrowstyle="->", color="#16A34A", lw=2))
    
    ax.add_patch(patches.FancyBboxPatch((3.5, 3.8), 2.2, 0.8, boxstyle="round,pad=0.03", facecolor="#DCFCE7", edgecolor="#16A34A", lw=1.5))
    ax.text(4.6, 4.2, "MobileNetV3 CNN\n[Tongue Encoder]", ha='center', va='center', fontsize=9, fontweight='bold', color="#166534")
    
    ax.annotate("", xy=(6.5, 4.2), xytext=(5.7, 4.2), arrowprops=dict(arrowstyle="->", color="#16A34A", lw=2))
    ax.text(6.1, 4.35, "16-D Vector", fontsize=8, color="#15803D", fontweight='bold')

    # Path 2: Skin
    ax.add_patch(patches.FancyBboxPatch((0.5, 2.3), 2.2, 0.8, boxstyle="round,pad=0.03", facecolor="#EFF6FF", edgecolor="#2563EB", lw=1.5))
    ax.text(1.6, 2.7, "Skin Image (ISIC)\n[Complementary]", ha='center', va='center', fontsize=9, fontweight='bold', color="#1D4ED8")
    
    ax.annotate("", xy=(3.5, 2.7), xytext=(2.7, 2.7), arrowprops=dict(arrowstyle="->", color="#2563EB", lw=2))
    
    ax.add_patch(patches.FancyBboxPatch((3.5, 2.3), 2.2, 0.8, boxstyle="round,pad=0.03", facecolor="#DBEAFE", edgecolor="#2563EB", lw=1.5))
    ax.text(4.6, 2.7, "MobileNetV3 CNN\n[Skin Encoder]", ha='center', va='center', fontsize=9, fontweight='bold', color="#1E40AF")
    
    ax.annotate("", xy=(6.5, 2.7), xytext=(5.7, 2.7), arrowprops=dict(arrowstyle="->", color="#2563EB", lw=2))
    ax.text(6.1, 2.85, "16-D Vector", fontsize=8, color="#1D4ED8", fontweight='bold')

    # Path 3: Clinical
    ax.add_patch(patches.FancyBboxPatch((0.5, 0.8), 2.2, 0.8, boxstyle="round,pad=0.03", facecolor="#FAF5FF", edgecolor="#9333EA", lw=1.5))
    ax.text(1.6, 1.2, "GI Symptoms & Lifestyle\n[15 Features]", ha='center', va='center', fontsize=9, fontweight='bold', color="#7E22CE")
    
    ax.annotate("", xy=(3.5, 1.2), xytext=(2.7, 1.2), arrowprops=dict(arrowstyle="->", color="#9333EA", lw=2))
    
    ax.add_patch(patches.FancyBboxPatch((3.5, 0.8), 2.2, 0.8, boxstyle="round,pad=0.03", facecolor="#F3E8FF", edgecolor="#9333EA", lw=1.5))
    ax.text(4.6, 1.2, "Random Forest ML\n[Clinical Encoder]", ha='center', va='center', fontsize=9, fontweight='bold', color="#6B21A8")
    
    ax.annotate("", xy=(6.5, 1.2), xytext=(5.7, 1.2), arrowprops=dict(arrowstyle="->", color="#9333EA", lw=2))
    ax.text(6.1, 1.35, "16-D Vector", fontsize=8, color="#7E22CE", fontweight='bold')

    # Fusion Layer
    ax.add_patch(patches.FancyBboxPatch((6.5, 1.5), 2.0, 2.2, boxstyle="round,pad=0.05", facecolor="#CCFBF1", edgecolor="#0D9488", lw=2))
    ax.text(7.5, 2.6, "GATED MULTIMODAL\nFEATURE FUSION\n[48-D -> 16-D MLP]", ha='center', va='center', fontsize=9, fontweight='bold', color="#0F766E")
    
    ax.annotate("", xy=(9.2, 2.6), xytext=(8.5, 2.6), arrowprops=dict(arrowstyle="->", color="#0D9488", lw=2.5))

    # Output Box
    ax.add_patch(patches.FancyBboxPatch((9.2, 2.0), 2.0, 1.2, boxstyle="round,pad=0.05", facecolor="#FEF3C7", edgecolor="#D97706", lw=2))
    ax.text(10.2, 2.6, "PRELIMINARY GI RISK\nINDICATION\n(Low / Mod / High)", ha='center', va='center', fontsize=9, fontweight='bold', color="#B45309")

    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.5, 5.0)
    plt.tight_layout()
    path = os.path.join(DIAGRAM_DIR, "architecture.png")
    plt.savefig(path, bbox_inches='tight', transparent=True)
    plt.close()
    return path

def create_pipeline_diagram():
    fig, ax = plt.subplots(figsize=(10, 2), dpi=200)
    ax.set_facecolor("#FFFFFF")
    ax.axis('off')
    
    steps = ["Real Datasets", "Preprocessing", "Model Training", "Evaluation", "FastAPI Backend", "Web App"]
    n = len(steps)
    box_w = 1.3
    spacing = 0.3
    
    for i, step in enumerate(steps):
        x = i * (box_w + spacing) + 0.2
        y = 0.6
        
        rect = patches.FancyBboxPatch((x, y), box_w, 0.7, boxstyle="round,pad=0.04", facecolor="#F1F5F9", edgecolor=NAVY, lw=1.5)
        ax.add_patch(rect)
        ax.text(x + box_w/2, y + 0.35, step, ha='center', va='center', fontsize=8, fontweight='bold', color=NAVY)
        
        if i < n - 1:
            ax.annotate("", xy=(x + box_w + spacing - 0.03, y + 0.35), xytext=(x + box_w + 0.03, y + 0.35),
                        arrowprops=dict(arrowstyle="->", color=TEAL, lw=2))
                        
    ax.set_xlim(0, n * box_w + (n-1)*spacing + 0.4)
    ax.set_ylim(0.4, 1.5)
    plt.tight_layout()
    path = os.path.join(DIAGRAM_DIR, "training_pipeline.png")
    plt.savefig(path, bbox_inches='tight', transparent=True)
    plt.close()
    return path

def create_roadmap_diagram():
    fig, ax = plt.subplots(figsize=(10, 2), dpi=200)
    ax.set_facecolor("#FFFFFF")
    ax.axis('off')
    
    steps = ["Current Prototype", "Paired Cohort Data", "Hospital Clinical Trial", "External Validation", "Mobile App Launch"]
    n = len(steps)
    box_w = 1.6
    spacing = 0.3
    
    for i, step in enumerate(steps):
        x = i * (box_w + spacing) + 0.2
        y = 0.6
        bg_col = "#CCFBF1" if i == 0 else "#F8FAFC"
        border_col = TEAL if i == 0 else NAVY
        
        rect = patches.FancyBboxPatch((x, y), box_w, 0.7, boxstyle="round,pad=0.04", facecolor=bg_col, edgecolor=border_col, lw=1.5)
        ax.add_patch(rect)
        ax.text(x + box_w/2, y + 0.35, f"Phase {i+1}\n{step}", ha='center', va='center', fontsize=8, fontweight='bold', color=NAVY)
        
        if i < n - 1:
            ax.annotate("", xy=(x + box_w + spacing - 0.03, y + 0.35), xytext=(x + box_w + 0.03, y + 0.35),
                        arrowprops=dict(arrowstyle="->", color=TEAL, lw=2))
                        
    ax.set_xlim(0, n * box_w + (n-1)*spacing + 0.4)
    ax.set_ylim(0.4, 1.5)
    plt.tight_layout()
    path = os.path.join(DIAGRAM_DIR, "roadmap.png")
    plt.savefig(path, bbox_inches='tight', transparent=True)
    plt.close()
    return path

if __name__ == "__main__":
    create_problem_flow()
    create_architecture_diagram()
    create_pipeline_diagram()
    create_roadmap_diagram()
    print("ALL PRESENTATION ASSETS GENERATED SUCCESSFULLY!")
