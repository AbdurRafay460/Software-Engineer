import tkinter as tk
from tkinter import messagebox  
import tkinter as tk
from PIL import ImageTk, Image
import time
# This define structure of our Gui  
class QuizApp:       
    def __init__(self , root):
         self.root = root
         self.root.title("Online Quiz System")
         self.root.configure(bg="#333333")

        # Variables
         self.logged_in = False
         self.student_name = ""
         self.roll_number = ""
         self.quiz_score = 0
         self.inter_marks = 0

        # Create login frame
         self.create_login_frame()
    def create_login_frame(self):
           
           login_frame = tk.Frame(self.root, padx=20, pady=20, borderwidth=2, relief=tk.GROOVE)
           login_frame.pack(padx=50, pady=50)

           label_heading = tk.Label(login_frame, text="Login to Quiz System", font=("Helvetica", 16))
           label_heading.grid(row=0, columnspan=2, pady=15,padx=15)
  
           label_username = tk.Label(login_frame, text="Username:",font=("Helvetica", 16))
           label_username.grid(row=1, column=0, pady=15,padx=15)
           entry_username = tk.Entry(login_frame)
           entry_username.grid(row=1, column=1, pady=15,padx=15)

           label_password = tk.Label(login_frame, text="Password:",font=("Helvetica", 16))
           label_password.grid(row=2, column=0, pady=15,padx=15)
           entry_password = tk.Entry(login_frame, show="*")
           entry_password.grid(row=2, column=1, pady=15,padx=15)

           button_login = tk.Button(login_frame, text="Login", command=lambda: self.authenticate(entry_username.get(), entry_password.get()),font=("Helvetica", 16))
           button_login.grid(row=3, columnspan=2, pady=15,padx=15)

    #Set font size of our login page
    def create_login_page(self):
        
        tk.Label(self.root, text="Welcome", font=("Helvetica", 20, "bold")).pack(pady=20)  # for design

        tk.Label(self.root, text="Username:", font=("Helvetica", 16)).pack(pady=8)
        tk.Entry(self.root, textvariable=self.username_var, font=("Helvetica", 16)).pack(pady=8)

        tk.Label(self.root, text="Password:", font=("Helvetica", 16)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.password_var, show="*", font=("Helvetica", 16)).pack(pady=12)

        tk.Button(self.root, text="Login", command=self.login, font=("Helvetica", 12, "bold"), width=24, bg="#4CAF50", fg="white").pack(pady=20)
    
    
    def authenticate(self,username,password):
           if username == "admin" and password == "123":
            self.logged_in = True
            self.create_student_info_frame()
           else:
            messagebox.showerror("Login Failed", "Invalid credentials. Try again.")
           

