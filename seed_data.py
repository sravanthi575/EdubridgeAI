"""Original learning content for EduBridge AI.

Lesson bodies are trusted HTML written by the project team (admins can edit them
later). Question tuple: (text, A, B, C, D, correct_letter, explanation, difficulty)
"""
import html


def code(s):
    return "<pre><code>" + html.escape(s.strip("\n")) + "</code></pre>"


def p(s):
    return "<p>" + s + "</p>"


def ex(s):
    return '<div class="exercise"><strong>Try it:</strong> ' + s + "</div>"


COURSES = [
    # ------------------------------------------------------------------ PYTHON
    dict(slug="python", title="Python Programming", category="Programming", level="Beginner",
         description="Learn Python from zero: variables, decisions, loops, functions, data structures and object-oriented programming.",
         lessons=[
             ("Introduction to Python",
              p("Python is a beginner-friendly language used for web development, automation, data analysis and AI. You write instructions in a file ending in <code>.py</code> and run them with the Python interpreter.")
              + code('print("Hello, EduBridge!")  # this prints text\n# Lines starting with # are comments')
              + p("Save this as <code>hello.py</code> and run <code>py hello.py</code> (Windows) or <code>python3 hello.py</code> (macOS/Linux).")
              + ex("Print your name and your favourite subject on two lines."), 20),
             ("Variables and Data Types",
              p("A variable is a name that stores a value. Python figures out the type for you. Common types are <code>int</code> (whole numbers), <code>float</code> (decimals), <code>str</code> (text) and <code>bool</code> (True/False).")
              + code('name = "Asha"\nage = 19\nheight = 1.62\nis_student = True\nprint(type(age))      # <class \'int\'>\n\nmarks = int(input("Enter marks: "))  # input() always returns text')
              + ex("Ask for two numbers and print their sum."), 25),
             ("Conditional Statements",
              p("Programs make decisions with <code>if</code>, <code>elif</code> and <code>else</code>. Indentation (4 spaces) shows which lines belong to each branch.")
              + code('marks = 72\nif marks >= 90:\n    print("Grade A")\nelif marks >= 60:\n    print("Grade B")\nelse:\n    print("Keep practising")')
              + p("Comparison operators: <code>==  !=  &lt;  &gt;  &lt;=  &gt;=</code>. Combine conditions with <code>and</code>, <code>or</code>, <code>not</code>.")
              + ex("Write a program that says whether a number is even or odd (hint: <code>%</code>)."), 25),
             ("Loops",
              p("Loops repeat work. Use <code>for</code> when you know how many times, and <code>while</code> when you repeat until a condition changes.")
              + code('for i in range(1, 6):      # 1 to 5\n    print(i)\n\ncount = 3\nwhile count > 0:\n    print(count)\n    count -= 1\n\nfor n in range(10):\n    if n == 3:\n        continue        # skip 3\n    if n == 6:\n        break           # stop the loop')
              + ex("Print the multiplication table of 7."), 25),
             ("Functions",
              p("A function is a named, reusable block of code. It can take parameters and send back a result with <code>return</code>.")
              + code('def greet(name, greeting="Hello"):\n    return f"{greeting}, {name}!"\n\nprint(greet("Ravi"))\nprint(greet("Sita", "Namaste"))')
              + p("Good functions do one job and have a clear name.")
              + ex("Write <code>is_prime(n)</code> that returns True or False."), 30),
             ("Lists, Tuples, Sets and Dictionaries",
              p("These collections store many values. <strong>List</strong>: ordered and changeable. <strong>Tuple</strong>: ordered, fixed. <strong>Set</strong>: unique items. <strong>Dictionary</strong>: key-value pairs.")
              + code('fruits = ["apple", "banana"]\nfruits.append("mango")\n\npoint = (3, 4)                 # tuple\nunique = {1, 2, 2, 3}          # {1, 2, 3}\nstudent = {"name": "Asha", "marks": 88}\nprint(student["name"])\nfor key, value in student.items():\n    print(key, value)')
              + ex("Count how many times each word appears in a sentence using a dictionary."), 35),
             ("Object-Oriented Programming",
              p("A class is a blueprint; an object is something built from it. Objects bundle data (attributes) and behaviour (methods).")
              + code('class Student:\n    def __init__(self, name):\n        self.name = name\n        self.marks = []\n\n    def add_mark(self, mark):\n        self.marks.append(mark)\n\n    def average(self):\n        return sum(self.marks) / len(self.marks)\n\nclass Topper(Student):          # inheritance\n    def badge(self):\n        return f"{self.name} is a topper!"\n\ns = Student("Asha")\ns.add_mark(90); s.add_mark(80)\nprint(s.average())')
              + ex("Create a <code>BankAccount</code> class with deposit and withdraw methods."), 40),
         ],
         questions=[
             ("Which keyword is used to define a function in Python?", "function", "define", "def", "func", "C", "Functions are defined with the def keyword.", "easy"),
             ("What type is the value 3.14?", "int", "float", "str", "bool", "B", "Numbers with a decimal point are floats.", "easy"),
             ("What does len([1, 2, 3]) return?", "2", "3", "4", "Error", "B", "len() counts the items in the list.", "easy"),
             ("Which method adds an item to the end of a list?", "add()", "push()", "append()", "insert_end()", "C", "list.append(x) adds x at the end.", "easy"),
             ("Which of these is immutable (cannot be changed after creation)?", "list", "dictionary", "set", "tuple", "D", "Tuples cannot be modified once created.", "medium"),
             ("What is the value of 7 // 2 ?", "3.5", "3", "4", "2", "B", "// is floor division and drops the decimal part.", "medium"),
             ("How many items are in set([1, 1, 2, 2, 3]) ?", "5", "2", "3", "4", "C", "A set keeps only unique values: {1, 2, 3}.", "medium"),
             ("What is the purpose of __init__ in a class?", "Delete an object", "Initialise a new object", "Import a module", "End the program", "B", "__init__ runs when a new object is created and sets up its attributes.", "medium"),
             ("What does bool(\"\") return?", "True", "False", "None", "Error", "B", "Empty strings are 'falsy', so bool('') is False.", "hard"),
         ]),
    # -------------------------------------------------------------------- HTML
    dict(slug="html", title="HTML for Beginners", category="Web Development", level="Beginner",
         description="Build the structure of web pages: headings, text, links, images, lists, tables and forms.",
         lessons=[
             ("Structure of an HTML Page",
              p("HTML (HyperText Markup Language) describes the structure of a web page using <em>tags</em>. Every page has the same skeleton.")
              + code('<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <title>My First Page</title>\n</head>\n<body>\n  <h1>Hello, world!</h1>\n  <p>This is my first web page.</p>\n</body>\n</html>')
              + p("The <code>head</code> holds information about the page; the <code>body</code> holds what visitors see.")
              + ex("Save this as <code>index.html</code> and open it in your browser."), 20),
             ("Text, Links and Images",
              p("Headings go from <code>&lt;h1&gt;</code> (largest) to <code>&lt;h6&gt;</code>. Paragraphs use <code>&lt;p&gt;</code>. Links use <code>&lt;a&gt;</code> and images use <code>&lt;img&gt;</code>.")
              + code('<a href="https://example.com">Visit Example</a>\n<img src="photo.jpg" alt="A student reading a book">')
              + p("Always write meaningful <code>alt</code> text so screen-reader users understand your images.")
              + ex("Add a heading, a paragraph, a link and an image to your page."), 25),
             ("Lists, Tables and Forms",
              p("Use <code>&lt;ul&gt;</code> for bullet lists, <code>&lt;ol&gt;</code> for numbered lists, and <code>&lt;table&gt;</code> for tabular data. Forms collect input.")
              + code('<ul>\n  <li>HTML</li>\n  <li>CSS</li>\n</ul>\n\n<form action="/subscribe" method="post">\n  <label for="email">Email</label>\n  <input type="email" id="email" name="email" required>\n  <button type="submit">Join</button>\n</form>')
              + ex("Create a sign-up form with name, email and a submit button."), 30),
         ],
         questions=[
             ("Which tag creates the largest heading?", "<h6>", "<head>", "<h1>", "<title>", "C", "<h1> is the top-level (largest) heading.", "easy"),
             ("Which attribute holds the destination URL of a link?", "src", "href", "link", "url", "B", "<a href=\"...\"> sets where the link goes.", "easy"),
             ("Which tag defines an unordered (bullet) list?", "<ol>", "<li>", "<ul>", "<list>", "C", "<ul> is an unordered list; <ol> is ordered.", "easy"),
             ("Which attribute provides alternative text for an image?", "title", "alt", "caption", "name", "B", "alt text describes the image for screen readers and when images fail to load.", "medium"),
         ]),
    # --------------------------------------------------------------------- CSS
    dict(slug="css", title="CSS Styling", category="Web Development", level="Beginner",
         description="Make web pages beautiful: selectors, colours, the box model, Flexbox and responsive design.",
         lessons=[
             ("Selectors and Properties",
              p("CSS tells the browser how HTML should look. A rule has a <em>selector</em> and <em>declarations</em>.")
              + code('h1 {\n  color: #5145cd;\n  font-size: 2rem;\n}\n.note {           /* class selector */\n  background: #fff8e1;\n}\n#logo {           /* id selector */\n  font-weight: bold;\n}')
              + p("Add CSS with <code>&lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</code> in the head of your HTML.")
              + ex("Change the colour and font of every paragraph on your page."), 20),
             ("The Box Model",
              p("Every element is a box: <strong>content</strong>, surrounded by <strong>padding</strong>, then <strong>border</strong>, then <strong>margin</strong>.")
              + code('.card {\n  padding: 16px;\n  border: 1px solid #ccc;\n  margin: 20px auto;\n  box-sizing: border-box;  /* width includes padding and border */\n}')
              + ex("Build a card with padding, a border and rounded corners (<code>border-radius</code>)."), 25),
             ("Flexbox and Responsive Design",
              p("Flexbox arranges items in a row or column. Media queries change the style on small screens.")
              + code('.row {\n  display: flex;\n  gap: 16px;\n  flex-wrap: wrap;\n}\n@media (max-width: 600px) {\n  .row { flex-direction: column; }\n}')
              + ex("Make three cards sit side by side on desktop and stack on mobile."), 30),
         ],
         questions=[
             ("Which CSS property changes the text colour?", "font-color", "text-style", "color", "foreground", "C", "color sets the text colour.", "easy"),
             ("Which selector targets elements with class=\"note\"?", "#note", ".note", "note", "*note", "B", "A dot selects by class; # selects by id.", "easy"),
             ("From inside to outside, what is the order of the box model?", "content, padding, border, margin", "margin, border, padding, content", "content, border, padding, margin", "padding, content, margin, border", "A", "Content is surrounded by padding, then border, then margin.", "medium"),
             ("What does display: flex do?", "Hides the element", "Lays out children in a flexible row or column", "Makes text bold", "Adds a border", "B", "Flexbox is a layout system for arranging child items.", "medium"),
         ]),
    # --------------------------------------------------------------------- SQL
    dict(slug="sql", title="SQL and Databases", category="Database", level="Beginner",
         description="Store and query data with SQL. The skills apply to MySQL, PostgreSQL, SQLite and more.",
         lessons=[
             ("Databases and Tables",
              p("A database stores data in <strong>tables</strong> made of rows and columns. Each row is a record. SQL (Structured Query Language) lets you talk to the database. The examples use a table called <code>students</code>.")
              + code("CREATE TABLE students (\n  id INTEGER PRIMARY KEY,\n  name TEXT NOT NULL,\n  city TEXT,\n  marks INTEGER\n);")
              + p("The <strong>primary key</strong> uniquely identifies each row."), 20),
             ("SELECT and WHERE",
              p("<code>SELECT</code> reads data and <code>WHERE</code> filters rows.")
              + code("SELECT name, marks FROM students;\nSELECT * FROM students WHERE marks >= 60 AND city = 'Hyderabad';\nSELECT * FROM students ORDER BY marks DESC LIMIT 3;")
              + ex("Write a query that lists students whose name starts with 'A' (use <code>LIKE 'A%'</code>)."), 25),
             ("INSERT, UPDATE and DELETE",
              p("Change data with <code>INSERT</code>, <code>UPDATE</code> and <code>DELETE</code>. Always use <code>WHERE</code> with UPDATE and DELETE, or every row will change!")
              + code("INSERT INTO students (name, city, marks) VALUES ('Asha', 'Chennai', 88);\nUPDATE students SET marks = 92 WHERE name = 'Asha';\nDELETE FROM students WHERE id = 5;"), 25),
             ("Aggregates and Joins",
              p("Aggregate functions summarise data: <code>COUNT</code>, <code>SUM</code>, <code>AVG</code>, <code>MIN</code>, <code>MAX</code>. <code>GROUP BY</code> summarises per group. A <code>JOIN</code> combines rows from two tables.")
              + code("SELECT city, AVG(marks) FROM students GROUP BY city;\n\nSELECT s.name, c.title\nFROM students s\nINNER JOIN enrollments e ON e.student_id = s.id\nINNER JOIN courses c ON c.id = e.course_id;")
              + p("<strong>INNER JOIN</strong> keeps only matching rows; <strong>LEFT JOIN</strong> keeps all rows from the left table."), 35),
         ],
         questions=[
             ("Which SQL statement retrieves data from a table?", "GET", "SELECT", "FETCH", "OPEN", "B", "SELECT reads data.", "easy"),
             ("Which clause filters rows?", "WHERE", "ORDER BY", "GROUP", "LIMIT", "A", "WHERE keeps only rows that match a condition.", "easy"),
             ("Which function counts rows?", "SUM()", "COUNT()", "TOTAL()", "NUMBER()", "B", "COUNT() returns the number of rows.", "easy"),
             ("Which JOIN returns only rows that match in both tables?", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL JOIN", "C", "INNER JOIN keeps only matching rows.", "medium"),
             ("What happens with DELETE FROM students; (no WHERE)?", "Nothing", "Deletes one row", "Deletes all rows", "Deletes the table structure", "C", "Without WHERE, every row is deleted (the table itself remains).", "hard"),
         ]),
    # -------------------------------------------------------------- JAVASCRIPT
    dict(slug="javascript", title="JavaScript Basics", category="Web Development", level="Beginner",
         description="Add interactivity to web pages with JavaScript variables, functions and the DOM.",
         lessons=[
             ("Variables and Functions",
              p("Declare variables with <code>let</code> (can change) or <code>const</code> (cannot be reassigned). Functions group reusable code.")
              + code('const course = "JavaScript";\nlet score = 10;\nscore = score + 5;\n\nfunction add(a, b) {\n  return a + b;\n}\nconsole.log(add(2, 3)); // 5'), 25),
             ("The DOM and Events",
              p("The DOM is the browser's live model of your page. JavaScript can read and change it, and react to events like clicks.")
              + code('<button id="btn">Click me</button>\n<p id="msg"></p>\n<script>\n  document.getElementById("btn").addEventListener("click", () => {\n    document.getElementById("msg").textContent = "Hello!";\n  });\n</script>')
              + p("Prefer <code>textContent</code> over <code>innerHTML</code> when showing user-typed text; it avoids security problems."), 30),
         ],
         questions=[
             ("Which keyword declares a variable whose value can change (block-scoped)?", "let", "const", "static", "final", "A", "let declares a changeable block-scoped variable.", "easy"),
             ("What does document.getElementById('x') return?", "All elements", "The element with id 'x'", "A string", "The page title", "B", "It returns the single element whose id matches.", "easy"),
         ]),
    # -------------------------------------------------------------------- JAVA
    dict(slug="java", title="Java Fundamentals", category="Programming", level="Beginner",
         description="Start Java: syntax, types, classes and objects.",
         lessons=[
             ("Your First Java Program",
              p("Java is a strongly typed, object-oriented language used for Android apps, backend systems and more. Every program starts at the <code>main</code> method.")
              + code('public class Hello {\n    public static void main(String[] args) {\n        int year = 2026;\n        System.out.println("Hello from Java " + year);\n    }\n}')
              + p("Compile with <code>javac Hello.java</code>, run with <code>java Hello</code>."), 25),
             ("Classes and Objects",
              p("A class defines fields and methods. Use <code>new</code> to create an object.")
              + code('class Student {\n    String name;\n    Student(String name) { this.name = name; }\n    void hello() { System.out.println("Hi, " + name); }\n}\n// Student s = new Student("Asha"); s.hello();'), 30),
         ],
         questions=[
             ("Which method is the entry point of a Java program?", "start()", "main()", "run()", "init()", "B", "Execution begins at public static void main(String[] args).", "easy"),
             ("Which keyword creates a new object?", "make", "create", "new", "object", "C", "new allocates a new object.", "easy"),
         ]),
    # ---------------------------------------------------------------- SECURITY
    dict(slug="security-fundamentals", title="Security Fundamentals", category="Cybersecurity", level="Beginner",
         description="Understand core security ideas and build safe digital habits.",
         lessons=[
             ("The CIA Triad and Common Threats",
              p("Security protects three things: <strong>Confidentiality</strong> (only the right people see data), <strong>Integrity</strong> (data is not altered improperly) and <strong>Availability</strong> (systems work when needed).")
              + p("Common threats: phishing (fake messages that trick you), malware, weak passwords and unpatched software.")
              + ex("Think of one example for each part of the triad in a school or college system."), 25),
             ("Passwords, Phishing and Safe Habits",
              p("Use a <strong>unique</strong> password for every account, ideally from a password manager, and turn on two-factor authentication. Be careful with urgent messages asking for OTPs, passwords or payments. Check sender addresses and link destinations before clicking, and keep your devices updated.")
              + p("Only test security on systems you own or have written permission to test."), 25),
         ],
         questions=[
             ("What does the 'CIA' triad stand for in security?", "Control, Identity, Access", "Confidentiality, Integrity, Availability", "Cyber, Internet, Authentication", "Cryptography, Intrusion, Audit", "B", "CIA = Confidentiality, Integrity, Availability.", "easy"),
             ("What is the best defence against reused passwords being stolen?", "Use one strong password everywhere", "Use a unique password per account", "Write passwords in an email", "Change letters to numbers", "B", "Unique passwords stop one breach from exposing all accounts.", "medium"),
         ]),
    dict(slug="networking-basics", title="Networking Basics", category="Cybersecurity", level="Beginner",
         description="How devices find and talk to each other: IP, DNS, HTTP and ports.",
         lessons=[
             ("IP Addresses, DNS and HTTP",
              p("Every device on a network has an <strong>IP address</strong>. <strong>DNS</strong> translates names like example.com into IP addresses. <strong>HTTP/HTTPS</strong> is how browsers request web pages; HTTPS encrypts the traffic.")
              + ex("Run <code>ping example.com</code> and note the IP address it shows."), 25),
             ("Layers and Ports",
              p("Networks are explained in layers (the OSI model has 7; the practical TCP/IP model has 4). A <strong>port</strong> identifies a service on a device, for example 80 for HTTP and 443 for HTTPS. <strong>TCP</strong> is reliable and ordered; <strong>UDP</strong> is faster but does not guarantee delivery."), 25),
         ],
         questions=[
             ("What does DNS do?", "Encrypts web traffic", "Translates domain names to IP addresses", "Blocks viruses", "Stores web pages", "B", "DNS is the internet's phone book.", "easy"),
             ("Which port does HTTPS use by default?", "21", "25", "80", "443", "D", "HTTPS uses port 443 by default.", "medium"),
         ]),
    # --------------------------------------------------------------------- AI
    dict(slug="ai-fundamentals", title="AI Fundamentals", category="Artificial Intelligence", level="Beginner",
         description="What artificial intelligence is, where it is used, and how to use it responsibly.",
         lessons=[
             ("What is Artificial Intelligence?",
              p("AI is the field of building systems that perform tasks that normally need human intelligence, such as recognising images, understanding language or recommending videos. Most modern AI uses <strong>machine learning</strong>: instead of writing every rule by hand, we let a system learn patterns from data.")
              + ex("List three apps you use daily that probably use AI."), 20),
             ("Using AI Responsibly",
              p("AI can make mistakes and can sound confident while being wrong, so always check important facts. AI can also be <strong>biased</strong> if its training data is unfair or incomplete. Protect privacy: do not share passwords or private information with AI tools. Use AI to help you learn, not to skip learning."), 20),
         ],
         questions=[
             ("Which best describes machine learning?", "Programming every rule by hand", "Systems that learn patterns from data", "Storing data in tables", "Designing web pages", "B", "ML systems learn from examples rather than fixed rules.", "easy"),
             ("Why can AI systems show bias?", "Computers are emotional", "Training data can reflect unfair patterns", "Because they are slow", "Because of the screen size", "B", "Biased or incomplete data leads to biased results.", "medium"),
         ]),
    dict(slug="machine-learning-basics", title="Machine Learning Basics", category="Artificial Intelligence", level="Intermediate",
         description="Supervised and unsupervised learning, training and testing, and overfitting.",
         lessons=[
             ("Supervised and Unsupervised Learning",
              p("In <strong>supervised learning</strong> the data has labels (for example house size and price) and the model learns to predict the label. In <strong>unsupervised learning</strong> there are no labels and the model finds structure, such as groups of similar customers.")
              + p("Typical supervised tasks: <em>classification</em> (spam or not) and <em>regression</em> (predict a number)."), 25),
             ("Training, Testing and Overfitting",
              p("Split data into a <strong>training set</strong> (to learn) and a <strong>test set</strong> (to check on unseen data). A model that memorises the training data but performs badly on new data is <strong>overfitting</strong>.")
              + code("# scikit-learn sketch\nfrom sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)"), 30),
         ],
         questions=[
             ("Learning from labelled examples is called:", "Unsupervised learning", "Supervised learning", "Random learning", "Manual coding", "B", "Labels make it supervised learning.", "easy"),
             ("What is overfitting?", "Model too small", "Model memorises training data and fails on new data", "Model trains too fast", "Using too few features by choice", "B", "Overfit models do not generalise.", "medium"),
         ]),
    # ----------------------------------------------------------------- CAREER
    dict(slug="resume-writing", title="Resume Writing", category="Career Development", level="Beginner",
         description="Write a clear, honest one-page resume that gets noticed.",
         lessons=[
             ("Building a Strong Resume",
              p("A resume is a short summary of who you are and what you can do. Freshers usually aim for <strong>one page</strong>.")
              + "<ul><li><strong>Header:</strong> name, email, phone, LinkedIn/GitHub link.</li><li><strong>Summary:</strong> 2 lines about your goal and strengths.</li><li><strong>Skills:</strong> only skills you can talk about.</li><li><strong>Projects:</strong> what you built, tools used and the result.</li><li><strong>Education:</strong> degree, college, year, score.</li></ul>"
              + p("Be honest, use simple fonts, check spelling and start bullet points with action verbs (built, designed, analysed). Use the Resume Builder in the Career Hub to get started."), 20),
         ],
         questions=[
             ("How long should a fresher's resume usually be?", "One page", "Five pages", "Ten pages", "Half a line", "A", "A focused one-page resume is the common recommendation for freshers.", "easy"),
             ("Which is best to list under Skills?", "Anything you have heard of", "Skills you can discuss and demonstrate", "Only hobbies", "Skills of your friends", "B", "Interviewers may ask about anything on your resume.", "easy"),
         ]),
    dict(slug="interview-preparation", title="Interview Preparation", category="Career Development", level="Beginner",
         description="Prepare for technical and HR interviews with a simple, repeatable method.",
         lessons=[
             ("Preparing for Interviews",
              p("Research the company and role, revise your resume line by line, and practise out loud. For behavioural questions use the <strong>STAR</strong> method: <strong>S</strong>ituation, <strong>T</strong>ask, <strong>A</strong>ction, <strong>R</strong>esult.")
              + p("For technical questions, think aloud, ask clarifying questions, and say honestly when you do not know something, then explain how you would find out. Prepare 2 questions to ask the interviewer. Use the Interview Questions and Mock Interview pages in the Career Hub to practise."), 25),
         ],
         questions=[
             ("What does STAR stand for in interviews?", "Skill, Time, Action, Reply", "Situation, Task, Action, Result", "Start, Think, Answer, Review", "Story, Topic, Aim, Reason", "B", "STAR structures answers about past experiences.", "easy"),
             ("What should you do if you don't know a technical answer?", "Make something up", "Stay silent", "Say so honestly and explain how you would find out", "Leave the interview", "C", "Honesty and problem-solving are valued.", "medium"),
         ]),
]

SCHOLARSHIPS = [
    dict(title="National Scholarship Portal (NSP)", provider="Government of India", category="Government Scheme",
         eligibility="One portal for many central and state scholarship schemes. Eligibility, amounts and dates differ by scheme.",
         deadline="Varies by scheme - check the portal", link="https://scholarships.gov.in"),
    dict(title="AICTE Scholarship Schemes", provider="All India Council for Technical Education", category="Scholarship",
         eligibility="Schemes for eligible technical-education students. Read each scheme's criteria on the official site.",
         deadline="Varies - check the official site", link="https://www.aicte-india.org"),
    dict(title="SWAYAM Free Online Courses", provider="Ministry of Education, Government of India", category="Free Course",
         eligibility="Open to learners; courses are free to study. A paid proctored exam may be needed for a certificate.",
         deadline="Course-wise - see course pages", link="https://swayam.gov.in"),
    dict(title="NPTEL Courses", provider="IITs and IISc", category="Free Course",
         eligibility="Free video lectures and course material in engineering, science and humanities. Certification exams may have a fee.",
         deadline="Exam registration dates are published on the site", link="https://nptel.ac.in"),
    dict(title="freeCodeCamp", provider="freeCodeCamp (non-profit)", category="Certification",
         eligibility="Free coding curriculum with free certifications. No eligibility criteria.",
         deadline="None - learn any time", link="https://www.freecodecamp.org"),
    dict(title="CS50 (Introduction to Computer Science)", provider="Harvard University / edX", category="Free Course",
         eligibility="Free to take online. A verified certificate may be paid.",
         deadline="Self-paced", link="https://cs50.harvard.edu/x"),
    dict(title="Kaggle Learn", provider="Kaggle", category="Free Course",
         eligibility="Short free micro-courses on Python, SQL, machine learning and data analysis.",
         deadline="Self-paced", link="https://www.kaggle.com/learn"),
    dict(title="Coursera Financial Aid", provider="Coursera", category="Scholarship",
         eligibility="Learners who cannot afford fees can apply per course. Approval is decided by Coursera.",
         deadline="Per course - apply from the course page", link="https://www.coursera.org/financial-aid"),
]
