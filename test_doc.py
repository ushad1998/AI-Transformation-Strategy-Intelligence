from tools import create_word_document

plan = [
    "Understand request",
    "Create outline",
    "Write proposal",
    "Review proposal"
]

content = """
This is a sample AI generated proposal

This AI Recruitment System automates resume screening, candidate ranking and interview scheduling.
"""

file = create_word_document(
    "Create AI Recruitment Proposal",
    plan,
    content
)

print(file)