# Create our stud information page here
    def create_student_info_frame(self):
          self.clear_frame()
          student_frame = tk.Frame(self.root, padx=20, pady=20, borderwidth=2, relief=tk.GROOVE)
          student_frame.pack(padx=50, pady=50)

          label_heading = tk.Label(student_frame, text="Enter Student Information", font=("Helvetica", 16))
          label_heading.grid(row=0, columnspan=2, pady=20,padx=20)

          label_name = tk.Label(student_frame, text="Student Name:" ,font=("Helvetica", 16, "bold"))
          label_name.grid(row=1, column=0, pady=15,padx=15)
          entry_name = tk.Entry(student_frame)
          entry_name.grid(row=1, column=1, pady=15,padx=15)

          label_roll = tk.Label(student_frame, text="Roll Number:",font=("Helvetica", 16, "bold"))
          label_roll.grid(row=2, column=0, pady=25,padx=25)
          entry_roll = tk.Entry(student_frame)
          entry_roll.grid(row=2, column=1, pady=25,padx=25)

          button_continue = tk.Button(student_frame, text="Continue to Quiz",command=self.start_quiz)
          button_continue.grid(row=3, columnspan=2, pady=25,padx=25)
    def start_quiz(self):
        self.clear_frame()
        # self.background_image = Image.open("pict5.jpeg.jpg")  # Replace with your image file path
        # self.background_photo = ImageTk.PhotoImage(self.background_image.resize((1680, 1100)))
        # self.background_label = tk.Label(root, image=self.background_photo)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.quiz_frame = tk.Frame(self.root,padx=20,pady=20)
        self.quiz_frame.pack(padx=10,pady=10)
        self.start_time=0
        self.questions=[]
        tk.Label(self.quiz_frame,text="Quiz system",font=("Helvetica,14")).grid(row=0,columnspan=2,pady=10)
        self.questions= [{"question":"1. Oslo is the capital of?","options": ["A. Norway","B. France","C. Poland","D. iceland"], 
                          "correct_option":"A. Norway"},
                               {"question":"2. Eurpeon Union total number is?","options": ["A. 30","B. 31","C. 27","D. 28"],
                           "correct_option":"C. 27"},
                              {"question":"3. When british army take controlled in Subcontinent?","options": [" A. 1885 "," B. 1858 "," C. 1826 "," D. 1890 "],
                           "correct_option":"B. 1858"},
                              {"question":"4. Capital city of Germany is?","options": ["A. Berlin ",
                                                                                       "B. Paris  ",
                                                                                       "C. Dehli  ",
                                                                                       "D. Kyiv   "],
                           "correct_option:":"A. Berlin"},
                              {"question":"5. Total number of OIC is?","options": ["A. 60","B. 76","C. 48","D. 58"],
                            "correct_option":"D. 58"},
                            {"question":"6. Python was develop by?","options":["A.Imran khan",
                                                                               "B.Jonny LLb",
                                                                               "C.Chris mark",
                                                                               "D.Van Rossum"],
                             "correct_option":"D.Van Rossum"},
                            {"question":"7. What is the purpose of super()function in python?","options":["A. To call the parent classes",
                                                                                                          "B. To access super class attributes",
                                                                                                          "C. To create instance of classes",
                                                                                                          "D. Toinvoked a method from a derived"],
                              "correct_option":"A. To call the parent classes"},
                            {"question":"8. What symbol is mostly used in python programming?","options":["A. //"  ,
                                                                                                          "B. --"  ,
                                                                                                          "C./**/" ,
                                                                                                          "D.  # "] ,
                               "correct_option":"D. #"},
                            {"question":"9. What Data Type is used to store whole number in programming language?","options":["A.Float",
                                                                                                                              "B.String",
                                                                                                                              "C.Boolean",
                                                                                                                              "D.Integer"],
                            "Correct_option":"D.Integer"},
                            {"question":"10. What is a purpose of (Return) Statement in Python?","options":["A.To exist the Function",
                                                                                                            "B.To print a value",
                                                                                                            "C.To Declare a variable",
                                                                                                            "D.To cammand a code"],
                            "correct_option":"B.To print a value"},
                            {"question":"11. What is a result of (5+3)","options":["A. 10",
                                                                                   "B. 5",
                                                                                   "C. 3",
                                                                                   "D. 8"],
                            "correct_option":"D. 8"},
                            {"question":"12. If x=3 and y=7, what is the value of (x time/y)?","options":["A.10",
                                                                                                          "B.15",
                                                                                                          "C.30",
                                                                                                          "D.21"],
                            "correct_option":"D.21"},
                            {"question":"13. If a=6 and b=2, What is (a^2-b^2)?","options":["A. 28",
                                                                                            "B. 20",
                                                                                            "C. 16",
                                                                                            "D. 11"],
                            "correct_option":"A. 28"},
                            {"question":"14. What is a result of 18 divided by 3?","options":["A. 3",
                                                                                              "B. 6",
                                                                                              "C. 8",
                                                                                              "D. 9"],
                            "correct option":"B. 6"},
                            {"question":"15. What is a value of PI to two decimal places?","options":["A. 3.14",
                                                                                                      "B. 3.25",
                                                                                                      "C. 2.71",
                                                                                                      "D. 4.20"],
                            "correct_option":"A. 3.14" }
                            ]
        self.current_question_index=0
        self.score=0
        self.start_time = time.time()
        self.display_question()    #This line show our questions

                                 # Radiobutton , Next button , Previous button are set in this function
    
    def display_question(self):
        
        for widget in self.root.winfo_children():
                widget.destroy()
        self.question_frame=tk.Frame(self.root,padx=20,bd=2,relief=tk.GROOVE)
        self.question_frame.pack(padx=50)
        question_info = self.questions[self.current_question_index]

        tk.Label(self.root, text=question_info["question"], font=("Helavetica", 22)).pack(pady=22)
        option_var = tk.IntVar()
        for option in question_info["options"]:
            tk.Radiobutton(self.root, text=option, variable=option_var, value=option, font=("Helavetica", 20),width=12,
            command=lambda var=option_var, opt=option: self.check_answer(opt)).pack(pady=20)
        tk.Button(self.root, text="Next", command=self.next_question, font=("Helvetica", 16, "bold"), width=12,
              bg="#008CBA", fg="white").pack(pady=20)
        tk.Button(self.root, text="Previous", command=self.previous_question, font=("Helvetica", 16, "bold"), width=12,
                  bg="#008CBA", fg="white").pack(pady=20)
        # Add a timer label
        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"), fg="red", bg="#FFFFFF")
        self.timer_label.pack(pady=10)

        # Start the timer countdown
        self.update_timer()

    
    def check_answer(self,
                     selected_option):
           question_info= self.questions[self.current_question_index]
           correct_option = question_info["correct_option"]
           if selected_option == correct_option:
                                            self.score+=1
    
    
                            #After check 1 question move into next question
    
    def next_question(self):
         self.current_question_index+=1

         if self.current_question_index<len(self.questions):
              for widget in self.root.winfo_children():
                  widget.destroy()
              self.display_question()
         else:
           #display  quiz results
           for widget in self.root.winfo_children():
               widget.destroy()
           self.show_results()
    
                           # move our quiz into prevoius question    
    
    def previous_question(self):
        self.current_question_index -= 1

        if self.current_question_index >= 0:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.display_question()
        else:
        # You can choose to handle the case where there are no previous questions
        # For now, it resets to the first question
            self.current_question_index = 0
            for widget in self.root.winfo_children():
                widget.destroy()
            self.display_question()
    
    
                        # Display our result
    
    def add_student_info(self):
         self.student_name.set("taimour")

         self.roll_number.set("12")

         # Show result form here
    def show_results(self):
         result_text = f"Your Score: {self.score}/{len(self.questions)}"
         tk.Label(self.root, text=result_text, font=("Helvetica", 16, "bold"), fg="black", bg="#FFFFFF").place(relx=0.5, rely=0.4, anchor=tk.CENTER)

         feedback_text = ""
 
         if self.score == len(self.questions):
           feedback_text = "Congratulations! You got all the questions correct. You have passed!"
         elif self.score >= 7:
            feedback_text = "Good effort! You have passed. Keep it up!"
         else:
            feedback_text = "Try again. You didn't pass this time. Review the questions to improve."
  
         tk.Label(self.root, text=feedback_text, font=("Helvetica", 14), fg="black", bg="#FFFFFF").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

  

    
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, 600 - elapsed_time)  # 600 seconds = 10 minutes

        minutes = remaining_time // 60
        seconds = remaining_time % 60

        timer_text = f"Time Left: {minutes:02d}:{seconds:02d}"

        self.timer_label.config(text=timer_text)

#   Display result according to time using conditional statement
        if remaining_time > 0:
            # Update the timer every 1000 milliseconds (1 second)
            self.root.after(1000, self.update_timer)
        else:
            # Time's up! Handle it here (e.g., move to the next question or show results)
            messagebox.showinfo("Time's Up", "Sorry, your time is up!")
            for widget in self.root.winfo_children():
                widget.destroy()
                self.show_results()

                # Destory all Frame here
    def clear_frame(self):
        # Destroy all widgets in the current frame
        for widget in self.root.winfo_children():
            widget.destroy()
        
   
 # call all our module form here                   
if __name__=="__main__":
    root =tk.Tk()
    app= QuizApp(root)
    root.mainloop()

