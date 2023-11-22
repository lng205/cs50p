from fpdf import FPDF, enums

name = input("Name: ")

class PDF(FPDF):
    def header(self):
        self.set_font("Times", "B", 40)
        self.cell(text=self.title, new_y="NEXT", center=True)

    def print_pic(self):
        self.add_page()
        self.image("shirtificate.png", enums.Align.C, 40, 180)
        self.set_font("Times", "B", 30)
        self.set_text_color(255,255,255)
        self.text(60, 100, f"{name} took CS50")

pdf = PDF()
pdf.set_title("CS50 Shirtificate")
pdf.print_pic()
pdf.output("shirtificate.pdf")
