import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import RocCurveDisplay

def split_test(df):
    X = df.drop(['target'], axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def fit_score(X_train, X_test, y_train, y_test):
    models = {"KNN": KNeighborsClassifier(),
          "Logistic Regression": LogisticRegression(max_iter=100),
          "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)}
    
    model_scores = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        model_scores[name] = model.score(X_test, y_test)
    return model_scores

def KNN(X_train, X_test, y_train, y_test):
    model = KNeighborsClassifier()
    train_scores = []
    test_scores = []
    dif_scores = []
    neighbors = range(1, 21)

    for i in neighbors:
        model.set_params(n_neighbors = i)
        model.fit(X_train, y_train)
        train_scores.append(model.score(X_train, y_train))
        test_scores.append(model.score(X_test, y_test))
        dif_scores.append(test_scores[-1] - train_scores[-1])

    df_train = pd.DataFrame(train_scores, columns=['train_scores'])
    df_test = pd.DataFrame(test_scores, columns=['test_scores'])

    result = pd.concat([df_train, df_test], axis=1)

    return result

def rs_cv(model, params, X_train, X_test, y_train, y_test):
    rs = RandomizedSearchCV(model, param_distributions=params, cv=5, n_iter=20, verbose=True)
    rs.fit(X_train, y_train)

    return rs

def grid_search(model, params, X_train, X_test, y_train, y_test):
    gs = GridSearchCV(model, param_grid=params, cv=5, verbose=True)
    gs.fit(X_train, y_train)

    return gs

def roc_curve(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    RocCurveDisplay.from_estimator(estimator=model, 
                               X=X_test, 
                               y=y_test)
    
def predict(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def c_matrix(y_test, y_preds):
    fig, ax = plt.subplots(figsize=(3, 3))
    ax = sns.heatmap(confusion_matrix(y_test, y_preds),
                     annot=True,
                     cbar=False)
    plt.xlabel("true label")
    plt.ylabel("predicted label")

def class_report(y_test, y_preds):
    print(classification_report(y_test, y_preds))

def cvscore(model, df):
    X = df.drop(['target'], axis=1)
    y = df['target']
    cv_acc = (cross_val_score(model, X, y, cv=5, scoring="accuracy"))
    cv_precision = (cross_val_score(model, X, y, cv=5, scoring="precision"))
    cv_recall = (cross_val_score(model, X, y, cv=5, scoring="recall"))
    cv_f1 = (cross_val_score(model, X, y, cv=5, scoring="f1"))
    return cv_acc.mean(), cv_precision.mean(), cv_recall.mean(), cv_f1.mean()