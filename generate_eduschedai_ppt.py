import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_eduschedai_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette - Academic Navy & Modern Tech
    NAVY_DARK = RGBColor(15, 23, 42)      # #0f172a
    NAVY_CARD = RGBColor(30, 41, 59)      # #1e293b
    BLUE_ACCENT = RGBColor(37, 99, 235)   # #2563eb
    CYAN_ACCENT = RGBColor(6, 182, 212)   # #06b6d4
    TEXT_LIGHT = RGBColor(248, 250, 252)  # #f8fafc
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94a3b8
    WHITE = RGBColor(255, 255, 255)
    GREEN_ACCENT = RGBColor(16, 185, 129) # #10b981
    AMBER_ACCENT = RGBColor(245, 158, 11) # #f59e0b

    def add_blank_slide():
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)
        # Background fill
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = NAVY_DARK
        bg.line.fill.background()
        return slide

    def add_header(slide, title_text, category_text=""):
        # Category / Chapter Tag
        if category_text:
            cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
            tf_cat = cat_box.text_frame
            tf_cat.word_wrap = True
            p_cat = tf_cat.paragraphs[0]
            p_cat.text = category_text.upper()
            p_cat.font.size = Pt(11)
            p_cat.font.bold = True
            p_cat.font.color.rgb = CYAN_ACCENT

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf = t_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT

        # Subtle bottom line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(51, 65, 85)
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=NAVY_CARD, border_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.5)
        else:
            card.line.color.rgb = RGBColor(51, 65, 85)
            card.line.width = Pt(1)
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = add_blank_slide()

    # Decorative header banner
    tag_box = s1.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.3), Inches(0.4))
    tf1 = tag_box.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "EASWARI ENGINEERING COLLEGE (AUTONOMOUS) • ANNA UNIVERSITY, CHENNAI"
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = CYAN_ACCENT

    # Main Project Title
    title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.3), Inches(1.8))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    pt = tf_t.paragraphs[0]
    pt.text = "EduSchedAI"
    pt.font.size = Pt(44)
    pt.font.bold = True
    pt.font.color.rgb = TEXT_LIGHT

    pt_sub = tf_t.add_paragraph()
    pt_sub.text = "Intelligent Timetable and Faculty Workload Management System"
    pt_sub.font.size = Pt(22)
    pt_sub.font.color.rgb = RGBColor(147, 197, 253)

    # Details Card Left (Candidate & Degree)
    c_left = add_card(s1, Inches(1.0), Inches(3.6), Inches(5.4), Inches(2.8), bg_color=NAVY_CARD)
    tb_c1 = s1.shapes.add_textbox(Inches(1.2), Inches(3.8), Inches(5.0), Inches(2.4))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True

    p = tf_c1.paragraphs[0]
    p.text = "PROJECT CANDIDATE"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p = tf_c1.add_paragraph()
    p.text = "SANTHANAKUMAR S"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p = tf_c1.add_paragraph()
    p.text = "Register Number: 310624243161\nDegree: Bachelor of Technology (B.Tech)\nDepartment of Artificial Intelligence and Data Science"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED

    # Details Card Right (Guide & Institution)
    c_right = add_card(s1, Inches(6.8), Inches(3.6), Inches(5.5), Inches(2.8), bg_color=NAVY_CARD)
    tb_c2 = s1.shapes.add_textbox(Inches(7.0), Inches(3.8), Inches(5.1), Inches(2.4))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True

    p = tf_c2.paragraphs[0]
    p.text = "ACADEMIC SUPERVISION & VIVA"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p = tf_c2.add_paragraph()
    p.text = "Supervisor: Ms. D. S. K. Harshitha"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p = tf_c2.add_paragraph()
    p.text = "Head of the Department: Dr. T. Kalai Selvi\nPrincipal: Dr. P. Deiva Sundari\nExamination Date: 28.10.2026 | Academic Year: 2026"
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED

    # Speaker notes
    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected external examiner, internal examiner, and guides. "
        "I am Santhanakumar S, presenting my final project titled EduSchedAI: Intelligent Timetable and Faculty Workload Management System."
    )

    # =========================================================================
    # SLIDE 2: EXECUTIVE SUMMARY & PROBLEM STATEMENT
    # =========================================================================
    s2 = add_blank_slide()
    add_header(s2, "Executive Problem Statement & Challenges", "Chapter 1 • Introduction & Problem Definition")

    # 3 Cards Layout
    cards_data = [
        ("1. NP-Hard Combinatorial Problem", 
         "• Placing dozens of course sessions across 5 days, 8 periods, multiple faculty and lab venues is mathematically NP-hard.\n• Manual generation takes days to weeks each semester.\n• Explores very few alternatives, leaving suboptimal arrangements.",
         AMBER_ACCENT),
        ("2. Undetected Clashes & Violations",
         "• Hidden double-booking of faculty, room venues, or student batches.\n• Continuous 2-hour lab slots and specialized venues frequently overlooked.\n• Manual spreadsheets lack real-time constraint verification.",
         RGBColor(239, 68, 68)),
        ("3. Unfair Workload & Disruptive Leave",
         "• Cadre-based workload (Prof: 14h, Assoc: 16h, Asst: 18h) rarely tracked objectively.\n• When faculty takes sudden leave, traditional systems require regenerating the entire timetable, disturbing all batches.",
         CYAN_ACCENT)
    ]

    for i, (head, body, acc) in enumerate(cards_data):
        x = Inches(0.8 + i * 4.0)
        c = add_card(s2, x, Inches(1.8), Inches(3.7), Inches(4.9), border_color=acc)
        tb = s2.shapes.add_textbox(x + Inches(0.2), Inches(2.0), Inches(3.3), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = head
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = acc

        p_b = tf.add_paragraph()
        p_b.text = body
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_LIGHT

    s2.notes_slide.notes_text_frame.text = (
        "The problem originates from the fact that educational timetabling is NP-hard. Manual creation in Excel takes days and causes teacher conflicts, lab venue clashes, and unequal teaching loads. When an instructor goes on leave, finding a replacement manually disrupts the whole department."
    )

    # =========================================================================
    # SLIDE 3: OBJECTIVES OF EDUSCHEDAI
    # =========================================================================
    s3 = add_blank_slide()
    add_header(s3, "Project Objectives & Success Benchmarks", "Chapter 1 • Proposed Solution Goals")

    objs = [
        ("Zero Hard Clashes Guaranteed", "Solve timetable as a Constraint Satisfaction Problem (CSP) ensuring 100% clash-free schedules (faculty, venue, batch, lab continuity)."),
        ("Multi-Criteria Optimization", "Apply heuristic local search & evolutionary optimization to minimize student idle gaps and teacher waiting windows."),
        ("Objective Workload Equity (Gini < 0.24)", "Track departmental teaching fairness with Gini Index and benchmark against cadre targets (14h, 16h, 18h)."),
        ("Dynamic 1-Click Leave Substitution", "Rank available, subject-qualified substitutes by lowest current workload without regenerating the master timetable."),
        ("Interactive Click-to-Swap Grid", "Enable coordinators to make live session swaps with instant conflict validation and visual feedback."),
        ("Sub-2-Second Solver Performance", "Generate full multi-batch 56-period timetable in under 1.5 seconds, replacing 3-5 days of manual labor.")
    ]

    for i, (title, desc) in enumerate(objs):
        row = i // 2
        col = i % 2
        x = Inches(0.8 + col * 5.95)
        y = Inches(1.8 + row * 1.65)
        
        c = add_card(s3, x, y, Inches(5.75), Inches(1.45))
        tb = s3.shapes.add_textbox(x + Inches(0.2), y + Inches(0.15), Inches(5.35), Inches(1.15))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"✔  {title}"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = GREEN_ACCENT

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_LIGHT

    s3.notes_slide.notes_text_frame.text = (
        "Our system has six core objectives: 100% clash-free scheduling using CSP, soft-constraint optimization, workload balancing with Gini Index below 0.24, instantaneous 1-click substitution, interactive manual editing, and high-speed generation under 1.5 seconds."
    )

    # =========================================================================
    # SLIDE 4: LITERATURE SURVEY & BENCHMARKING
    # =========================================================================
    s4 = add_blank_slide()
    add_header(s4, "Literature Review & Comparative Analysis", "Chapter 2 • State-of-the-Art vs EduSchedAI")

    # Table layout
    rows, cols = 7, 3
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9)
    table_shape = s4.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table

    tbl.columns[0].width = Inches(2.8)
    tbl.columns[1].width = Inches(4.3)
    tbl.columns[2].width = Inches(4.633)

    headers = ["Evaluation Metric", "Legacy Tools (FET / UniTime / Excel)", "EduSchedAI (Proposed Modern MERN)"]
    for c_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h_text
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_CARD
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = CYAN_ACCENT

    table_data = [
        ("Architecture & UI", "Outdated Qt desktop app / dense Java tables", "Cloud-native responsive SPA (React + Tailwind CSS)"),
        ("Solver Execution Speed", "Several minutes to hours on complex constraints", "1.1 seconds for 56 periods (100% clash-free)"),
        ("Workload Equity Tracking", "Basic unmeasured weekly limits", "Dedicated Workload Balancer with Gini Index (< 0.24)"),
        ("Faculty Leave Handling", "Requires full timetable regeneration", "Dynamic Leave & Substitution Finder without full regeneration"),
        ("Interactive Editing", "Static grid with high risk of human error", "Click-to-Swap modal with real-time clash verification"),
        ("Multi-Role Access Control", "Single-user or complex enterprise setup", "4-Tier RBAC: HOD, Class Coordinator, Faculty, Student")
    ]

    for r_idx, row_values in enumerate(table_data):
        for c_idx, val in enumerate(row_values):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(15, 23, 42) if r_idx % 2 == 0 else NAVY_CARD
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            if c_idx == 2:
                p.font.bold = True
                p.font.color.rgb = GREEN_ACCENT
            else:
                p.font.color.rgb = TEXT_LIGHT

    s4.notes_slide.notes_text_frame.text = (
        "Comparing with legacy tools like FET and UniTime: FET is desktop-only and UniTime is heavy to configure. Both require full regeneration on faculty leave. EduSchedAI solves this with cloud architecture, sub-second generation, Gini workload index, and instant local substitute ranking."
    )

    # =========================================================================
    # SLIDE 5: SYSTEM ARCHITECTURE
    # =========================================================================
    s5 = add_blank_slide()
    add_header(s5, "5-Layered System Architecture", "Chapter 4 • System Design & Methodology")

    layers = [
        ("1. Presentation Layer (Port 3050)", "React.js 18 + Tailwind CSS SPA • Executive Dashboard, Interactive Timetable, AI Studio, Workload Balancer, Leave Portal, Role Switcher"),
        ("2. API & Security Gateway (Port 5050)", "Express.js REST API • JWT Authentication, BCrypt Password Hashing, Role-Based Route Guards, Input Validation & Sanitization"),
        ("3. Scheduling & Business Core", "Hybrid CSP Solver with MRV & Forward Checking • Local Search & Evolutionary Optimizer • Real-Time Constraint Checker • Gini Index Engine"),
        ("4. Data Access Layer (DAL)", "Data Models: Users, Faculty, Batches (CSE A/B), Subjects, Venues/Rooms, TimetableSlots, LeaveRequests, Substitutions"),
        ("5. Persistence Layer (Database)", "MongoDB Document Store • Pre-seeded sample dataset: 2 batches, 12 faculty members across 3 cadres, 8 specialized venues")
    ]

    for i, (layer_title, layer_desc) in enumerate(layers):
        y = Inches(1.8 + i * 1.0)
        c = add_card(s5, Inches(0.8), y, Inches(11.733), Inches(0.85), border_color=BLUE_ACCENT if i == 2 else None)
        tb = s5.shapes.add_textbox(Inches(1.0), y + Inches(0.08), Inches(11.3), Inches(0.68))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = layer_title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT if i == 2 else TEXT_LIGHT

        p2 = tf.add_paragraph()
        p2.text = layer_desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

    s5.notes_slide.notes_text_frame.text = (
        "EduSchedAI adopts a decoupled 5-tier architecture: React single page application communicating with Express.js REST API, which triggers our hybrid scheduling core. The data access layer maps models into MongoDB."
    )

    # =========================================================================
    # SLIDE 6: 4-TIER USER HIERARCHY & WORKFLOW
    # =========================================================================
    s6 = add_blank_slide()
    add_header(s6, "Institutional User Hierarchy & Role Workflow", "Chapter 4 • Role-Based Access Control (RBAC)")

    roles = [
        ("Head of Department (HOD)", "Master Admin", 
         "• Generates and publishes master timetable via AI Engine.\n• Adjusts soft-constraint optimization weights.\n• Creates faculty profiles & sets credentials.\n• Appoints Class Coordinators for sections.\n• Approves emergency leaves & substitutions.",
         RGBColor(168, 85, 247)),
        ("Class Coordinator", "Batch Manager", 
         "• Enrolls students for specific section (e.g. CSE-A).\n• Configures student credentials and batch subjects.\n• Monitors section timetable and room availability.\n• Reports venue or faculty scheduling issues.",
         BLUE_ACCENT),
        ("Regular Faculty", "Instructor", 
         "• Views personal weekly timetable and teaching venues.\n• Monitors individual teaching hours against cadre target.\n• Applies for leave with reason and period.\n• Receives substitution requests and alerts.",
         GREEN_ACCENT),
        ("Student", "Learner", 
         "• Views real-time clash-free weekly timetable.\n• Checks lecture halls, lab venues, and timing.\n• Views Class Coordinator contact details.\n• Sees real-time substitution announcements.",
         AMBER_ACCENT)
    ]

    for i, (r_name, r_badge, r_pts, col_accent) in enumerate(roles):
        x = Inches(0.8 + i * 3.0)
        c = add_card(s6, x, Inches(1.8), Inches(2.8), Inches(4.9), border_color=col_accent)
        tb = s6.shapes.add_textbox(x + Inches(0.15), Inches(1.95), Inches(2.5), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = r_name
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = col_accent

        p_b = tf.add_paragraph()
        p_b.text = f"[{r_badge}]"
        p_b.font.size = Pt(11)
        p_b.font.bold = True
        p_b.font.color.rgb = TEXT_MUTED

        p_desc = tf.add_paragraph()
        p_desc.text = r_pts
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = TEXT_LIGHT

    s6.notes_slide.notes_text_frame.text = (
        "Our system reflects authentic college administration: HOD has master privilege to run AI solver and assign coordinators. Class Coordinators manage students. Faculty access their personal load, and students view their section's schedule with live substitution notices."
    )

    # =========================================================================
    # SLIDE 7: HYBRID SCHEDULING ALGORITHM (CSP + LOCAL SEARCH)
    # =========================================================================
    s7 = add_blank_slide()
    add_header(s7, "Hybrid Scheduling Engine: Mathematical Formulation", "Chapter 4 • Core Algorithm & Optimization")

    # Left Column: Formulation & CSP
    c_left = add_card(s7, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tb_l = s7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "Phase 1: CSP Construction (Feasibility)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p = tf_l.add_paragraph()
    p.text = (
        "• Variables (X): Course sessions to be scheduled (56 periods).\n"
        "• Domains (D): Cartesian product of (Day, Period, Room, Faculty).\n"
        "• Heuristic Ordering: Most Constrained Variable (MRV) first:\n"
        "   - 2-hour continuous Laboratory blocks placed first in Lab venues.\n"
        "   - Faculty with limited free periods scheduled early.\n"
        "• Forward Checking & Backtracking: Prunes invalid domains instantly.\n"
        "• Outcome: 100% clash-free starting timetable in < 200ms."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LIGHT

    # Right Column: Local Search & Cost Function
    c_r = add_card(s7, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.9))
    tb_r = s7.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.333), Inches(4.5))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "Phase 2: Local Search Optimization"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf_r.add_paragraph()
    p.text = (
        "Objective Function Minimized:\n"
        "Cost = 1000 × HardClashes + w1 × Gini(Workload) +\n"
        "        w2 × StudentIdleGaps + w3 × FacultyWaitingWindows\n\n"
        "• Weights (w1, w2, w3) are dynamically tunable via AI Studio sliders.\n"
        "• Evolutionary Step: Generates neighbor via session swaps/moves.\n"
        "• Acceptance Criteria: Accept move if HardClashes == 0 and cost improves.\n"
        "• Converges to optimal soft-constraint score in ~1000 iterations."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LIGHT

    s7.notes_slide.notes_text_frame.text = (
        "The algorithm uses a two-phase hybrid approach: Phase 1 models the timetable as CSP with MRV heuristic to guarantee zero hard clashes. Phase 2 applies evolutionary local search to minimize the cost function which balances faculty workload, student idle gaps, and teacher waiting windows."
    )

    # =========================================================================
    # SLIDE 8: HARD & SOFT CONSTRAINTS SPECIFICATION
    # =========================================================================
    s8 = add_blank_slide()
    add_header(s8, "Comprehensive Constraints Matrix", "Chapter 4 • Table 4.2 Constraints Analysis")

    rows, cols = 8, 3
    left, top, width, height = Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9)
    table_shape = s8.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table

    tbl.columns[0].width = Inches(1.8)
    tbl.columns[1].width = Inches(5.5)
    tbl.columns[2].width = Inches(4.433)

    headers = ["Constraint Type", "Constraint Description", "Enforcement Strategy"]
    for c_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.text = h_text
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY_CARD
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = CYAN_ACCENT

    cons_data = [
        ("HARD", "Faculty No-Clash: Faculty cannot teach 2 classes in same period", "Solver domain filtering; strictly 0 violations"),
        ("HARD", "Room No-Clash: Venue cannot host multiple classes simultaneously", "Venue lock during slot assignment"),
        ("HARD", "Batch No-Clash: Student section cannot attend 2 sessions at once", "Strict temporal slot exclusivity per batch"),
        ("HARD", "Lab Block Continuity: 2-hour practicals require continuous periods", "Atomic 2-period placement in specialized lab rooms"),
        ("HARD", "Institutional Lunch Break: Period 4 reserved exclusively for lunch", "Removed from variable domain space"),
        ("SOFT", "Faculty Cadre Target Equity: Prof (14h), Assoc (16h), Asst (18h)", "Gini Index penalty minimization (w1 slider)"),
        ("SOFT", "Student Idle Gaps & Teacher Waiting Windows", "Penalizes scattered isolated sessions (w2 & w3 sliders)")
    ]

    for r_idx, (c_type, c_desc, c_enf) in enumerate(cons_data):
        for c_idx, val in enumerate([c_type, c_desc, c_enf]):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(15, 23, 42) if r_idx % 2 == 0 else NAVY_CARD
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(11)
            if c_idx == 0:
                p.font.bold = True
                p.font.color.rgb = RGBColor(239, 68, 68) if val == "HARD" else GREEN_ACCENT
            else:
                p.font.color.rgb = TEXT_LIGHT

    s8.notes_slide.notes_text_frame.text = (
        "Here is our complete constraint catalog. Hard constraints like faculty, venue, and batch double-booking are never violated. Continuous 2-hour laboratory blocks and lunch break are enforced strictly. Soft constraints optimize teacher workload and eliminate student idle gaps."
    )

    # =========================================================================
    # SLIDE 9: WORKLOAD BALANCER & GINI INDEX FORMULATION
    # =========================================================================
    s9 = add_blank_slide()
    add_header(s9, "Faculty Workload Balancing & Gini Metric", "Chapter 5 • Workload Equity & Audit Engine")

    # Formula Box
    c_f = add_card(s9, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.3), border_color=CYAN_ACCENT)
    tb_f = s9.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.1))
    tf_f = tb_f.text_frame
    tf_f.word_wrap = True

    p = tf_f.paragraphs[0]
    p.text = "Mathematical Gini Coefficient Formulation for Departmental Workload:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p_f = tf_f.add_paragraph()
    p_f.text = "G = ( ∑ ∑ | x_i  -  x_j | )  /  ( 2 × n² × μ )        [ Target Benchmark: G < 0.24 ]"
    p_f.font.size = Pt(18)
    p_f.font.bold = True
    p_f.font.color.rgb = WHITE

    # 3 Stat Cards Below
    stats = [
        ("Professor Cadre Target", "14 Hours / Week", "Balanced allocation for senior faculty allowing research and PhD guidance.", BLUE_ACCENT),
        ("Associate Professor Target", "16 Hours / Week", "Equitable balance between core theory teaching and lab mentorship.", GREEN_ACCENT),
        ("Assistant Professor Target", "18 Hours / Week", "Standard instructional load with lab session allocations.", AMBER_ACCENT)
    ]

    for i, (title, hrs, desc, acc) in enumerate(stats):
        x = Inches(0.8 + i * 4.0)
        c = add_card(s9, x, Inches(3.3), Inches(3.7), Inches(3.4), border_color=acc)
        tb = s9.shapes.add_textbox(x + Inches(0.2), Inches(3.5), Inches(3.3), Inches(3.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT

        p_h = tf.add_paragraph()
        p_h.text = hrs
        p_h.font.size = Pt(22)
        p_h.font.bold = True
        p_h.font.color.rgb = acc

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MUTED

    s9.notes_slide.notes_text_frame.text = (
        "Unlike existing timetabling systems that treat faculty hours generically, we adopted the economic Gini coefficient to measure workload inequality. We normalize hours against cadre benchmarks of 14, 16, and 18 hours. In our prototype, Gini Index is 0.238, well below the target 0.24 threshold."
    )

    # =========================================================================
    # SLIDE 10: DYNAMIC LEAVE & 1-CLICK SUBSTITUTION FINDER
    # =========================================================================
    s10 = add_blank_slide()
    add_header(s10, "Dynamic Leave & Instant Substitution Engine", "Chapter 5 • Zero-Regeneration Fault Tolerance")

    c1 = add_card(s10, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tb1 = s10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Traditional Timetable vs EduSchedAI"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)

    p = tf1.add_paragraph()
    p.text = (
        "• Legacy Limitation:\n"
        "   When a teacher takes emergency sick leave, existing tools require re-running the solver, disturbing all 56 class slots across the entire department.\n\n"
        "• EduSchedAI Innovation:\n"
        "   Zero-regeneration localized repair. The master timetable remains 100% stable; only the affected period is reassigned algorithmically."
    )
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_LIGHT

    c2 = add_card(s10, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.9))
    tb2 = s2.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.333), Inches(4.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "3-Step Algorithmic Ranking Process"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf2.add_paragraph()
    p.text = (
        "1. Temporal Free Slot Filter:\n"
        "   Isolate only faculty who have no active class or lab during that exact day & period.\n\n"
        "2. Subject Qualification Verification:\n"
        "   Check teacher's qualified subject matrix to ensure curriculum competence.\n\n"
        "3. Workload-Priority Ranking:\n"
        "   Rank candidates ascending by (Current Hours / Cadre Target). Teachers with the lowest workload appear at the top for 1-click allocation."
    )
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_LIGHT

    s10.notes_slide.notes_text_frame.text = (
        "Our dynamic substitution module is a major practical breakthrough. Instead of regenerating the entire timetable when an instructor is absent, EduSchedAI filters all free teachers, verifies subject competence, and ranks them by lowest current workload for 1-click assignment."
    )

    # =========================================================================
    # SLIDE 11: KEY RESULTS OF IMPLEMENTED PROTOTYPE
    # =========================================================================
    s11 = add_blank_slide()
    add_header(s11, "Experimental Results & Benchmark Telemetry", "Chapter 5 • Table 5.1 Performance Findings")

    # 4 Key metrics
    results = [
        ("0", "Hard Clashes", "Guaranteed zero double-booking across all batches & venues", GREEN_ACCENT),
        ("1.1s", "Generation Time", "Computed 56 periods across 2 sections in 1100 milliseconds", CYAN_ACCENT),
        ("0.238", "Gini Fairness Index", "Successfully achieved target G < 0.24 ensuring equal teaching load", BLUE_ACCENT),
        ("73.2%", "Fairness Score", "Measured against AICTE / UGC cadre benchmarks across department", AMBER_ACCENT)
    ]

    for i, (val, label, sub, col_acc) in enumerate(results):
        x = Inches(0.8 + i * 3.0)
        c = add_card(s11, x, Inches(1.8), Inches(2.8), Inches(2.1), border_color=col_acc)
        tb = s11.shapes.add_textbox(x + Inches(0.15), Inches(1.9), Inches(2.5), Inches(1.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = val
        p.font.size = Pt(32)
        p.font.bold = True
        p.font.color.rgb = col_acc

        p_l = tf.add_paragraph()
        p_l.text = label
        p_l.font.size = Pt(14)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_LIGHT

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(10)
        p_s.font.color.rgb = TEXT_MUTED

    # Bottom summary card
    c_b = add_card(s11, Inches(0.8), Inches(4.2), Inches(11.733), Inches(2.5))
    tb_b = s11.shapes.add_textbox(Inches(1.0), Inches(4.4), Inches(11.333), Inches(2.1))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    p = tf_b.paragraphs[0]
    p.text = "Prototype Testbed Configuration"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p = tf_b.add_paragraph()
    p.text = (
        "• Academic Batches: 2 Sections (CSE Section A & CSE Section B) with 60 students each.\n"
        "• Faculty Pool: 12 Faculty Members across Professor, Associate Professor, and Assistant Professor cadres.\n"
        "• Campus Venues: 8 Dedicated Venues (Lecture Halls, AI Computing Labs, Hardware IoT Labs).\n"
        "• Weekly Sessions Scheduled: 56 Periods (Core Theory, 2-Hour Practical Lab Sessions, Lunch Breaks).\n"
        "• Verification: 10 Comprehensive Test Scenarios executed; 100% Pass Rate recorded."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LIGHT

    s11.notes_slide.notes_text_frame.text = (
        "In our prototype evaluation with 12 faculty and 2 batches: the engine generated 56 periods in 1.1 seconds with exactly zero clashes. The Gini Index achieved was 0.238, proving equitable distribution."
    )

    # =========================================================================
    # SLIDE 12: USER INTERFACE & FEATURE MODULES
    # =========================================================================
    s12 = add_blank_slide()
    add_header(s12, "Core Functional UI Modules", "Chapter 4 & Appendix • Modern Web Portal")

    ui_modules = [
        ("Executive Dashboard", "Real-time KPI metrics (0 clashes, Gini 0.238, active faculty count, total sessions) with 1-click re-generation banner."),
        ("Master Timetable", "Multi-filter view (by Batch, Faculty, Room) with color-coded theory (indigo) and 2-hour laboratory blocks (emerald)."),
        ("Click-to-Swap Editor", "Interactive manual slot swapping with instant backend conflict detection and rejection of double-booking attempts."),
        ("AI Scheduling Studio", "Dynamic weight sliders (w1 Workload, w2 Student Gaps, w3 Faculty Wait) with live solver runtime telemetry."),
        ("Workload Balancer", "Departmental equity gauge, cadre target comparison charts, and individual faculty allocation status progress bars."),
        ("Academic Directory", "Centralized repository of lecture halls, specialized laboratories, curricula, credit structures, and weekly lecture quotas.")
    ]

    for i, (m_title, m_desc) in enumerate(ui_modules):
        r = i // 2
        c = i % 2
        x = Inches(0.8 + c * 5.95)
        y = Inches(1.8 + r * 1.65)
        
        card = add_card(s12, x, y, Inches(5.75), Inches(1.45))
        tb = s12.shapes.add_textbox(x + Inches(0.2), y + Inches(0.15), Inches(5.35), Inches(1.15))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"💻  {m_title}"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

        p2 = tf.add_paragraph()
        p2.text = m_desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_LIGHT

    s12.notes_slide.notes_text_frame.text = (
        "The web interface includes six intuitive modules: the Executive Dashboard, Master Timetable with multi-perspective views, Click-to-Swap editor, AI Studio for weight tuning, Faculty Workload Balancer, and the Academic Resources Directory."
    )

    # =========================================================================
    # SLIDE 13: CONCLUSION & FUTURE ENHANCEMENTS
    # =========================================================================
    s13 = add_blank_slide()
    add_header(s13, "Conclusion & Future Research Roadmap", "Chapter 6 • Research Contributions")

    c1 = add_card(s13, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
    tb1 = s13.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Key Research Contributions"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf1.add_paragraph()
    p.text = (
        "• Solved NP-Hard Timetabling: Successfully combined CSP and evolutionary local search for educational scheduling.\n\n"
        "• 100% Conflict-Free: Zero double-booking of rooms, teachers, or batches with continuous laboratory allocation.\n\n"
        "• Objective Fairness: Integrated economic Gini coefficient for academic workload balancing (G = 0.238).\n\n"
        "• Zero-Regeneration Substitution: Ranked emergency substitute allocation without disturbing unaffected sessions."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LIGHT

    c2 = add_card(s13, Inches(6.8), Inches(1.8), Inches(5.733), Inches(4.9))
    tb2 = s13.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.333), Inches(4.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "Future Enhancements"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p = tf2.add_paragraph()
    p.text = (
        "1. Multi-Campus & Cross-Department Scaling: Sharing laboratory venues and inter-disciplinary faculty across schools.\n\n"
        "2. Examination Timetabling & Invigilation: Reusing the constraint engine for exam scheduling and hall invigilator rosters.\n\n"
        "3. Preference Deep Learning: Learning faculty and student time preferences from historical timetable patterns.\n\n"
        "4. Mobile Notifications & Push Alerts: Instant WhatsApp/SMS alerts for substitution updates and room swaps."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_LIGHT

    s13.notes_slide.notes_text_frame.text = (
        "In conclusion, EduSchedAI demonstrates that NP-hard timetabling can be solved practically and equitably in a modern cloud web app. Our future roadmap includes cross-department scaling, exam invigilation duty scheduling, and mobile push notifications."
    )

    # =========================================================================
    # SLIDE 14: THANK YOU & VIVA Q&A DEFENSE
    # =========================================================================
    s14 = add_blank_slide()

    c_center = add_card(s14, Inches(2.0), Inches(1.5), Inches(9.333), Inches(4.5), border_color=BLUE_ACCENT)
    tb_c = s14.shapes.add_textbox(Inches(2.5), Inches(1.8), Inches(8.333), Inches(3.9))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "Thank You!"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p_sub = tf_c.add_paragraph()
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.text = "EduSchedAI: Intelligent Timetable and Faculty Workload Management System"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = CYAN_ACCENT

    p_div = tf_c.add_paragraph()
    p_div.alignment = PP_ALIGN.CENTER
    p_div.text = "─" * 40
    p_div.font.size = Pt(14)
    p_div.font.color.rgb = RGBColor(71, 85, 105)

    p_can = tf_c.add_paragraph()
    p_can.alignment = PP_ALIGN.CENTER
    p_can.text = "Candidate: Santhanakumar S (Reg No: 310624243161)\nDepartment of Artificial Intelligence & Data Science\nEaswari Engineering College (Autonomous), Anna University"
    p_can.font.size = Pt(13)
    p_can.font.color.rgb = TEXT_LIGHT

    p_live = tf_c.add_paragraph()
    p_live.alignment = PP_ALIGN.CENTER
    p_live.text = "Live Deployment: https://eduschedai-1.onrender.com"
    p_live.font.size = Pt(12)
    p_live.font.bold = True
    p_live.font.color.rgb = GREEN_ACCENT

    p_q = tf_c.add_paragraph()
    p_q.alignment = PP_ALIGN.CENTER
    p_q.text = "Questions & Project Defense"
    p_q.font.size = Pt(16)
    p_q.font.bold = True
    p_q.font.color.rgb = AMBER_ACCENT

    s14.notes_slide.notes_text_frame.text = (
        "Thank you examiners and faculty. I am now open to your questions and ready to demonstrate the live application."
    )

    output_path = "C:/Users/Ranji/.gemini/antigravity/scratch/leave-attendance-app/EduSchedAI_Project_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == '__main__':
    create_eduschedai_presentation()
