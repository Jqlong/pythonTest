import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.feature_selection import mutual_info_classif
from sklearn.neighbors import KNeighborsClassifier


def relief_feature_selection(data, target_col, num_features=10, k_neighbors=5):
    # Separate the features and target column
    X = data.drop(columns=target_col)
    y = data[target_col]

    # Initialize Relief selector and fit to data
    relief_selector = SelectKBest(score_func=mutual_info_classif, k=num_features)
    relief_selector.fit(X, y)

    # Get feature scores and rank them in descending order
    feature_scores = pd.DataFrame({'Feature': X.columns, 'Score': relief_selector.scores_})
    feature_scores = feature_scores.sort_values(by=['Score'], ascending=False)

    # Fit KNN classifier to data and get feature importances using ReliefF
    knn_classifier = KNeighborsClassifier(n_neighbors=k_neighbors)
    knn_classifier.fit(X, y)
    relief_importances = knn_classifier.feature_importances_

    # Merge the two feature score dataframes and sort in descending order
    combined_scores = pd.merge(feature_scores, pd.DataFrame({'Feature': X.columns, 'Importance': relief_importances}),
                               on='Feature')
    combined_scores = combined_scores.sort_values(by=['Score', 'Importance'], ascending=False)

    # Print the sorted feature scores and return the feature importance dataframe
    print(combined_scores)
    return combined_scores[['Feature', 'Importance']]


data = pd.read_excel('../relief/all_lose.xls')
result = relief_feature_selection(data, 'ROTT_min_mean', num_features=10, k_neighbors=5)
print(result)
