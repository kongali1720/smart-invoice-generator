from fpdf import FPDF
from PIL import Image
import datetime

class InvoicePDF(FPDF):
    def header(self):
        self.image("logo.png", 10, 8, 33)  # Ganti logo.png dengan logo kamu
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "INVOICE", ln=1, align="R")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Tanggal: {datetime.datetime.now().strftime('%Y-%m-%d')}", ln=1, align="R")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Terima kasih telah menggunakan layanan kami.", 0, 0, "C")

def generate_invoice(client, item, qty, price):
    total = int(qty) * float(price)
    pdf = InvoicePDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, f"Nama Klien: {client}", ln=1)
    pdf.cell(0, 10, f"Item: {item}", ln=1)
    pdf.cell(0, 10, f"Jumlah: {qty}", ln=1)
    pdf.cell(0, 10, f"Harga Satuan: ${price}", ln=1)
    pdf.cell(0, 10, f"Total: ${total:.2f}", ln=1)

    filename = f"Invoice_{client}_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
    pdf.output(filename)
    print(f"[+] Invoice berhasil dibuat: {filename}")

# Contoh penggunaan
generate_invoice("Jamal", "Jasa Desain Logo", 2, 25.00)
