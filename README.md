# Invoice-app
## Overview
The Invoice System is a Python application built using Tkinter and FPDF libraries. It provides a simple graphical user interface (GUI) to create invoices, display them, save the data, load existing data, and generate PDF invoices. The system allows users to enter customer details, product information, and automatically calculates the total amount.
<br>

## Features

1. Add customer and product details to create an invoice.
2. Display the invoice details in a text widget.
3. Calculate and display the total amount.
4. Generate a PDF version of the invoice.
5. Save the invoice data to a file.
6. Load invoice data from a file.
7. Clear all entries and reset the invoice.
<br>

## Requirements
```
Python 3.x
Tkinter library (comes pre-installed with Python)
FPDF library (install using pip install fpdf)
Installation
Make sure you have Python installed on your system. If not, download and install it from the official Python website.
Install the FPDF library using pip:
Copy code
pip install fpdf
Usage
Clone or download the repository containing the code.
Navigate to the directory where the code is located.
Run the invoice_system.py file:
Copy code
python invoice_system.py
The Invoice System window will appear.
Instructions
Adding Data to the Invoice
Enter the customer name in the "Customer Name" field.
Enter the product name in the "Product Name" field.
Enter the quantity of the product in the "Quantity" field.
Enter the price of the product in the "Price" field.
Click the "ADD" button to add the data to the invoice.
The invoice details will be displayed in the text widget, and the total amount will be updated.
Generating a PDF Invoice
After adding the required data, click the "Generate Pdf" button.
A dialog box will appear asking you to save the PDF file. Choose the desired location and filename, then click "Save".
A message box will confirm that the PDF invoice has been generated successfully.
Clearing Entries
To clear all entries and reset the invoice, click the "Clear" button.
Saving Invoice Data
Click the "Save" button to save the current invoice data to a file named invoice_data.txt.
Loading Invoice Data
Click the "Load" button to load invoice data from the invoice_data.txt file.
The loaded data will be displayed in the text widget, and the total amount will be updated.
Code Explanation
Main Components
GUI Elements: Labels, Entry fields, Text widget, and Buttons are used to create the interface.
Invoice List: The invoice details are stored in a list named self.invoice.
Total Amount: The total amount is calculated and displayed using self.total_amount and self.total_amount_label.
```

<br>

## Methods
```
__init__(self, root): Initializes the GUI components and sets up the layout.
add_data_invoice(self): Retrieves data from the entry fields, validates it, updates the invoice list, and refreshes the display.
update_invoice_text(self): Updates the text widget with the current invoice details.
update_total_amount(self): Updates the label displaying the total amount.
generate_pdf(self): Generates a PDF of the invoice and saves it to a user-specified location.
clear_entries(self): Clears all input fields, resets the invoice list and total amount.
save_data(self): Saves the current invoice data to a file.
load_data(self): Loads invoice data from a file and updates the display.
```
<br>

## Error Handling
The system checks for invalid input (e.g., non-numeric values for quantity and price) and shows appropriate error messages using messagebox.showerror.