# **PDF Generator for Patient Form**  

This project is a desktop application developed in Python that allows users to fill out a patient form and generate a PDF file with the entered information. It uses libraries such as **tkinter** for the graphical interface and **reportlab** for PDF generation.  

## **Features**  
✅ User-friendly graphical interface for entering patient data.  

✅ Automatic generation of a PDF file with the form's content.  

✅ Ability to customize the name and location of the generated file.  

✅ Splash Screen displayed when launching the application.  

## **System Requirements**  
- **Python 3.8 or higher**.  
- **Required libraries**:  
  - **tkinter** (included by default in Python).  
  - **reportlab**.  

## **Installation**  
Clone this repository or download the project files.  

Ensure the necessary dependencies are installed by running:  

```bash
pip install reportlab
```  

Run the main file:  

```bash
python main.py
```  

## **Project Structure**  
The project is divided into several modules for easier maintenance:  

| File            | Description |
|----------------|------------|
| **main.py**       | Main file that launches the application and manages the overall workflow. |
| **gui.py**        | Defines the graphical interface using tkinter. |
| **pdf_generator.py** | Contains the logic for generating the PDF file with the entered data. |
| **utils.py**      | Helper functions, such as retrieving the current date. |

## **How to Use**  
1. Run the program with:  

   ```bash
   python main.py
   ```  
2. Fill out the form fields in the main window.  
3. Click the **"Create PDF"** button.  
4. Select a location to save the generated PDF file.  

## **Technical Notes**  

### **1. Graphical Interface (gui.py)**  
The GUI includes:  
- Input fields organized by categories (**personal data, contact information, medical history, etc.**).  
- A button to generate the PDF.  

### **2. PDF Generation (pdf_generator.py)**  
The module uses **reportlab** to create a PDF document with:  
- Formatted titles and subtitles.  
- Information organized into sections.  

### **3. Splash Screen (main.py)**  
When launched, the application displays a **Splash Screen** with a welcome message before opening the main window.  

## **Contributing**  
If you’d like to improve this project:  
1. Fork the repository.  
2. Create a new branch:  

   ```bash
   git checkout -b feature/new-feature
   ```  
3. Make your changes and submit a **pull request**.  

## **Author**  
This program was developed by **Edelan** as a solution for managing forms and generating reports in PDF format.  

Thank you for using this program! 😊  
