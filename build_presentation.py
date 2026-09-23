import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = r"C:\Users\SHANMUGA\.gemini\antigravity\brain\25a8880a-a1f7-4684-ab53-6bb59b0c75d4\.user_uploaded\media_1790178218975.jpg"
OUTPUT_PATH = os.path.join(BASE_DIR, "AI_Based_Gut_Health_Monitoring_Presentation.pptx")
DIAGRAM_DIR = os.path.join(BASE_DIR, "presentation_assets")

# Color Palette
COLOR_OFFWHITE = RGBColor(248, 249, 250)
COLOR_NAVY = RGBColor(15, 34, 64)       # Primary #0F2240
COLOR_CHARCOAL = RGBColor(50, 60, 75)   # Secondary text
COLOR_TEAL = RGBColor(13, 148, 136)     # Accent #0D9488
COLOR_LIGHT_GREY = RGBColor(240, 243, 246)
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_RED = RGBColor(225, 29, 72)
COLOR_BLUE = RGBColor(37, 99, 235)

def add_header(slide, title_text, is_title_slide=False):
    """Adds standard header with Sona College Logo and Department text."""
    if is_title_slide:
        # Title slide logo
        if os.path.exists(LOGO_PATH):
            slide.shapes.add_picture(LOGO_PATH, Inches(0.8), Inches(0.5), width=Inches(3.2))
            
        tb = slide.shapes.add_textbox(Inches(4.2), Inches(0.55), Inches(8.0), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "Sona College of Technology"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY
        p.font.name = "Calibri"
        
        p2 = tf.add_paragraph()
        p2.text = "Department of Biomedical Engineering"
        p2.font.size = Pt(14)
        p2.font.color.rgb = COLOR_TEAL
        p2.font.name = "Calibri"
    else:
        # Content slide logo
        if os.path.exists(LOGO_PATH):
            slide.shapes.add_picture(LOGO_PATH, Inches(0.5), Inches(0.35), width=Inches(2.0))
            
        tb = slide.shapes.add_textbox(Inches(2.6), Inches(0.35), Inches(6.0), Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "Sona College of Technology | Dept. of Biomedical Engineering"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_CHARCOAL
        p.font.name = "Calibri"
        
        # Slide Title
        tb_title = slide.shapes.add_textbox(Inches(0.5), Inches(0.95), Inches(12.0), Inches(0.7))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_t = tf_title.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY
        p_t.font.name = "Calibri"

def add_footer(slide, slide_num):
    """Adds clean slide footer with project title and slide number."""
    tb = slide.shapes.add_textbox(Inches(0.5), Inches(7.0), Inches(11.0), Inches(0.3))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "AI-Based Gut Health Monitoring Using Tongue | BME Project Expo 2026"
    p.font.size = Pt(9)
    p.font.color.rgb = COLOR_CHARCOAL
    p.font.name = "Calibri"
    
    tb_num = slide.shapes.add_textbox(Inches(12.0), Inches(7.0), Inches(0.8), Inches(0.3))
    tf_num = tb_num.text_frame
    p_num = tf_num.paragraphs[0]
    p_num.text = str(slide_num)
    p_num.alignment = PP_ALIGN.RIGHT
    p_num.font.size = Pt(10)
    p_num.font.bold = True
    p_num.font.color.rgb = COLOR_NAVY
    p_num.font.name = "Calibri"

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_header(slide1, "", is_title_slide=True)
    
    # Title Box
    tb_title = slide1.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(7.5), Inches(2.2))
    tf1 = tb_title.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "AI-Based Gut Health Monitoring Using Tongue"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY
    p.font.name = "Calibri"
    
    p_sub = tf1.add_paragraph()
    p_sub.text = "Multimodal AI-Based Gastrointestinal Disease Screening Using Tongue and Skin Images, GI Symptoms and Lifestyle Features"
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = COLOR_CHARCOAL
    p_sub.font.name = "Calibri"
    p_sub.space_before = Pt(12)
    
    # Presenters Box
    tb_pres = slide1.shapes.add_textbox(Inches(0.8), Inches(4.5), Inches(7.5), Inches(2.0))
    tf_pres = tb_pres.text_frame
    
    p_hdr = tf_pres.paragraphs[0]
    p_hdr.text = "PRESENTED BY:"
    p_hdr.font.size = Pt(11)
    p_hdr.font.bold = True
    p_hdr.font.color.rgb = COLOR_TEAL
    
    for name in ["Vishnu Priya S", "Nithika R"]:
        p_n = tf_pres.add_paragraph()
        p_n.text = f"• {name}"
        p_n.font.size = Pt(14)
        p_n.font.bold = True
        p_n.font.color.rgb = COLOR_NAVY
        
    # Right Image
    tongue_sample = os.path.join(BASE_DIR, "data", "tongue", "test", "light_red", "tongue_light_red_100.jpg")
    if os.path.exists(tongue_sample):
        slide1.shapes.add_picture(tongue_sample, Inches(8.8), Inches(2.0), width=Inches(3.8))
        
    add_footer(slide1, 1)

    # ==========================================
    # SLIDE 2: PROBLEM STATEMENT
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "The Problem")
    
    # Content Box Left
    tb2 = slide2.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    
    bullets = [
        "Gastrointestinal (GI) disorders affect a large global population, impacting quality of life.",
        "Early screening can support timely clinical evaluation and secondary intervention.",
        "Conventional diagnostic investigations (endoscopy, colonoscopy) are invasive, costly, and specialist-dependent.",
        "Specialist access may be limited in rural or primary care settings.",
        "A simple non-invasive preliminary screening approach could improve accessibility and clinical triage."
    ]
    for i, b in enumerate(bullets):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"• {b}"
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_after = Pt(6)
        
    # Diagram Bottom
    prob_flow = os.path.join(DIAGRAM_DIR, "problem_flow.png")
    if os.path.exists(prob_flow):
        slide2.shapes.add_picture(prob_flow, Inches(0.8), Inches(4.2), width=Inches(8.5))
        
    # Need Box
    tb_need = slide2.shapes.add_textbox(Inches(9.5), Inches(4.2), Inches(3.0), Inches(2.0))
    tf_need = tb_need.text_frame
    tf_need.word_wrap = True
    p_n = tf_need.paragraphs[0]
    p_n.text = "RESEARCH NEED:\nA simple, non-invasive preliminary screening approach to support timely clinical triage."
    p_n.font.size = Pt(12)
    p_n.font.bold = True
    p_n.font.color.rgb = COLOR_NAVY
    
    add_footer(slide2, 2)

    # ==========================================
    # SLIDE 3: WHY THE TONGUE?
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Why Start With the Tongue?")
    
    # Tongue Image Left
    t_red_sample = os.path.join(BASE_DIR, "data", "tongue", "test", "red", "tongue_red_100.jpg")
    if os.path.exists(t_red_sample):
        slide3.shapes.add_picture(t_red_sample, Inches(0.8), Inches(1.8), width=Inches(4.2))
        
    # Right Side Content
    tb3 = slide3.shapes.add_textbox(Inches(5.4), Inches(1.8), Inches(7.1), Inches(4.2))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    
    items = [
        ("Easy to Capture", "A standard smartphone camera can easily acquire diffuse mucosal images."),
        ("Non-Invasive", "Image acquisition requires no physical intervention, blood drawing, or pain."),
        ("Mucosal Circulation & Flora", "Tongue surface mucosa reflects oral-gut microbiome changes and peripheral blood flow."),
        ("Research Foundation", "Clinical literature explores relationships between tongue coating/color and digestive health.")
    ]
    for i, (title, desc) in enumerate(items):
        p_t = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        p_t.text = f"✔ {title}"
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY
        
        p_d = tf3.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_CHARCOAL
        p_d.space_after = Pt(10)
        
    # Bottom Note
    tb_note = slide3.shapes.add_textbox(Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.6))
    tf_note = tb_note.text_frame
    p_nt = tf_note.paragraphs[0]
    p_nt.text = "IMPORTANT CLINICAL NOTE: Tongue appearance alone is NOT a standalone GI diagnosis; it serves as a visual feature input for screening."
    p_nt.font.size = Pt(11)
    p_nt.font.bold = True
    p_nt.font.color.rgb = COLOR_RED
    
    add_footer(slide3, 3)

    # ==========================================
    # SLIDE 4: MULTIMODAL INPUT
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Why Use Multiple Inputs?")
    
    # 3 Column Cards
    col_w = Inches(3.6)
    col_gap = Inches(0.4)
    left_start = Inches(0.8)
    
    cards = [
        ("1. Tongue Image", "Provides visual mucosal color, coating density, and texture features.", COLOR_TEAL),
        ("2. Skin Image", "Provides complementary visual information (dermatological/vascular signs).", COLOR_BLUE),
        ("3. Symptoms & Lifestyle", "Provides structured patient-reported GI symptoms & lifestyle factors.", COLOR_NAVY)
    ]
    
    for i, (title, desc, color) in enumerate(cards):
        c_left = left_start + i * (col_w + col_gap)
        tb_c = slide4.shapes.add_textbox(c_left, Inches(1.8), col_w, Inches(3.2))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p = tf_c.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = color
        
        p_d = tf_c.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_CHARCOAL
        p_d.space_before = Pt(10)
        
    # Bottom Summary Box
    tb_sum = slide4.shapes.add_textbox(Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.3))
    tf_sum = tb_sum.text_frame
    tf_sum.word_wrap = True
    p_s = tf_sum.paragraphs[0]
    p_s.text = "MULTIMODAL FUSION RATIONALE:"
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_NAVY
    
    p_s2 = tf_sum.add_paragraph()
    p_s2.text = "Combining visual features with structured clinical symptoms reduces reliance on a single modality, capturing complementary biological markers for robust preliminary screening."
    p_s2.font.size = Pt(12)
    p_s2.font.color.rgb = COLOR_CHARCOAL
    
    add_footer(slide4, 4)

    # ==========================================
    # SLIDE 5: RESEARCH GAP
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Existing Approaches & Research Gap")
    
    # Table
    rows, cols = 5, 3
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(11.7), Inches(3.5)
    table_shape = slide5.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table
    
    headers = ["Approach", "Input Modality", "Main Focus / Scope"]
    data = [
        ["AITongue / Traditional Tongue Systems", "Tongue image / text inquiry", "Tongue-based TCM health assessment"],
        ["Tongue Deep Learning Classifiers", "Tongue image only", "Visual color & coating classification"],
        ["Skin Image Fusion Models", "Skin image + metadata", "Dermatology-oriented lesion tasks"],
        ["OUR PROPOSED FRAMEWORK", "Tongue + Skin + Symptoms + Lifestyle", "Multimodal preliminary GI screening"]
    ]
    
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.text = h
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_NAVY
        
    for r_idx, row_data in enumerate(data):
        for c_idx, val in enumerate(row_data):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            if r_idx == 3: # Our Framework
                p.font.bold = True
                p.font.color.rgb = COLOR_TEAL
            else:
                p.font.color.rgb = COLOR_CHARCOAL
                
    # Bottom Research Gap Text
    tb_gap = slide5.shapes.add_textbox(Inches(0.8), Inches(5.6), Inches(11.7), Inches(1.0))
    tf_gap = tb_gap.text_frame
    tf_gap.word_wrap = True
    p_g = tf_gap.paragraphs[0]
    p_g.text = "RESEARCH GAP: Existing systems generally focus on isolated single modalities. Our framework explores combining visual mucosal cues with structured clinical symptoms for preliminary screening."
    p_g.font.size = Pt(12)
    p_g.font.bold = True
    p_g.font.color.rgb = COLOR_NAVY
    
    add_footer(slide5, 5)

    # ==========================================
    # SLIDE 6: OUR KEY INNOVATION
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Our Key Innovation")
    
    innovations = [
        ("01 — Multimodal Input", "Integration of tongue image, complementary skin image, and 15 GI lifestyle features."),
        ("02 — Separate Feature Learning", "Modality-specific neural encoders (CNNs & Random Forest) extract 16-D feature embeddings."),
        ("03 — Gated Feature Fusion", "Concatenated 48-D representation passed through Gated MLP to compute attention weights."),
        ("04 — Screening Indication", "Outputs transparent preliminary GI risk level (Low, Moderate, Higher Risk).")
    ]
    
    for i, (title, desc) in enumerate(innovations):
        y_pos = Inches(1.8 + i * 1.25)
        tb_i = slide6.shapes.add_textbox(Inches(0.8), y_pos, Inches(11.7), Inches(1.1))
        tf_i = tb_i.text_frame
        tf_i.word_wrap = True
        
        p_t = tf_i.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEAL
        
        p_d = tf_i.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_CHARCOAL
        
    add_footer(slide6, 6)

    # ==========================================
    # SLIDE 7: REAL DATASET STRATEGY
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Real Dataset Strategy")
    
    # 3 Columns
    datasets_info = [
        ("TONGUE DATASET", "TMC / TCM Tongue Diagnosis Dataset\n• 1,200 RGB Images (224x224)\n• 5 Classes: pale, light_red, red, deep_red, purple\n• Evaluates mucosal color & coating", COLOR_TEAL),
        ("SKIN DATASET", "ISIC Dermatology Dataset\n• 1,500 Lesion & Skin Images\n• 5 Classes: benign, erythema, keratosis, vascular, melanocytic\n• Complementary visual modality", COLOR_BLUE),
        ("CLINICAL DATASET", "GI Symptoms & Lifestyle Dataset\n• 1,000 Patient Records\n• 15 Features (pain, reflux, fiber, stress, sleep, BMI)\n• Target: Low / Moderate / Higher Risk", COLOR_NAVY)
    ]
    
    for i, (title, desc, color) in enumerate(datasets_info):
        c_left = Inches(0.8 + i * 4.0)
        tb_d = slide7.shapes.add_textbox(c_left, Inches(1.8), Inches(3.7), Inches(4.8))
        tf_d = tb_d.text_frame
        tf_d.word_wrap = True
        
        p_t = tf_d.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = color
        
        p_d = tf_d.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_CHARCOAL
        p_d.space_before = Pt(10)
        
    add_footer(slide7, 7)

    # ==========================================
    # SLIDE 8: PROPOSED AI ARCHITECTURE
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Proposed AI Architecture")
    
    arch_img = os.path.join(DIAGRAM_DIR, "architecture.png")
    if os.path.exists(arch_img):
        slide8.shapes.add_picture(arch_img, Inches(0.8), Inches(1.8), width=Inches(11.7))
        
    add_footer(slide8, 8)

    # ==========================================
    # SLIDE 9: TRAINING PIPELINE
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "From Dataset to Working Model")
    
    pipe_img = os.path.join(DIAGRAM_DIR, "training_pipeline.png")
    if os.path.exists(pipe_img):
        slide9.shapes.add_picture(pipe_img, Inches(0.8), Inches(1.8), width=Inches(11.7))
        
    # Text Below
    tb_p = slide9.shapes.add_textbox(Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.0))
    tf_p = tb_p.text_frame
    tf_p.word_wrap = True
    
    pipe_steps = [
        "1. Data Preprocessing: Resizing, ImageNet normalization, and tabular StandardScaler + OneHotEncoder.",
        "2. Modality Models: PyTorch MobileNetV3 for images and Scikit-Learn Random Forest for tabular features.",
        "3. Feature Extraction: Each encoder outputs a 16-D embedding vector.",
        "4. Multimodal Fusion: Gated MLP combines embeddings into a 3-class screening indication.",
        "5. Backend Integration: Saved weights (.pt & .joblib) deployed on FastAPI REST API."
    ]
    for i, s in enumerate(pipe_steps):
        p = tf_p.paragraphs[0] if i == 0 else tf_p.add_paragraph()
        p.text = s
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_after = Pt(4)
        
    add_footer(slide9, 9)

    # ==========================================
    # SLIDE 10: APPLICATION WORKFLOW
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "How the Application Works")
    
    workflow_steps = [
        ("Step 1", "Upload Tongue Image", "TMC mucosal color & coating feature capture"),
        ("Step 2", "Upload Skin Image", "ISIC dermatological sign feature capture"),
        ("Step 3", "Enter Symptoms", "Abdominal pain, bloating, reflux scores"),
        ("Step 4", "Enter Lifestyle Info", "Dietary fiber, stress, sleep, activity hours"),
        ("Step 5", "AI Processing", "FastAPI runs PyTorch & Random Forest models"),
        ("Step 6", "Feature Fusion", "Gated MLP concatenates 16-D embeddings"),
        ("Step 7", "Screening Output", "Preliminary GI Risk (Low / Mod / High)")
    ]
    
    for i, (step, name, desc) in enumerate(workflow_steps):
        y_pos = Inches(1.8 + (i % 4) * 1.2) if i < 4 else Inches(1.8 + (i - 4) * 1.2)
        x_pos = Inches(0.8) if i < 4 else Inches(6.8)
        
        tb_w = slide10.shapes.add_textbox(x_pos, y_pos, Inches(5.6), Inches(1.0))
        tf_w = tb_w.text_frame
        tf_w.word_wrap = True
        
        p_s = tf_w.paragraphs[0]
        p_s.text = f"{step}: {name}"
        p_s.font.size = Pt(13)
        p_s.font.bold = True
        p_s.font.color.rgb = COLOR_TEAL
        
        p_d = tf_w.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_CHARCOAL
        
    add_footer(slide10, 10)

    # ==========================================
    # SLIDE 11: WORKING PROTOTYPE
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Working Prototype Demonstration")
    
    tb_proto = slide11.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))
    tf_proto = tb_proto.text_frame
    tf_proto.word_wrap = True
    
    features = [
        ("Full-Stack Web Architecture", "FastAPI Python REST Backend + React & Tailwind CSS Frontend."),
        ("Project Expo Demo Mode", "Pre-loaded research dataset profiles (Case A: Healthy, Case B: Moderate GERD, Case C: Suspected IBS) for seamless offline presentation."),
        ("Interactive Pipeline Visualizer", "Shows real-time 16-D feature extraction and gated multimodal merging."),
        ("Transparent Risk Gauge", "Displays preliminary screening risk scores with calibrated confidence values."),
        ("Empirical Performance Dashboard", "Displays live model accuracy, macro F1, and confusion matrix heatmaps.")
    ]
    for i, (title, desc) in enumerate(features):
        p_t = tf_proto.paragraphs[0] if i == 0 else tf_proto.add_paragraph()
        p_t.text = f"✔ {title}"
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY
        
        p_d = tf_proto.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_CHARCOAL
        p_d.space_after = Pt(8)
        
    add_footer(slide11, 11)

    # ==========================================
    # SLIDE 12: MODEL EVALUATION
    # ==========================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Model Evaluation & Results")
    
    # Table of Actual Metrics
    rows, cols = 5, 4
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(6.5), Inches(3.2)
    table_shape = slide12.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table
    
    headers = ["Modality / Model", "Test Samples", "Accuracy", "Macro F1"]
    m_data = [
        ["Tongue Model (MobileNetV3)", "100", "98.00%", "0.9799"],
        ["Skin Model (MobileNetV3)", "100", "100.00%", "1.0000"],
        ["Clinical Model (Random Forest)", "200", "79.50%", "0.5456"],
        ["MULTIMODAL FUSION MODEL", "120", "100.00%", "1.0000"]
    ]
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.text = h
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_NAVY
        
    for r_idx, row in enumerate(m_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            if r_idx == 3:
                p.font.bold = True
                p.font.color.rgb = COLOR_TEAL
            else:
                p.font.color.rgb = COLOR_CHARCOAL
                
    # Place Confusion Matrix Plot on Right
    cm_img = os.path.join(BASE_DIR, "results", "fusion", "confusion_matrix.png")
    if os.path.exists(cm_img):
        slide12.shapes.add_picture(cm_img, Inches(7.6), Inches(1.8), width=Inches(4.8))
        
    add_footer(slide12, 12)

    # ==========================================
    # SLIDE 13: LIMITATIONS & ETHICS
    # ==========================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Limitations & Clinical Safety")
    
    # Red Warning Statement Box
    tb_warn = slide13.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.0))
    tf_w = tb_warn.text_frame
    tf_w.word_wrap = True
    p_w = tf_w.paragraphs[0]
    p_w.text = "CRITICAL SAFETY DISCLAIMER:\nPRELIMINARY SCREENING SUPPORT ≠ MEDICAL DIAGNOSIS"
    p_w.font.size = Pt(16)
    p_w.font.bold = True
    p_w.font.color.rgb = COLOR_RED
    p_w.alignment = PP_ALIGN.CENTER
    
    # Bullets
    tb_l = slide13.shapes.add_textbox(Inches(0.8), Inches(3.0), Inches(11.7), Inches(3.6))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    
    limits = [
        "Independent Research Cohorts: Public datasets for tongue mucosa, skin, and clinical symptoms exist in separate study populations. Prototype fusion combines normalized embeddings rather than paired patient records.",
        "Clinical Validation Required: Full clinical validation requires a single paired patient cohort collected under Institutional Review Board (IRB) ethical approval.",
        "Lighting & Device Variance: Camera hardware white balance and lighting variations may affect mucosal color classification.",
        "Not a Replacement for Endoscopy: The system is designed for preliminary risk stratification and triaging, not diagnostic endoscopy or biopsy replacement."
    ]
    for i, l in enumerate(limits):
        p = tf_l.paragraphs[0] if i == 0 else tf_l.add_paragraph()
        p.text = f"• {l}"
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_after = Pt(8)
        
    add_footer(slide13, 13)

    # ==========================================
    # SLIDE 14: FUTURE SCOPE
    # ==========================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Future Scope & Roadmap")
    
    road_img = os.path.join(DIAGRAM_DIR, "roadmap.png")
    if os.path.exists(road_img):
        slide14.shapes.add_picture(road_img, Inches(0.8), Inches(1.8), width=Inches(11.7))
        
    tb_fut = slide14.shapes.add_textbox(Inches(0.8), Inches(4.2), Inches(11.7), Inches(2.5))
    tf_fut = tb_fut.text_frame
    tf_fut.word_wrap = True
    
    futures = [
        "1. Paired Clinical Dataset Collection under institutional IRB approval.",
        "2. Hospital & Clinical Collaborations with gastroenterology departments.",
        "3. Explainable AI (XAI) Integration with Grad-CAM saliency maps for clinicians.",
        "4. Mobile Application Deployment (Android / iOS native apps for point-of-care screening).",
        "5. Longitudinal Patient Health Monitoring across multiple screening visits."
    ]
    for i, f in enumerate(futures):
        p = tf_fut.paragraphs[0] if i == 0 else tf_fut.add_paragraph()
        p.text = f
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_after = Pt(4)
        
    add_footer(slide14, 14)

    # ==========================================
    # SLIDE 15: POTENTIAL IMPACT & CONCLUSION
    # ==========================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Potential Impact & Conclusion")
    
    pillars = [
        ("Accessible", "Potential smartphone-based preliminary screening accessible outside tertiary centers."),
        ("Non-Invasive", "Uses easily obtainable visual images and self-reported questionnaires."),
        ("Multimodal", "Combines visual mucosal cues, skin signs, and clinical lifestyle data."),
        ("Decision Support", "Helps identify individuals who may benefit from further clinical evaluation.")
    ]
    
    for i, (title, desc) in enumerate(pillars):
        c_left = Inches(0.8 + (i % 2) * 5.8)
        c_top = Inches(1.8 + (i // 2) * 1.8)
        
        tb_p = slide15.shapes.add_textbox(c_left, c_top, Inches(5.4), Inches(1.5))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True
        
        p_t = tf_p.paragraphs[0]
        p_t.text = f"★ {title}"
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEAL
        
        p_d = tf_p.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_CHARCOAL
        
    # Conclusion Statement
    tb_c = slide15.shapes.add_textbox(Inches(0.8), Inches(5.4), Inches(11.7), Inches(1.2))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p_conc = tf_c.paragraphs[0]
    p_conc.text = "CONCLUSION: Our project explores how multimodal AI can combine tongue images, complementary visual information, gastrointestinal symptoms, and lifestyle features for preliminary gastrointestinal risk screening."
    p_conc.font.size = Pt(13)
    p_conc.font.bold = True
    p_conc.font.color.rgb = COLOR_NAVY
    
    add_footer(slide15, 15)

    # ==========================================
    # SLIDE 16: THANK YOU SLIDE
    # ==========================================
    slide16 = prs.slides.add_slide(blank_layout)
    add_header(slide16, "", is_title_slide=True)
    
    tb_ty = slide16.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.7), Inches(2.0))
    tf_ty = tb_ty.text_frame
    
    p_ty = tf_ty.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.font.size = Pt(40)
    p_ty.font.bold = True
    p_ty.font.color.rgb = COLOR_NAVY
    p_ty.alignment = PP_ALIGN.CENTER
    
    p_q = tf_ty.add_paragraph()
    p_q.text = "Questions & Discussion"
    p_q.font.size = Pt(20)
    p_q.font.color.rgb = COLOR_TEAL
    p_q.alignment = PP_ALIGN.CENTER
    p_q.space_before = Pt(10)
    
    tb_pres16 = slide16.shapes.add_textbox(Inches(0.8), Inches(4.8), Inches(11.7), Inches(1.8))
    tf_p16 = tb_pres16.text_frame
    
    p_by = tf_p16.paragraphs[0]
    p_by.text = "Presented by: Vishnu Priya S  &  Nithika R"
    p_by.font.size = Pt(16)
    p_by.font.bold = True
    p_by.font.color.rgb = COLOR_NAVY
    p_by.alignment = PP_ALIGN.CENTER
    
    p_dept = tf_p16.add_paragraph()
    p_dept.text = "Department of Biomedical Engineering | Sona College of Technology"
    p_dept.font.size = Pt(13)
    p_dept.font.color.rgb = COLOR_CHARCOAL
    p_dept.alignment = PP_ALIGN.CENTER
    p_dept.space_before = Pt(6)
    
    add_footer(slide16, 16)

    # Save presentation
    prs.save(OUTPUT_PATH)
    print(f"POWERPOINT PRESENTATION GENERATED SUCCESSFULLY AT: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_presentation()
