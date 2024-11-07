from flask import Flask, render_template, request

app = Flask(__name__)

# Full Stack Development quiz data
quiz_data = {
    "What does 'Full Stack Development' refer to?": {
        "options": ["Development of the front-end only", "Development of both the front-end and back-end", 
                    "Development of only databases", "Development of APIs"],
        "answer": "Development of both the front-end and back-end"
    },
    "Which of the following is a front-end JavaScript framework?": {
        "options": ["Express.js", "React", "Django", "Flask"],
        "answer": "React"
    },
    "What is the primary language used for back-end development in a typical full stack application?": {
        "options": ["JavaScript", "Python", "Ruby", "HTML"],
        "answer": "Python"
    },
    "Which database is commonly used in full-stack applications?": {
        "options": ["MongoDB", "MySQL", "PostgreSQL", "All of the above"],
        "answer": "All of the above"
    },
    "What is Node.js primarily used for in full stack development?": {
        "options": ["Front-end development", "Back-end development", 
                    "Database management", "API documentation"],
        "answer": "Back-end development"
    },
    "Which of the following is a popular CSS framework used in full stack applications?": {
        "options": ["React", "Flask", "Bootstrap", "Express.js"],
        "answer": "Bootstrap"
    },
    "What is the role of an API in a full stack application?": {
        "options": ["To manage the front-end UI", "To handle data transfer between the client and server", 
                    "To connect the database to the application", "To handle file uploads"],
        "answer": "To handle data transfer between the client and server"
    },
    "Which of the following is a common back-end web framework in Python for building full stack applications?": {
        "options": ["Flask", "React", "Angular", "Vue.js"],
        "answer": "Flask"
    },
    "Which version control system is widely used in full-stack development for code management?": {
        "options": ["Git", "SVN", "Mercurial", "CVS"],
        "answer": "Git"
    },
    "What is the purpose of a REST API in full stack applications?": {
        "options": ["To manage the client-side interface", "To allow communication between the front-end and back-end", 
                    "To store large amounts of data", "To create a database schema"],
        "answer": "To allow communication between the front-end and back-end"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        # Loop through each question in the quiz_data dictionary
        for question, data in quiz_data.items():
            user_answer = request.form.get(question)
            # Check if the answer is correct
            if user_answer and user_answer.strip() == data['answer']:
                score += 1
        return render_template('result.html', score=score, total=len(quiz_data))
    
    return render_template('quiz.html', questions=quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
