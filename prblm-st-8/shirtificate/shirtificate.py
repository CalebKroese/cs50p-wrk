# Must use "python3 Shirtificate.py" in terminal
from fpdf import FPDF

def main():
    name = input("Name: ").strip()
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add header text
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C", ln=True)

    # Add the shirt image (official CS50 version)
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # Overlay user's name on the shirt
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=105, y=150, txt=f"{name} took CS50")

    # Save output
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()