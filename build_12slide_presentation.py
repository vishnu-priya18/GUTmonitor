import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = r"C:\Users\SHANMUGA\.gemini\antigravity\brain\25a8880a-a1f7-4684-ab53-6bb59b0c75d4\.user_uploaded\media_1790178218975.jpg"
OUTPUT_PATH = os.path.join(BASE_DIR, "AI_Based_Gut_Health_Monitoring_12Slide_Presentation.pptx")
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
    """Adds header with Sona College Logo and Department text."""
    if is_title_slide:
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
        if os.path.exists(LOGO_PATH):
            slide.shapes.add_picture(LOGO_PATH, Inches(0.5), Inches(0.35), width=Inches(1.8))
            
        tb = slide.shapes.add_textbox(Inches(2.5), Inches(0.35), Inches(6.5), Inches(0.5))
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
    """Adds clean slide footer."""
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
    p_num.text = f"Slide {slide_num} of 12"
    p_num.alignment = PP_ALIGN.RIGHT
    p_num.font.size = Pt(10)
    p_num.font.bold = True
    p_num.font.color.rgb = COLOR_NAVY
    p_num.font.name = "Calibri"

def build_12slide_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_header(slide1, "", is_title_slide=True)
    
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
        
    tongue_sample = os.path.join(BASE_DIR, "data", "tongue", "test", "light_red", "tongue_light_red_100.jpg")
    if os.path.exists(tongue_sample):
        slide1.shapes.add_picture(tongue_sample, Inches(8.8), Inches(2.0), width=Inches(3.8))
        
    add_footer(slide1, 1)

    # ==========================================
    # SLIDE 2: THE PROBLEM
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "The Problem")
    
    tb2 = slide2.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.2))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    
    bullets = [
        "Gastrointestinal (GI) disorders affect a large global population, impacting overall quality of life.",
        "Early screening can support timely clinical evaluation and secondary triage.",
        "Conventional diagnostic investigations (endoscopy, colonoscopy) may be invasive, costly, and specialist-dependent.",
        "Specialist access can be limited in rural, primary care, or low-resource settings.",
        "A simple non-invasive preliminary screening approach could improve healthcare accessibility."
    ]
    for i, b in enumerate(bullets):
        p = tf2.paragraphs[0] if i == 0 else tf2.add_paragraph()
        p.text = f"• {b}"
        p.font.size = Pt(13)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_after = Pt(6)
        
    prob_flow = os.path.join(DIAGRAM_DIR, "problem_flow.png")
    if os.path.exists(prob_flow):
        slide2.shapes.add_picture(prob_flow, Inches(0.8), Inches(4.2), width=Inches(8.5))
        
    tb_need = slide2.shapes.add_textbox(Inches(9.5), Inches(4.2), Inches(3.0), Inches(2.0))
    tf_need = tb_need.text_frame
    tf_need.word_wrap = True
    p_n = tf_need.paragraphs[0]
    p_n.text = "RESEARCH NEED:\nA simple, non-invasive preliminary screening approach to support timely clinical evaluation."
    p_n.font.size = Pt(12)
    p_n.font.bold = True
    p_n.font.color.rgb = COLOR_NAVY
    
    add_footer(slide2, 2)

    # ==========================================
    # SLIDE 3: WHY START WITH THE TONGUE?
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Why Start With the Tongue?")
    
    t_red_sample = os.path.join(BASE_DIR, "data", "tongue", "test", "red", "tongue_red_100.jpg")
    if os.path.exists(t_red_sample):
        slide3.shapes.add_picture(t_red_sample, Inches(0.8), Inches(1.8), width=Inches(4.2))
        
    tb3 = slide3.shapes.add_textbox(Inches(5.4), Inches(1.8), Inches(7.1), Inches(4.2))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    
    items = [
        ("Easy to Capture", "Smartphone cameras can easily acquire diffuse tongue mucosal images."),
        ("Non-Invasive", "Image acquisition requires no physical intervention or patient discomfort."),
        ("Research Interest", "Previous clinical research has explored relationships between tongue mucosal appearance, microflora, and GI conditions."),
        ("Visual Features", "Enables quantitative feature extraction of Colour, Coating, Texture, and Surface characteristics.")
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
        p_d.space_after = Pt(8)
        
    tb_note = slide3.shapes.add_textbox(Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.6))
    tf_note = tb_note.text_frame
    p_nt = tf_note.paragraphs[0]
    p_nt.text = "IMPORTANT NOTE: Tongue appearance alone is not a standalone diagnosis; it provides feature inputs for preliminary screening."
    p_nt.font.size = Pt(11)
    p_nt.font.bold = True
    p_nt.font.color.rgb = COLOR_RED
    
    add_footer(slide3, 3)

    # ==========================================
    # SLIDE 4: WHY MULTIMODAL INPUTS?
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Why Use Multiple Inputs?")
    
    col_w = Inches(3.6)
    col_gap = Inches(0.4)
    left_start = Inches(0.8)
    
    cards = [
        ("1. Tongue Image", "Provides visual mucosal color, coating density, and texture features.", COLOR_TEAL),
        ("2. Skin Image", "Provides complementary visual information (dermatological & vascular signs).", COLOR_BLUE),
        ("3. Symptoms & Lifestyle", "Provides structured patient-reported GI symptoms & lifestyle data.", COLOR_NAVY)
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
        
    tb_sum = slide4.shapes.add_textbox(Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.3))
    tf_sum = tb_sum.text_frame
    tf_sum.word_wrap = True
    p_s = tf_sum.paragraphs[0]
    p_s.text = "MULTIMODAL FUSION RATIONALE:"
    p_s.font.size = Pt(12)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_NAVY
    
    p_s2 = tf_sum.add_paragraph()
    p_s2.text = "Skin appearance is used only as a complementary visual modality and is not presented as direct evidence of gastrointestinal disease. Combining visual features with structured clinical symptoms captures complementary biological markers for robust preliminary screening."
    p_s2.font.size = Pt(11)
    p_s2.font.color.rgb = COLOR_CHARCOAL
    
    add_footer(slide4, 4)

    # ==========================================
    # SLIDE 5: RESEARCH GAP & PROPOSED INNOVATION
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Research Gap & Proposed Innovation")
    
    # Table Left
    rows, cols = 5, 3
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(6.2), Inches(3.2)
    table_shape = slide5.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table
    
    headers = ["Approach", "Input Modality", "Main Focus"]
    data = [
        ["Tongue-based systems", "Tongue image / inquiry", "Tongue-based health assessment"],
        ["Tongue deep learning", "Tongue image only", "Visual classification"],
        ["Skin-image approaches", "Skin image + metadata", "Dermatology-oriented tasks"],
        ["PROPOSED FRAMEWORK", "Tongue + Skin + Symptoms", "Multimodal preliminary GI screening"]
    ]
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.text = h
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_NAVY
        
    for r_idx, row_data in enumerate(data):
        for c_idx, val in enumerate(row_data):
            cell = table.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            if r_idx == 3:
                p.font.bold = True
                p.font.color.rgb = COLOR_TEAL
            else:
                p.font.color.rgb = COLOR_CHARCOAL
                
    # 4 Innovation Pillars Right
    tb_inn = slide5.shapes.add_textbox(Inches(7.3), Inches(1.8), Inches(5.2), Inches(4.8))
    tf_inn = tb_inn.text_frame
    tf_inn.word_wrap = True
    
    innovations = [
        ("01 Multimodal Input", "Tongue image + skin image + symptoms + lifestyle"),
        ("02 Separate Feature Learning", "Appropriate model trained for each modality"),
        ("03 Feature Fusion", "Gated MLP combines complementary feature representations"),
        ("04 Screening Output", "Preliminary GI risk indication, not medical diagnosis")
    ]
    for i, (title, desc) in enumerate(innovations):
        p_t = tf_inn.paragraphs[0] if i == 0 else tf_inn.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEAL
        
        p_d = tf_inn.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_CHARCOAL
        p_d.space_after = Pt(6)
        
    add_footer(slide5, 5)

    # ==========================================
    # SLIDE 6: REAL DATASET STRATEGY
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Real Dataset Strategy")
    
    datasets_info = [
        ("TONGUE DATA", "TMC / TCM Tongue Diagnosis Dataset\n• 1,200 RGB Images (224x224)\n• 5 Classes: pale, light_red, red, deep_red, purple\n• Evaluates mucosal color & coating", COLOR_TEAL),
        ("SKIN DATA", "ISIC Dermatology Dataset\n• 1,500 Lesion & Skin Images\n• 5 Classes: benign, erythema, keratosis, vascular, melanocytic\n• Used as complementary visual modality", COLOR_BLUE),
        ("GI / CLINICAL DATA", "GI Symptoms & Lifestyle Dataset\n• 1,000 Patient Records\n• 15 Real Features (pain, reflux, fiber, stress, sleep, BMI)\n• Target: Low / Moderate / Higher Risk", COLOR_NAVY)
    ]
    
    for i, (title, desc, color) in enumerate(datasets_info):
        c_left = Inches(0.8 + i * 4.0)
        tb_d = slide6.shapes.add_textbox(c_left, Inches(1.8), Inches(3.7), Inches(4.8))
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
        
    add_footer(slide6, 6)

    # ==========================================
    # SLIDE 7: PROPOSED AI ARCHITECTURE
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Proposed AI Architecture")
    
    arch_img = os.path.join(DIAGRAM_DIR, "architecture.png")
    if os.path.exists(arch_img):
        slide7.shapes.add_picture(arch_img, Inches(0.8), Inches(1.8), width=Inches(11.7))
        
    add_footer(slide7, 7)

    # ==========================================
    # SLIDE 8: TRAINING & APPLICATION WORKFLOW
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Training & Application Workflow")
    
    pipe_img = os.path.join(DIAGRAM_DIR, "training_pipeline.png")
    if os.path.exists(pipe_img):
        slide8.shapes.add_picture(pipe_img, Inches(0.8), Inches(1.7), width=Inches(11.7))
        
    tb_wf = slide8.shapes.add_textbox(Inches(0.8), Inches(4.2), Inches(11.7), Inches(2.5))
    tf_wf = tb_wf.text_frame
    tf_wf.word_wrap = True
    
    p_hdr = tf_wf.paragraphs[0]
    p_hdr.text = "7-STEP USER APPLICATION WORKFLOW:"
    p_hdr.font.size = Pt(12)
    p_hdr.font.bold = True
    p_hdr.font.color.rgb = COLOR_NAVY
    
    wf_steps = [
        "1. Upload Tongue Image (TMC mucosal features)  |  2. Upload Skin Image (ISIC complementary visual signs)",
        "3. Enter GI Symptoms (pain, bloating, reflux)  |  4. Enter Lifestyle Data (dietary fiber, stress, sleep)",
        "5. AI Processes Inputs via FastAPI Service     |  6. Multimodal Feature Fusion (16-D vector concatenation)",
        "7. Display Preliminary Screening Result (Low / Moderate / Higher GI Risk)"
    ]
    for s in wf_steps:
        p = tf_wf.add_paragraph()
        p.text = f"• {s}"
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_before = Pt(4)
        
    add_footer(slide8, 8)

    # ==========================================
    # SLIDE 9: WORKING PROTOTYPE
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Working Prototype")
    
    tb_proto = slide9.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))
    tf_proto = tb_proto.text_frame
    tf_proto.word_wrap = True
    
    features = [
        ("Full-Stack Web Architecture", "FastAPI Python REST Backend + React & Tailwind CSS Web Dashboard."),
        ("Project Expo Demo Mode", "Pre-loaded research dataset profiles (Case A: Healthy, Case B: Moderate GERD, Case C: Suspected IBS) for seamless presentation."),
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
        
    add_footer(slide9, 9)

    # ==========================================
    # SLIDE 10: MODEL EVALUATION
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Model Evaluation & Results")
    
    rows, cols = 5, 4
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(6.5), Inches(3.2)
    table_shape = slide10.shapes.add_table(rows, cols, left, top, width, height)
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
                
    cm_img = os.path.join(BASE_DIR, "results", "fusion", "confusion_matrix.png")
    if os.path.exists(cm_img):
        slide10.shapes.add_picture(cm_img, Inches(7.6), Inches(1.8), width=Inches(4.8))
        
    add_footer(slide10, 10)

    # ==========================================
    # SLIDE 11: LIMITATIONS, SAFETY & FUTURE SCOPE
    # ==========================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Limitations, Clinical Safety & Future Scope")
    
    # Left Box: Limitations & Safety
    tb_lim = slide11.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    tf_lim = tb_lim.text_frame
    tf_lim.word_wrap = True
    
    p_lt = tf_lim.paragraphs[0]
    p_lt.text = "LIMITATIONS & CLINICAL SAFETY"
    p_lt.font.size = Pt(14)
    p_lt.font.bold = True
    p_lt.font.color.rgb = COLOR_RED
    
    limits = [
        "Independent Datasets: Public datasets exist in separate cohorts. Prototype fusion combines normalized embeddings.",
        "Clinical Validation Required: Full validation requires paired patient data under IRB ethical approval.",
        "Not a Medical Diagnosis: System triages preliminary risk; does not replace endoscopy or biopsy."
    ]
    for l in limits:
        p = tf_lim.add_paragraph()
        p.text = f"• {l}"
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_before = Pt(6)
        
    p_warn = tf_lim.add_paragraph()
    p_warn.text = "\nSCREENING SUPPORT ≠ MEDICAL DIAGNOSIS"
    p_warn.font.size = Pt(12)
    p_warn.font.bold = True
    p_warn.font.color.rgb = COLOR_RED
    
    # Right Box: Future Roadmap
    road_img = os.path.join(DIAGRAM_DIR, "roadmap.png")
    if os.path.exists(road_img):
        slide11.shapes.add_picture(road_img, Inches(6.8), Inches(1.8), width=Inches(5.7))
        
    tb_fut = slide11.shapes.add_textbox(Inches(6.8), Inches(3.8), Inches(5.7), Inches(2.8))
    tf_fut = tb_fut.text_frame
    tf_fut.word_wrap = True
    
    p_ft = tf_fut.paragraphs[0]
    p_ft.text = "FUTURE DEVELOPMENT ROADMAP"
    p_ft.font.size = Pt(14)
    p_ft.font.bold = True
    p_ft.font.color.rgb = COLOR_TEAL
    
    futures = [
        "1. Paired Clinical Dataset Collection (IRB Approval)",
        "2. Hospital & Gastroenterology Collaboration",
        "3. Mobile Native App Launch (Android / iOS)",
        "4. Prospective Clinical Evaluation & Validation"
    ]
    for f in futures:
        p = tf_fut.add_paragraph()
        p.text = f
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_before = Pt(4)
        
    add_footer(slide11, 11)

    # ==========================================
    # SLIDE 12: POTENTIAL IMPACT & THANK YOU
    # ==========================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "", is_title_slide=True)
    
    tb_imp = slide12.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.2))
    tf_imp = tb_imp.text_frame
    tf_imp.word_wrap = True
    
    p_it = tf_imp.paragraphs[0]
    p_it.text = "POTENTIAL IMPACT:"
    p_it.font.size = Pt(14)
    p_it.font.bold = True
    p_it.font.color.rgb = COLOR_TEAL
    
    impacts = [
        "• Accessible: Smartphone-based preliminary screening accessible outside tertiary centers.",
        "• Non-Invasive: Readily obtainable visual images and self-reported questionnaires.",
        "• Multimodal: Combines visual mucosal cues, skin signs, and clinical lifestyle data.",
        "• Decision Support: May help identify individuals needing secondary clinical evaluation."
    ]
    for imp in impacts:
        p = tf_imp.add_paragraph()
        p.text = imp
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CHARCOAL
        p.space_before = Pt(2)
        
    # Thank you bottom block
    tb_ty = slide12.shapes.add_textbox(Inches(0.8), Inches(4.0), Inches(11.7), Inches(2.5))
    tf_ty = tb_ty.text_frame
    
    p_ty = tf_ty.paragraphs[0]
    p_ty.text = "THANK YOU"
    p_ty.font.size = Pt(36)
    p_ty.font.bold = True
    p_ty.font.color.rgb = COLOR_NAVY
    p_ty.alignment = PP_ALIGN.CENTER
    
    p_q = tf_ty.add_paragraph()
    p_q.text = "Questions & Discussion"
    p_q.font.size = Pt(18)
    p_q.font.color.rgb = COLOR_TEAL
    p_q.alignment = PP_ALIGN.CENTER
    p_q.space_before = Pt(4)
    
    p_by = tf_ty.add_paragraph()
    p_by.text = "Presented by: Vishnu Priya S  &  Nithika R\nDepartment of Biomedical Engineering | Sona College of Technology"
    p_by.font.size = Pt(13)
    p_by.font.bold = True
    p_by.font.color.rgb = COLOR_NAVY
    p_by.alignment = PP_ALIGN.CENTER
    p_by.space_before = Pt(8)
    
    add_footer(slide12, 12)

    prs.save(OUTPUT_PATH)
    print(f"12-SLIDE POWERPOINT PRESENTATION GENERATED SUCCESSFULLY AT: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_12slide_presentation()
