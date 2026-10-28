INTERVIEW_QUESTIONS = {
    "Python": [
        ("What is the difference between a list and a tuple?", "A list is mutable (can be changed); a tuple is immutable. Tuples are slightly faster and can be dictionary keys."),
        ("What is a dictionary?", "A collection of key-value pairs with fast lookup by key. Keys must be hashable (e.g. strings, numbers, tuples)."),
        ("What does the 'self' parameter mean?", "It refers to the current instance of the class and lets methods access that object's attributes."),
        ("What is a decorator?", "A function that wraps another function to add behaviour without changing its code, applied with the @name syntax."),
        ("Difference between '==' and 'is'?", "'==' compares values; 'is' checks whether two names refer to the exact same object in memory."),
    ],
    "SQL": [
        ("What is a primary key?", "A column (or set) that uniquely identifies each row and cannot be NULL."),
        ("Difference between INNER JOIN and LEFT JOIN?", "INNER JOIN returns only matching rows; LEFT JOIN returns all rows from the left table plus matches from the right (NULL where none)."),
        ("Difference between WHERE and HAVING?", "WHERE filters rows before grouping; HAVING filters groups after GROUP BY."),
        ("What is normalisation?", "Organising tables to reduce duplicate data and update problems, by splitting data into related tables."),
        ("What is an index?", "A data structure that speeds up lookups on a column, at the cost of extra storage and slower writes."),
    ],
    "HTML, CSS and JavaScript": [
        ("What is semantic HTML?", "Using tags that describe meaning (header, nav, main, article, footer) rather than just appearance. It helps accessibility and SEO."),
        ("Explain the CSS box model.", "Content, padding, border and margin make up every element's box."),
        ("Difference between 'let', 'const' and 'var'?", "let and const are block-scoped; const cannot be reassigned. var is function-scoped and older."),
        ("What is the DOM?", "The browser's tree representation of the page that JavaScript can read and modify."),
        ("What is a media query?", "A CSS rule that applies styles only under certain conditions, such as screen width, enabling responsive design."),
    ],
    "Java": [
        ("What are the four pillars of OOP?", "Encapsulation, inheritance, polymorphism and abstraction."),
        ("Difference between JDK, JRE and JVM?", "JVM runs bytecode; JRE = JVM + libraries to run programs; JDK = JRE + development tools like the compiler."),
        ("What is method overloading vs overriding?", "Overloading: same method name, different parameters in one class. Overriding: a subclass redefines a parent's method."),
        ("What is the difference between an interface and an abstract class?", "An interface defines a contract a class can implement (a class may implement many); an abstract class can hold shared state and partial implementation (single inheritance)."),
        ("What is garbage collection?", "Automatic memory management where the JVM frees objects that are no longer reachable."),
    ],
    "Cybersecurity": [
        ("What is the CIA triad?", "Confidentiality, Integrity and Availability - the three core goals of security."),
        ("What is phishing?", "A social-engineering attack using fake messages or sites to steal credentials or money."),
        ("Difference between encryption and hashing?", "Encryption is reversible with a key; hashing is one-way and used to verify data or store passwords (with salt)."),
        ("What is two-factor authentication?", "Requiring two different proofs of identity, such as a password plus a code from your phone."),
        ("What is SQL injection and how do you prevent it?", "Attackers insert SQL through input fields. Prevent it with parameterised queries and input validation."),
    ],
    "HR Interview": [
        ("Tell me about yourself.", "Give a short story: education, key skills/projects, and why this role. Keep it to about a minute and relevant."),
        ("What are your strengths and weaknesses?", "Pick real strengths with proof. For a weakness, name a genuine one and show how you are improving it."),
        ("Why should we hire you?", "Link your skills and projects to the job requirements and show eagerness to learn."),
        ("Where do you see yourself in five years?", "Show ambition to grow skills and responsibility within the field, without being unrealistic."),
        ("Describe a challenge you faced (use STAR).", "Situation, Task, Action, Result - pick a real example, focus on what YOU did and what you learned."),
    ],
}

PROJECT_IDEAS = [
    ("Personal Portfolio Website", "Beginner", "HTML, CSS", "Show your projects, skills and contact details on a responsive site."),
    ("To-Do List App", "Beginner", "Python or JavaScript", "Add, complete and delete tasks; store them in a file or database."),
    ("Quiz Game", "Beginner", "Python", "Ask questions from a list, keep score and show results."),
    ("Expense Tracker", "Intermediate", "Python, SQL, Flask", "Record spending, group by category and show monthly totals."),
    ("Student Attendance System", "Intermediate", "Flask, SQLite", "Mark and report attendance for classes with login for teachers."),
    ("Blog with Login", "Intermediate", "Flask, SQL", "Users register, write posts and comment. Practise authentication and security."),
    ("Spam Message Classifier", "Intermediate", "Python, scikit-learn", "Train a simple model on a public dataset and measure accuracy honestly."),
    ("Password Strength Checker", "Beginner", "Python, Security", "Score passwords by length and variety, and give advice (never store real passwords)."),
    ("Study Planner with Reminders", "Advanced", "Flask, JavaScript, SQL", "Plan weekly study sessions, track streaks and show charts."),
]
