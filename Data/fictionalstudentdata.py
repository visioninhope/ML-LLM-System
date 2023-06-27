import pandas as pd
import numpy as np

# Setting a random seed for reproducibility
np.random.seed(0)

extracurricular_options = ['Chess Club', 'Soccer', 'Drama Club', 'Yearbook Committee', 'Robotics', 'Mathletes', 'Art Club', 'Basketball', 'Debate Team', 'Music Band', 'Science Club', 'Volunteer Club', 'Coding Club', 'Gardening Club', 'Language Club']

# Create a DataFrame with 400 students
data = {
    'Student ID': np.arange(1, 401),
    'Name': ['Student ' + str(i) for i in range(1, 401)],
    'Grade Level': np.random.choice([9, 10, 11, 12], 400),
    'Attendance': np.random.randint(70, 101, 400),
    'Academic Performance Math': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Grade Math': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Academic Performance English': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Grade English': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Academic Performance History': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Grade History': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Academic Performance Science': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Grade Science': np.random.choice(['A', 'B', 'C', 'D', 'F'], 400),
    'Extracurricular Activities': [np.random.choice(extracurricular_options, size=np.random.randint(1, 4)) for _ in range(400)],
    'Learning Preferences': np.random.choice(['Visual', 'Auditory', 'Kinesthetic'], 400),
    'Social and Emotional Well-being': np.random.randint(1, 11, 400),
    'Recommendations': ['To be generated' for _ in range(400)],
}

df = pd.DataFrame(data)
df.to_csv('student_data.csv', index=False)
