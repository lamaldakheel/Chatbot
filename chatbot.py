import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext


genai.configure(api_key="AIzaSyDWAI1CThavYPFIy0Shs5aMoCCIBnEj8qE")

def generate_recipe():
    ingredients = entry.get()
    
    if not ingredients.strip():
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "Please enter some ingredients!")
        return
    
    prompt = f"""
    Please create a recipe using the following ingredients: {ingredients}.
    - Include a creative name 
    - under the name include this 'here is your meal!' 
    - Include a short introduction about the recipe
    - List ingredients under 'Ingredients:' 
    - Provide cooking steps under 'Directions:' 
    - Mention approximate calories under 'Calories:' 
    - Highlight allergy warnings under 'Allergy Warnings:' 
    - Describe health benefits under 'Health Benefits:'
     Format the output as follows: "without stars"
    
    Ingredients:
    - Ingredient 1
    - Ingredient 2
    
    Cooking Steps:
    1. Step one
    2. Step two
    
    Calories:
    - Approximate calories per serving
    
    Allergy Warnings:
    - Relevant allergy information
    
    Health Benefits:
    - Benefit 1
    - Benefit 2
    """
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, response.text)

    except Exception as e:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, f"Error: {e}")

root = tk.Tk()
root.title("Create Your Meal with One Click!")
root.geometry("850x450")
root.configure(bg="#F8ECE9")

frame = tk.Frame(root, bg="#F8ECE9")
frame.pack(pady=20, padx=20)

left_frame = tk.Frame(frame, bg="#F8ECE9")
left_frame.pack(side=tk.LEFT, padx=10)

tk.Label(left_frame, text="Enter Ingredients:", font=("Times New Roman", 14, "bold"), bg="#F8ECE9", fg="#333333").pack(pady=5)
entry = tk.Entry(left_frame, width=40, bd=2, relief="solid", highlightbackground="#D8BFD8", font=("Times New Roman", 12))
entry.pack(pady=5)

tk.Button(left_frame, text="Surprise Me!", command=generate_recipe, font=("Times New Roman", 12), bg="#E6A4B4", fg="white").pack(pady=10)

right_frame = tk.Frame(frame, bg="#F8ECE9")
right_frame.pack(side=tk.RIGHT, padx=10)

tk.Label(right_frame, text="Taste the Magic!", font=("Times New Roman", 14, "bold"), bg="#F8ECE9", fg="#333333").pack(pady=5)
output_box = scrolledtext.ScrolledText(right_frame, width=50, height=15, wrap=tk.WORD, font=("Times New Roman", 12), bd=2, relief="solid", highlightbackground="#D8BFD8")
output_box.pack(pady=5)


root.mainloop()
