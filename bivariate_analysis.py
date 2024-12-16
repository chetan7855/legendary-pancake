import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation(data):
    """Plots a heatmap of correlations for numerical columns."""
    # Select only numerical columns
    numerical_data = data.select_dtypes(include=['float64', 'int64'])
    
    # Compute correlation matrix
    corr_matrix = numerical_data.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
