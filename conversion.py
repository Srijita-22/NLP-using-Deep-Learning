from sklearn.preprocessing import LabelEncoder

# Encode labels (Politics = 0, Sports = 1, Business = 2)
label_encoder = LabelEncoder()
df['category_encoded'] = label_encoder.fit_transform(df['category'])

print(df[['category', 'category_encoded']])
