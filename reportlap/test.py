from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    # Create a canvas (PDF) object
    c = canvas.Canvas(filename, pagesize=letter)

    # Define the content for flashcards and exercises
    flashcards = [
        {'question': 'What is JavaScript?', 'answer': 'JavaScript is a scripting language for web development.'},
        {'question': 'What is a variable?', 'answer': 'A variable is a container for storing data.'},
        # Add more flashcards as needed
    ]

    exercises = [
        {'question': 'Write a function to add two numbers.', 'answer': 'function addNumbers(a, b) { return a + b; }'},
        {'question': 'What is the output of 2 + 3 * 4?', 'answer': 'The output is 14.'},
        # Add more exercises as needed
    ]

    # Set font and font size
    c.setFont("Helvetica", 12)

    # Add flashcards to the PDF
    c.drawString(50, 750, 'JavaScript Basics - Flashcards:')
    y_pos = 720
    for card in flashcards:
        y_pos -= 20
        c.drawString(50, y_pos, f'Q: {card["question"]}')
        y_pos -= 15
        c.drawString(50, y_pos, f'A: {card["answer"]}')

    # Add exercises to the PDF
    y_pos -= 50
    c.drawString(50, y_pos, 'JavaScript Basics - Exercises:')
    y_pos -= 20
    for ex in exercises:
        y_pos -= 20
        c.drawString(50, y_pos, f'Q: {ex["question"]}')
        y_pos -= 15
        c.drawString(50, y_pos, f'A: {ex["answer"]}')

    # Save the PDF file
    c.save()
    print(f'PDF file "{filename}" created successfully.')

# Call the function to create the PDF file
create_pdf('javascript_basics.pdf')
