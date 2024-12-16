import matplotlib.pyplot as plt
import seaborn as sns

def plot_categorical(data, column):
    """Plots a bar chart for a categorical column."""
    plt.figure(figsize=(10, 6))
    sns.countplot(data[column])
    plt.title(f"Distribution of {column}")
    plt.show()

def plot_numerical(data, column):
    """Plots a histogram for a numerical column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()
