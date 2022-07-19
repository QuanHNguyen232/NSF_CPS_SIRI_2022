#%%
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn')

#%%
# PLOT CONFUSION MATRIX
def plt_conf_matrix(acc, cm, classes, isRatio=False):
    fig, ax = plt.subplots(figsize=(5, 3),dpi= 100)

    if isRatio:
        ax =sns.heatmap(cm/np.sum(cm), annot=True, cmap = "inferno", xticklabels=classes, yticklabels=classes)    # return ratio
    else:
        ax =sns.heatmap(cm, annot=True, cmap = "inferno", xticklabels=classes, yticklabels=classes)
    plt.yticks(rotation=0) 
    plt.title('accuracy = %3.3f'%acc)
    ax.axis('equal')
    plt.xlabel('true label')
    plt.ylabel('predicted label')
    plt.show()

#%%
# PLOT FEAT_IMPORTANT
def plt_feat_important(cols_name, feature_importances, title):
    fig, ax = plt.subplots(figsize=(16, 9))
    tmp_df = pd.DataFrame({'colname':cols_name, 'important': list(feature_importances)})
    tmp_df.sort_values('important', ascending=True, inplace=True)
    ax.barh(tmp_df['colname'], tmp_df['important'])
    plt.show()

def plt_models_perform(model_name, acc, title):
    fig = plt.figure(figsize=(10, 7))
    plt.bar(model_name, acc, width=0.4)
    plt.ylabel('Accuracy')
    plt.xlabel('Models')
    plt.title(title)
    plt.show()