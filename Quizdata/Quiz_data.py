quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the Largest planet in solar system?",
        "choices": ["Mars", "Jupiter", "Saturn", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Au", "Ag", "Gd"],
        "answer": "Au"
    },
    {
        "question": "Which country is known as the 'Land of Rising sun'?",
        "choices": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    },
    {
        "question": "Which planet do we live on?",
        "choices": ["Earth", "Pluto", "Jupiter", "Saturn"],
        "answer" : "Earth"
    },
    {
        "question": "When was Nigeria formed?",
        "choices": ["October 1st 1960", "August 1st 1960", "October 21st 1960", "February 2nd 1979"],
        "answer": "October 1st 1960"
    },
    {
        "question": "When was Lagos created?",
        "choices": ["27 August 1978", "21 August 2012", "4th July 2017", "27 May 1967"],
        "answer": "27 May 1967"
    },
    {
        "question": "Who is the Governor oyo state?",
        "choices": ["Governor Dapo Abiodun", "Governor Adeleke Ademola", "Governor Oluseyi Abiodun Makinde", "Governor Babajide Sanwo-Olu"],
        "answer": "Governor Oluseyi Abiodun Makinde"
    },
    {
        "question": "Who is the President of Nigeria?",
        "choices": ["President Muhammadu Buhari", "President Olusegun Obasanjo", "President Bola Ahmed Tinubu", "President GoodLuck Jonathan"],
        "answer": "President Bola Ahmed Tinubu"
    },
    {
        "question": "Who is the first military president of Nigeria?",
        "choices": ["General Muritala Mohammed", "General Agoyi Irosi", "General Ibrahim Babagida", "General Yakubu Gowon"],
        "answer": "General Agoyi Irosi"
    },
    

]




import customtkinter
from tkinter import messagebox, ttk
from ttkbootstrap import Style

# from sqlink import database





                                    


root = customtkinter.CTk()
root.title("Quiz app")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

# phone.pack(pady=20)



style = Style(theme="flatly")

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))








def show_question():
    question = quiz_data[current_question]
    qs_label.configure(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].configure(text=choices[i], state="normal")

    feedback_label.configure(text="")
    next_btn.configure(state="disabled")    

def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:

        global score
        score += 1
        score_main.configure(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.configure(text="Correct", foreground="green")
    else:
        feedback_label.configure(text="Wrong", foreground="red")

    for button in choice_btns:
        button.configure(state="disabled")   
    next_btn.configure(state="normal")


def next_question():
    global current_question
    current_question += 1
    
    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz complete",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))  
        root.destroy()  


qs_label = ttk.Label(
    root,
    font=("Helvetica", 16),
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

choice_btns = []
for i in range (4):
    button = customtkinter.CTkButton(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)


feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)


score = 0
score_main = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_main.pack(pady=10)



next_btn = customtkinter.CTkButton(
    root,
    text="Next",
    command=next_question,
    state="disabled"

)
next_btn.pack(pady=5)




current_question = 0
show_question()
 





root.mainloop()