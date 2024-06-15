                                                         STEP MENTOR



 Brief about the Idea: The idea involves developing a system that helps the Students practice questions. It will generate clear problem statements using GenAI, suggest relevant formulas, and present solutions step-by-step in the given time frame; the prototype features GenAI API for question descriptions and chatbot and machine learning for formula suggestions. Opportunity : How different is it from any other existing ideas out there? The proposed model stands out with its comprehensive learning support, leveraging advanced technologies like Prompt Engineering and Machine learning. It offers a personalized learning experience akin to having a personal tutor. These features distinguish it from existing platforms, ensuring a unique and effective study tool for JEE students. The dataset used for practicing questions is imported from Youdata.ai (https://www.youdata.ai/datasets/662dddd37bb79dfcf0856b99)

 How will it be able to solve the problem? 

The app solves the problem of effective question practice for JEE students through several key mechanisms: Comprehensive Guidance: By providing step-by-step solutions, formula suggestions, and chatbot assistance, the app guides students through the question-solving process, ensuring they understand each step thoroughly. Free Accessibility: Offering free access to all users, the app removes cost barriers and ensures inclusivity, allowing students from diverse backgrounds to benefit from high-quality educational support. Empowerment through Practice: By facilitating regular practice and providing detailed explanations and assistance, the app empowers students to develop their problem-solving skills and deepen their understanding of physics concepts, ultimately improving their performance in the JEE exam.

 List of features offered by the solution : 

GenAI Question Description: Automatically generate clear and concise descriptions for questions using the Prompt Engineering and GenAI model. 

• Stepwise Solution Presentation: Divide solutions into step-by-step explanations, guiding students through each problem-solving stage. 

• Formula Suggestions: Analyze question contexts and suggest relevant formulas to users to aid problem-solving.

 • Chatbot Assistance: Integrate a chatbot assistant powered by GenAI to provide real-time support, explanations, and tips for solving questions. 

• Web Dashboard: Provide a user-friendly web-based dashboard for easy navigation, question selection, and access to features.

 • User Authentication: Implement secure user authentication to ensure privacy and access control.

 • Question Practice: Offer students a comprehensive database of questions from previous years of JEE to practice and improve their skills. 

• Personalized Learning: Adapt to each student's pace and needs, providing customized guidance and support throughout the learning process. 

• Feedback Mechanism: Incorporate a feedback mechanism for users to provide input, report issues, and suggest improvements. 

• Free Accessibility: Provide free access to all features, ensuring inclusivity and affordability for students from diverse backgrounds.

 Technology used :

 The "StepMentor" could utilize Google GenAI tools for machine learning, data processing and prompt engineering. Specifically: 



Streamlit is used to create an interactive web application.
YoudataAI (https://www.youdata.ai/datasets/662dddd37bb79dfcf0856b99) is used to import data(questions) for the application.
Pandas manages and processes the user data, such as saving which buttons were clicked or handling login information.
PIL and Fitz are used for processing images of questions that users upload, extracting the text or relevant information.
Pytesseract performs OCR on these images to convert the text into a format that can be processed and analyzed by your application.
Scikit-learn: Used for model development.
Google Generative AI is used to generate hints, explanations, or solutions for the questions users ask, providing a sophisticated, AI-driven tutoring experience.
io is used for handling file operations, such as reading and writing the CSV files that store user data and feedback.
