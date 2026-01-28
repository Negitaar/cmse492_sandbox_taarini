import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Hours_Studied": [2, 4, 6, 8, 10],
    "Exam_Score": [65, 70, 78, 85, 92],
    "Sleep_Hours": [6, 7, 8, 7, 6]
}

df = pd.DataFrame(data)

# Compute summary statistics
mean_scores = df[["Hours_Studied", "Exam_Score", "Sleep_Hours"]].mean()
print("Mean values:")
print(mean_scores)

# Create a simple visualization
plt.plot(df["Hours_Studied"], df["Exam_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Exam Score vs Hours Studied")
plt.show()
