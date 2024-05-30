import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from tkinter import filedialog
from datetime import datetime 

class InvoiceSystem:
    def __init__(self , root):
        self.root = root
        self.root.title("INVOICE SYSTEM")

        self.customer_name_label = tk.Label(root, text="Customer Name")
        self.customer_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.customer_name_entry = tk.Entry()
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.product_name_label = tk.Label(root, text="Product Name")
        self.product_name_label.grid(row=1, column=0, padx=10, pady=5)
        self.product_name_entry = tk.Entry()
        self.product_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.product_quantity_label = tk.Label(root, text="Quantity")
        self.product_quantity_label.grid(row=2, column=0, padx=10, pady=5)
        self.product_quantity_entry = tk.Entry()
        self.product_quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        self.product_price_label = tk.Label(root, text="Price")
        self.product_price_label.grid(row=3, column=0, padx=10, pady=5)
        self.product_price_entry = tk.Entry()
        self.product_price_entry.grid(row=3, column=1, padx=10, pady=5)

        self.invoice_text = tk.Text(root, height=10, width=50)
        self.invoice_text.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

        self.total_label = tk.Label(root, text="Total Amount:")
        self.total_label.grid(row=5, column=0, padx=10, pady=5)
        self.total_amount_label = tk.Label(root, text="")
        self.total_amount_label.grid(row=5, column=1, padx=10, pady=5)

        self.add_button = tk.Button(text="ADD", command=self.add_data_invoice)
        self.add_button.grid(row=7, column=0, padx=5, pady=5)

        self.generate_pdf_button = tk.Button(text="Generate Pdf", command=self.generate_pdf)
        self.generate_pdf_button.grid(row=8, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=8, column=1, padx=5, pady=5)

        self.save_button = tk.Button(text="Save", command=self.save_data)
        self.save_button.grid(row=9, column=0, padx=5, pady=5)

        self.load_button = tk.Button(text="Load", command=self.load_data)
        self.load_button.grid(row=9, column=1, padx=5, pady=5)

        self.invoice = []
        self.total_amount = 0

    def add_data_invoice(self):
        customer_name = self.customer_name_entry.get()
        product_name = self.product_name_entry.get()
        quantity = self.product_quantity_entry.get()
        price = self.product_price_entry.get()

        if customer_name and product_name and quantity and price:
            try:
                quantity = float(quantity)
                price = float(price)
                total_price = price * quantity
                self.invoice.append((customer_name, product_name, quantity, price, total_price))
                self.total_amount += total_price
                self.update_invoice_text()
                self.update_total_amount()
            except ValueError:
                messagebox.showerror("Error", "Invalid! Please enter valid quantity and price.")
        else:
            messagebox.showerror("Error", "Please enter valid data in all fields!")
        self.product_name_entry.delete(0,tk.END)
        self.product_quantity_entry.delete(0,tk.END)
        self.product_price_entry.delete(0,tk.END)

    def update_invoice_text(self):
        self.invoice_text.delete("1.0", tk.END)
        for item in self.invoice:
            self.invoice_text.insert(tk.END, f"{item[0]} - {item[1]} - Quantity: {item[2]}, Price: Rs.{item[3]}, Total: Rs.{item[4]:.2f}\n")

    def update_total_amount(self):
        self.total_amount_label.config(text=f"Total: Rs.{self.total_amount:.2f}")

    def generate_pdf(self):
    
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        current_date_time = datetime.now().strftime("%Y-%m-%d  %H : %M : %S")
        pdf.cell(200, 10, txt="INVOICE", ln=True, align='C')
        pdf.cell(200, 10, txt="GST IN. : *******************", ln=True)
        pdf.cell(200, 10, txt="Date : "+current_date_time, ln=True)
        pdf.cell(200, 10, txt="+---------------------------------------------------------------------------------------------------------------------------------+", ln=True)
        
        
        pdf.cell(200, 10, txt="From : XYZ..", ln=True,align='L')
        pdf.cell(200, 10, txt="To Customer: " + self.customer_name_entry.get(), ln=True)
        pdf.cell(200, 10, txt="+---------------------------------------------------------------------------------------------------------------------------------+", ln=True)
       

        pdf.cell(100, 10, txt="Product Name", border=1)
        pdf.cell(30, 10, txt="Quantity", border=1)
        pdf.cell(30, 10, txt="Price", border=1)
        pdf.cell(30, 10, txt="Total", border=1)
        pdf.ln()
        # Data
        for item in self.invoice:
            pdf.cell(100, 10, txt=item[1], border=1)
            pdf.cell(30, 10, txt=str(item[2]), border=1)
            pdf.cell(30, 10, txt="Rs. {:.2f}".format(item[3]), border=1)
            pdf.cell(30, 10, txt="Rs .{:.2f}".format(item[4]), border=1)
            pdf.ln()
        # Total amount
        pdf.cell(160, 10, txt="Total Amount:", border=1, align="R")
        pdf.cell(30, 10, txt="Rs. {:.2f}".format(self.total_amount), border=1)
        pdf.ln()
        pdf_output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if pdf_output_filename:
            pdf.output(pdf_output_filename)
            messagebox.showinfo("PDF Generated", "PDF invoice generated successfully.")

    def clear_entries(self):
        self.customer_name_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.product_quantity_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.invoice_text.delete("1.0", tk.END)
        self.total_amount = 0
        self.update_total_amount()
        self.invoice.clear()

    def save_data(self):
        with open("invoice_data.txt", "w") as f:
            for item in self.invoice:
                f.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]}\n")

    def load_data(self):
        try:
            with open("invoice_data.txt", "r") as f:
                data = f.readlines()
                for line in data:
                    parts = line.strip().split(',')
                    self.invoice.append((parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])))
                self.update_invoice_text()
                self.total_amount = sum(item[4] for item in self.invoice)
                self.update_total_amount()
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved data found!")

if __name__ == "__main__":
    root = tk.Tk()
    invoice_system = InvoiceSystem(root)
    root.mainloop()
