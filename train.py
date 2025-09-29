from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train(house_df, test_size=0.4):
    X = house_df[['Avg. Area Income', 'Avg. Area House Age',
                  'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
                  'Area Population']]
    y = house_df['Price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=101
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    return X_train, X_test, y_train, y_test, model

