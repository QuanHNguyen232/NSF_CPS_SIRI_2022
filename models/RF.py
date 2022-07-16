#%%
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import accuracy_score,confusion_matrix, classification_report, ConfusionMatrixDisplay

import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from MyDataLoader import daq_dataloader
MY_SEED = 0
#%% 
features = [
        'Label',
        'VDS_Brake_Pedal_Force0',
        'VDS_Veh_Speed0',
        'VDS_Steering_Wheel_Angle0',
        'VDS_Steering_Wheel_Angle_Rate0',
        'SCC_Lane_Deviation1'   # offset from center of lane
        ]
df = daq_dataloader(features)
y = df['Label']
le = LabelEncoder()
le.fit(y)
classes = le.classes_
y_enc=le.transform(y)
df['Label_enc'] = le.transform(y)

print('encoded classes', classes)
df

#%%

p=sns.heatmap(df.corr(), annot=False, vmin=-1, vmax=1,cmap ="coolwarm")

#%%
X = df.drop(['Label', 'Label_enc'], axis=1)
Y = df[['Label_enc']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, shuffle=True, random_state=MY_SEED)

print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

print(Y_train[:10]) # check if isShuffled
#%%

std_scale = StandardScaler()
X_train_std = std_scale.fit_transform(X_train)
X_test_std = std_scale.transform(X_test)

#%%
# CLASSIFIERS
def DTree_clf():
    DT_clf = DecisionTreeClassifier(max_depth=10, random_state=MY_SEED)
    DT_clf.fit(X_train_std, Y_train)
    y_pred = DT_clf.predict(X_test_std)
    acc = accuracy_score(Y_test, y_pred)
    cm = confusion_matrix(Y_test, y_pred)
    return DT_clf, acc, cm

def RF_clf():
    RF_clf = RandomForestClassifier(n_estimators=100,random_state=MY_SEED)
    RF_clf.fit(X_train_std, Y_train)
    y_pred = RF_clf.predict(X_test_std)
    acc = accuracy_score(Y_test, y_pred)
    cm = confusion_matrix(Y_test, y_pred)
    return RF_clf, acc, cm

# PLOT CONFUSION MATRIX
def plt_conf_matrix(acc, cm):
    fig, ax = plt.subplots(figsize=(5, 3),dpi= 100)
    ax =sns.heatmap(cm/np.sum(cm), annot=True, cmap = "inferno", xticklabels=classes, yticklabels=classes)
    plt.yticks(rotation=0) 
    plt.title('accuracy = %3.3f'%acc)
    ax.axis('equal')
    plt.xlabel('true label')
    plt.ylabel('predicted label')
    plt.show()

#%%
DT_clf, acc, cm = DTree_clf()
print(acc)

print(DT_clf.feature_importances_)
plt_conf_matrix(acc, cm)


RF_clf, acc, cm = RF_clf()
print(acc)
print(RF_clf.feature_importances_)
plt_conf_matrix(acc, cm)

#%%
# feature_importances = pd.DataFrame(
#     RF_clf.feature_importances_,
#     index =X_train.columns,
#     columns=['importance']).sort_values('importance', ascending=False)
# feature_importances.plot()

cols = ['_'.join(list(X_train.columns[i])) for i in range(len(X_train.columns))]
plt.bar(cols, RF_clf.feature_importances_, width = 0.4)
plt.xlabel("Features")
plt.ylabel("feature_importances_")
plt.show()

#%%
sns.countplot(y=cols)
plt.xticks(rotation=90)
