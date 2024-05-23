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

+ Python 3.x
+ Tkinter library (comes pre-installed with Python)
+ FPDF library (install using pip install fpdf)
<br>

## Installation

1. Make sure you have Python installed on your system. If not, download and install it from the official Python website.
2. Install the FPDF library using pip:
```
pip install fpdf
```
<br>

## Usage
1. Clone or download the repository containing the code.
2. Navigate to the directory where the code is located.
3. Run the invoice_system.py file:
```
python invoice_system.py
```
4. The Invoice System window will appear.
<br>

## Instructions
### Adding Data to the Invoice
1. Enter the customer name in the "Customer Name" field.
2. Enter the product name in the "Product Name" field.
3. Enter the quantity of the product in the "Quantity" field.
4. Enter the price of the product in the "Price" field.
5. Click the "ADD" button to add the data to the invoice.
6. The invoice details will be displayed in the text widget, and the total amount will be updated.
<br>

## Generating a PDF Invoice
1. After adding the required data, click the "Generate Pdf" button.
2. A dialog box will appear asking you to save the PDF file. Choose the desired location and filename, then click "Save".
3. A message box will confirm that the PDF invoice has been generated successfully.
<br>

## Clearing Entries
1. To clear all entries and reset the invoice, click the "Clear" button.
<br>

## Saving Invoice Data
1. Click the "Save" button to save the current invoice data to a file named invoice_data.txt.
<br>

## Loading Invoice Data
1. Click the "Load" button to load invoice data from the invoice_data.txt file.
2. The loaded data will be displayed in the text widget, and the total amount will be updated.
<br>

## Code Explanation
### Main Components
+ GUI Elements: Labels, Entry fields, Text widget, and Buttons are used to create the interface.
+ Invoice List: The invoice details are stored in a list named self.invoice.
+ Total Amount: The total amount is calculated and displayed using self.total_amount and self.total_amount_label.
<br>

## Methods
+ __init__(self, root): Initializes the GUI components and sets up the layout.
+ add_data_invoice(self): Retrieves data from the entry fields, validates it, updates the invoice list, and refreshes the display.
+ update_invoice_text(self): Updates the text widget with the current invoice details.
+ update_total_amount(self): Updates the label displaying the total amount.
+ generate_pdf(self): Generates a PDF of the invoice and saves it to a user-specified location.
+ clear_entries(self): Clears all input fields, resets the invoice list and total amount.
+ save_data(self): Saves the current invoice data to a file.
+ load_data(self): Loads invoice data from a file and updates the display.
<br>

## Error Handling
+ The system checks for invalid input (e.g., non-numeric values for quantity and price) and shows appropriate error messages using messagebox.showerror.
<br>

# SCREENSHOTS
<img width ="500" height="500" alt="bill-app" src="https://github.com/sukhe3608/Invoice-app/blob/main/bill-app.png">
<img width ="500" height ="500" alt="pdf" src = " https://github.com/sukhe3608/Invoice-app/blob/main/billing-pdf.png">