from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO

# Create a PDF writer object
output_pdf = PdfWriter()

# Define the content for the PDF summary
summary_content = """
JavaScript Basics Summary:

1. What is JavaScript?
JavaScript is a high-level, interpreted programming language used for web development.

2. Variables and Data Types:
JavaScript variables are used to store data. Common data types include numbers, strings, booleans, arrays, and objects.

3. Control Structures:
JavaScript supports control structures like if statements, loops (for, while), and switch-case for decision making and looping.

4. Functions:
Functions in JavaScript are reusable blocks of code that perform a specific task. They can be defined and called as needed.

5. DOM Manipulation:
The Document Object Model (DOM) allows JavaScript to interact with HTML elements, enabling dynamic content and interactivity.

6. Events and Event Handling:
JavaScript can handle user actions and events such as clicks, mouse movements, form submissions, etc., using event listeners.

7. Asynchronous Programming:
JavaScript supports asynchronous programming using promises, async/await, and callbacks for handling tasks that take time to complete.

8. ES6 Features:
ES6 (ECMAScript 2015) introduced new features like arrow functions, template literals, destructuring, classes, and modules.

This is a basic summary of JavaScript essentials.
"""

# Create a BytesIO object to store the PDF content temporarily
temp_pdf = BytesIO()

# Create a new PDF document
pdf_writer = PdfWriter()

# Create a new blank page and add the summary content
pdf_writer.add_blank_page(width=612, height=792)  # Letter size page (8.5 x 11 inches)
pdf_writer.add_page(PdfReader(BytesIO(summary_content.encode('utf-8'))).pages[0])

# Write the PDF content to the BytesIO object
pdf_writer.write(temp_pdf)

# Move to the beginning of the BytesIO stream
temp_pdf.seek(0)

# Add the PDF content from the BytesIO to the main PDF writer object
output_pdf.append_pages_from_stream(temp_pdf)

# Save the PDF file
with open("javascript_summary.pdf", "wb") as output_file:
    output_pdf.write(output_file)

print("PDF summary created successfully.")


