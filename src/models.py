class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics or []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course(
        "Introduction to Python",
        "Learn the basics of Python programming.",
        "John Doe",
        "4 weeks",
        [
            "Variables and data types",
            "Control flow (if/else, loops)",
            "Functions and modules",
            "Lists, tuples, and dictionaries",
            "File I/O and error handling",
        ],
    ),
    Course(
        "Web Development with Flask",
        "Build web applications using Flask.",
        "Jane Smith",
        "6 weeks",
        [
            "Flask routing and views",
            "Jinja2 templates",
            "Handling forms and requests",
            "Working with databases",
            "Deploying a Flask app",
        ],
    ),
    Course(
        "Data Science Fundamentals",
        "An introduction to data science concepts and tools.",
        "Alice Johnson",
        "8 weeks",
        [
            "Data collection and cleaning",
            "Exploratory data analysis",
            "Data visualization",
            "Statistics fundamentals",
            "Introduction to machine learning",
        ],
    ),
    Course(
        "Introduction to Go",
        "Learn the basics of Go programming.",
        "Bob Williams",
        "5 weeks",
        [
            "Go syntax and types",
            "Structs and interfaces",
            "Goroutines and channels",
            "Error handling in Go",
            "Building and testing Go modules",
        ],
    ),
]