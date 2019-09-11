from fpdf import FPDF, HTMLMixin

title = '20000 Leagues Under the Seas'


class CustomPDF(FPDF, HTMLMixin):
    def header(self):
        # Set up a logo
        self.image('snakehead.png', 10, 8, 33)
        self.set_font('Rajdhani', '', 15)
        # Add an address
        self.cell(100)
        self.cell(0, 5, 'Mike Driscoll', ln=1)
        self.cell(100)
        self.cell(0, 5, '123 American Way', ln=1)
        self.cell(100)
        self.cell(0, 5, 'Any Town, USA', ln=1)
        # Line break
        self.ln(20)

    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Rajdhani', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Rajdhani', '', 12)
        # Output justified text
        if '.html' in name:
            self.write_html(txt)
        else:
            self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('Rajdhani', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)


def create_pdf(pdf_path):
    pdf = CustomPDF(format='A4')
    # Create the special value {nb}
    pdf.alias_nb_pages()
    # pdf.add_page()
    pdf.add_font('Rajdhani', '', 'Rajdhani-Regular.ttf', uni=True)
    pdf.add_font('Rajdhani', 'B', 'Rajdhani-Bold.ttf', uni=True)
    pdf.add_font('Rajdhani', 'I', 'Rajdhani-Light.ttf', uni=True)
    pdf.set_font('Rajdhani', '', 12)
    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    pdf.print_chapter(1, 'A RUNAWAY REEF', 'main.html')
    pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
    pdf.output(pdf_path)


if __name__ == '__main__':
    create_pdf('header_footer.pdf')
