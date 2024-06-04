import os
import pandas as pd
import streamlit as st
from PIL import Image
import Tuning



def save_user_data(user_id, button):

    existing_data = pd.read_csv("credentials/userdevelopment.csv")


    old_data = pd.DataFrame(columns=["User_ID", "Button_Clicked"])

    new_data = pd.DataFrame({"User_ID": [user_id], "Button_Clicked": [button]})
    updated_data = pd.concat([old_data, new_data], ignore_index=True)
    updated_data.to_csv("userdevelopment.csv", index=False)


users = {"Saurab": "thisispass", "Shubham": "thisispass","Krishna": "thisispass"}


def login(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False


def loadingQuestions(path):
    with open(path, 'r') as file:
        questions = file.readlines()
    return questions


questions = loadingQuestions('resource/physics_questions.txt')
# gui
subject = st.sidebar.selectbox('Select:',('Dashboard', 'Ask Questions', 'Physics', 'Maths', 'Chemistry','Feedback'))


if subject == 'Dashboard':
    image = Image.open('resource/logo_images/step.png')
    st.image(image, width=100)
    st.title('Step Mentor')

    st.header('Welcome to **Step Mentor**, your AI tutor! Unlock your full potential with AI. ACE your JEE Preparation with confidence and ease!')
    st.subheader('Please Select a Subject to proceed further :eyes:')
    st.sidebar.header('Login to Your Account')
    # Input for username and password
    username = st.sidebar.text_input("Username", key="username_input")
    password = st.sidebar.text_input("Password", type="password",key="password_input")

    # Login button
    if st.sidebar.button("Login",key="login_button"):
        if login(username, password):
            st.session_state.username = username  # Store the username in session state
            st.header(f"Welcome {username}")
            st.success("Login Successful!🎉 You’re now in control! Choose your preferred subject")
        else:
            st.error("Invalid username or password")



if 'username' in st.session_state:
    user_id = st.session_state.username  # Retrieve the username from session state

    if subject == 'Ask Questions':
        st.title('Feel free to Ask Questions 🔎')
        asked_question = st.text_area('Please enter your Question')
        go_button = st.button("Go")
        if go_button:
            ans = Tuning.answer_asked_question(asked_question)
            st.write(ans)

        else:
           question_image= st.file_uploader("Please upload the Image of Question")
           image_search=st.button("Search")
           if image_search:
                ans=Tuning.image_asked_question(image_search)
                st.write(ans)


    if subject == 'Physics':
        t = st.time_input("Set an Timer for", value=None)
        st.write("Time is set for", t)







        question_index = st.selectbox("Select a question:", range(len(questions)))
        question = questions[question_index]

        st.header(f"Question {question_index + 1}")
        st.write(question)

        # Save the current question to the global variable
        current_question = question
        st.info("Your Proficiency level will be upadated based on how much helped you tooked in this question.")


        ProblemStatementButton=st.button("Explain")
        if ProblemStatementButton:
            explain = Tuning.explain_question(question)
            st.write(explain)
            save_user_data(user_id, "explain")
            st.success("Current Proficiency Level: Expert")





        HintButton = st.button("Hint")
        if HintButton:
            hint = Tuning.generate_hint(question)
            st.write(hint)
            save_user_data(user_id, "Hint")
            st.success("Current Proficiency Level: Learner")


        FormulaeButton = st.button("Formulae")
        if FormulaeButton:
            formulae = Tuning.get_formulae(question)
            st.write(formulae)
            save_user_data(user_id, "Formulae")
            st.error("Latest Proficiency Score: Intermediate")

        solutionButton = st.button("Solution")
        if solutionButton:
            ans = Tuning.get_solution(question)
            st.write(ans)
            save_user_data(user_id, "Show Solution")
            st.error("Final Proficiency Score: Begineer")

    if subject== 'Maths':
        st.subheader("Coming Soon!")

    if subject=='Chemistry':
        st.subheader("Coming Soon!")


    if subject=='Feedback':
        st.subheader("Your Valuable Feedback help us to Improve the quality of content")
        suggest=st.form("Enter your concent here")
                # This is writing directly to the main body. Since the form container is
        # defined above, this will appear below everything written in the form.
        problem = st.selectbox('Suggestion Regarding', ['Asking Questions','Login Issue','Practice Questions','Interface'])

        # These methods called on the form container, so they appear inside the form.
        submit = suggest.form_submit_button(f'Give feedback regarding: {problem}')
        sentence = suggest.text_input('Issue you are facing:')
        view_it = sentence.rstrip('.,!?') + f', {problem}!'
        if submit:
            suggest.subheader(view_it)
            file = open('feedback/feedback.txt', 'w')
            file.write(view_it)
            file.close()
            st.success("We appreciate your valuable Feedback! Thanks for Using Step Mentor")


        else:
            suggest.subheader('&nbsp;')



else:
    st.warning("Please log in to continue.")
