# =====================================================
# EduMentor AI – Streamlit App
# SDG 4: Quality Education
# =====================================================

import streamlit as st
import random

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="EduMentor AI",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Knowledge Base
# -----------------------------

learning_data = {
    "Python": {
        "Beginner": {
            "notes": "Python is a beginner-friendly programming language. "
                     "Focus on variables, data types, conditions, and loops.",
            "topics": ["Variables", "Data Types", "If-Else", "Loops"],
            "questions": [
                "What is a variable in Python?",
                "What is the difference between int and float?",
                "What is the use of a for loop?"
            ]
        },
        "Intermediate": {
            "notes": "Intermediate Python includes functions and data structures "
                     "for writing reusable code.",
            "topics": ["Functions", "Lists", "Tuples", "Dictionaries"],
            "questions": [
                "What is the difference between a list and a tuple?",
                "What is a dictionary?",
                "Why are functions important?"
            ]
        },
        "Advanced": {
            "notes": "Advanced Python covers OOP concepts and working with APIs.",
            "topics": ["OOP", "APIs", "File Handling", "Data Analysis"],
            "questions": [
                "What is Object-Oriented Programming?",
                "What is an API?",
                "What is inheritance?"
            ]
        }
    },

    "AI": {
        "Beginner": {
            "notes": "AI enables machines to mimic human intelligence.",
            "topics": ["What is AI", "Types of AI", "Applications of AI"],
            "questions": [
                "What is Artificial Intelligence?",
                "What are the types of AI?",
                "Name one application of AI."
            ]
        },
        "Intermediate": {
            "notes": "Machine Learning allows systems to learn from data.",
            "topics": ["Machine Learning", "Supervised Learning", "Unsupervised Learning"],
            "questions": [
                "What is Machine Learning?",
                "What is supervised learning?",
                "Difference between supervised and unsupervised learning?"
            ]
        },
        "Advanced": {
            "notes": "Advanced AI includes Deep Learning and NLP.",
            "topics": ["Deep Learning", "Neural Networks", "NLP"],
            "questions": [
                "What is Deep Learning?",
                "What is a neural network?",
                "What is Natural Language Processing?"
            ]
        }
    },

    "Math": {
        "Beginner": {
            "notes": "Basic math builds problem-solving foundations.",
            "topics": ["Algebra", "Linear Equations"],
            "questions": [
                "What is an algebraic expression?",
                "Solve: 2x + 3 = 7",
                "What is a variable?"
            ]
        },
        "Intermediate": {
            "notes": "Trigonometry studies relationships between angles and sides.",
            "topics": ["Trigonometry", "Geometry"],
            "questions": [
                "What is sine?",
                "State Pythagoras theorem.",
                "What is a right-angled triangle?"
            ]
        },
        "Advanced": {
            "notes": "Calculus deals with change and motion.",
            "topics": ["Limits", "Derivatives", "Integrals"],
            "questions": [
                "What is a derivative?",
                "What is an integral?",
                "Define limit."
            ]
        }
    }
}

# -----------------------------
# UI Layout
# -----------------------------

st.title("🎓 EduMentor AI")
st.subheader("Personalized Learning Assistant")
st.markdown("**Aligned with SDG 4 – Quality Education**")

st.divider()

subject = st.selectbox("📘 Select Subject", list(learning_data.keys()))
level = st.selectbox("🎯 Select Level", list(learning_data[subject].keys()))

if st.button("🚀 Start Learning"):
    st.subheader("📖 Learning Notes")
    st.write(learning_data[subject][level]["notes"])

    st.subheader("📌 Topics to Study")
    for topic in learning_data[subject][level]["topics"]:
        st.write("•", topic)

    st.subheader("📝 Practice Questions")
    questions = random.sample(
        learning_data[subject][level]["questions"], 2
    )
    for i, q in enumerate(questions, 1):
        st.write(f"{i}. {q}")

st.divider()
st.caption("© 2025 EduMentor AI | CSRBOX – IBM SkillsBuild Capstone Project")
