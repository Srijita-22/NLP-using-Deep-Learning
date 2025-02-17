# Sample dataset
data = {
    'text': [
        "Government passes new tax reform",
        "Football team wins the championship",
        "Stock market hits an all-time high",
        "Elections coming up next month",
        "Tennis player wins grand slam",
        "Company reports huge quarterly profit"
    ],
    'category': ['Politics', 'Sports', 'Business', 'Politics', 'Sports', 'Business']
}

df = pd.DataFrame(data)

# Display dataset
print(df.head())
