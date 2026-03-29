from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def generate_pdf(data, filename="FootprintX_Intel_Report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- PAGE 1: THE COVER (Start-up Branding) ---
    c.setFillColor(colors.HexColor("#01080e"))
    c.rect(0, 0, width, height, fill=1)
    
    # White "FOOTPRINT" Red "X" Branding
    c.setFont("Helvetica-Bold", 40)
    c.setFillColor(colors.white)
    c.drawString(50, height-200, "FOOTPRINT")
    c.setFillColor(colors.HexColor("#ff0055"))
    c.drawString(305, height-200, "X")
    
    c.setFillColor(colors.lightgrey)
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(50, height-230, '"Where Privacy Meets Intelligence"')
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.white)
    c.drawString(50, 400, "OFFICIAL IDENTITY RISK INTELLIGENCE REPORT")
    c.setFont("Helvetica", 10)
    c.drawString(50, 380, f"SUBJECT IDENTIFIER: {data['name'].upper()}")
    c.drawString(50, 365, f"DATA VECTOR: {data['email']}")
    c.drawString(50, 350, f"GENERATED AT: {timestamp}")
    
    # SDG Compliance footer on cover
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(colors.HexColor("#00d4ff"))
    c.drawString(50, 50, "COMPLIANT WITH UN SUSTAINABLE DEVELOPMENT GOALS: SDG 9 (INNOVATION) & SDG 16 (PEACE & JUSTICE)")
    c.showPage()

    # --- PAGE 2: THE HPBS & RISK TWIN ---
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height-50, "1.0 HUMAN PRIVACY BEHAVIOR SCORE (HPBS)")
    
    # Score Visualization
    score = int(data['score'])
    score_color = colors.HexColor("#ff0055") if score < 50 else colors.green
    c.setStrokeColor(colors.lightgrey)
    c.rect(50, height-120, 500, 40)
    c.setFillColor(score_color)
    c.rect(50, height-120, (score/100)*500, 40, fill=1)
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, height-108, f"CURRENT SCORE: {score}/100")

    # Risk Twin Explanation
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height-160, "1.1 DIGITAL RISK TWIN ANALYSIS")
    c.setFont("Helvetica", 10)
    risk_text = [
        f"Level: {data['risk_level']}",
        f"Attack Vector Detected: {data['vector']}",
        "Analysis: Based on SOCMINT (Social Media Intelligence) probing, your digital shadow",
        "has high correlation. Attackers can simulate your identity for social engineering."
    ]
    y = height-180
    for line in risk_text:
        c.drawString(60, y, f"> {line}")
        y -= 15

    # --- PAGE 3: TECHNICAL FINDINGS & PREVENTION ---
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y-40, "2.0 OSINT PROBE FINDINGS (DORKING & SOCMINT)")
    
    findings = [
        f"Visual Exposure (Photos): {data['photos']}",
        f"Geographic Tracking (Metadata): {data['location']}",
        f"Historical Data Breaches: {data['breach_intel']} verified leaks found in database scan."
    ]
    y -= 65
    for f in findings:
        c.drawString(70, y, f"● {f}")
        y -= 20

    # Business Weakest-Link Section
    c.setFillColor(colors.HexColor("#f0f0f0"))
    c.rect(50, y-80, 500, 60, fill=1)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, y-40, "BUSINESS IMPACT: WEAKEST-LINK MAPPING")
    c.setFont("Helvetica", 9)
    c.drawString(60, y-55, "This profile represents a high-risk entry point for corporate BEC (Business Email Compromise).")
    c.drawString(60, y-68, "Corporate recommendation: Enroll subject in Tier-1 Privacy Awareness workshops.")

    # Final Prevention Steps
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y-120, "3.0 ACTIONABLE REMEDIATION STRATEGY")
    steps = [
        "DECOY GEN: Create secondary alias profiles to confuse automated scrapers.",
        "NFC SHIELD: Deploy FootprintX hardware to prevent localized RFID cloning.",
        "SANITIZATION: Use EXIF-stripping tools before uploading to Instagram/Facebook.",
        "CREDENTIAL ROTATION: Reset passwords for all accounts sharing the current email prefix."
    ]
    y_step = y-145
    for step in steps:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(70, y_step, step.split(':')[0] + ":")
        c.setFont("Helvetica", 10)
        c.drawString(150, y_step, step.split(':')[1])
        y_step -= 20

    c.save()
    return filename