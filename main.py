import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

data = pandas.read_csv('EAR_4MTH_SEX_OCU_CUR_NB_A.csv')
data = data[['ref_area','sex','classif1','classif2','time','obs_value']]
ddata = data.loc[data['ref_area'] != 'AUS']

data_classif1 = pandas.read_csv('classif1_en.csv', index_col = 'classif1')
data_classif1 = data_classif1.rename(columns={' classif1.label':'classif1_label'})
data_classif1 = data_classif1[['classif1_label']]

data = data.join(data_classif1, on = ['classif1'])
col = "classif1_label"
data = data[['obs_value','ref_area','sex','classif2','time','classif1_label','classif1']]
data[col] = data[col].str.split('.').str[1]
data = data[~data.isin([np.nan]).any(1)]



data_sex_ocu = data[(data.classif2 == 'CUR_TYPE_USD') & (data.time > 2010) & (data.time < 2014)]
sns.set()
sns.barplot(
    x="time",
    y="obs_value",
    hue="classif1_label",
    data=data_sex_ocu
);
# plt.legend(loc='upper left', bbox_to_anchor=(0, -0.05),
#            shadow=True, ncol=2,borderaxespad=0.)
plt.legend(loc='upper left', bbox_to_anchor=(0, -0.2),
           shadow=True, ncol=2,borderaxespad=0.)
plt.savefig('1.pdf')
''''
data_sex_ocu = first_data[(first_data.classif2 == 'CUR_TYPE_USD') & (first_data.time == 2019) & (first_data.sex == 'SEX_F')]
plt.figure(figsize=(10,6))
sns.set()
sns.barplot(
    x="time",
    y="obs_value",
    hue="classif1_label",
    data=data_sex_ocu,
);
plt.legend(loc='upper left', bbox_to_anchor=(0, -0.05),
           shadow=True, ncol=2,borderaxespad=0.)
# plt.legend(loc='upper left', bbox_to_anchor=(0, -0.2),
#            shadow=True, ncol=2,borderaxespad=0.)
plt.savefig('2.pdf')


data_sex_ocu = first_data[(first_data.classif2 == 'CUR_TYPE_USD') & (first_data.time == 2019) & (first_data.sex == 'SEX_F')]
sns.set()
sns.barplot(
    x="time",
    y="obs_value",
    hue="classif1_label",
    data=data_sex_ocu,
);
# plt.legend(loc='lower left', bbox_to_anchor=(0, -0.05),
#            shadow=True, ncol=2,borderaxespad=0.)
plt.legend(loc='upper left', bbox_to_anchor=(0, -0.2),
           shadow=True, ncol=2,borderaxespad=0.)
plt.savefig('3.pdf')

first_data = first_data[(first_data.classif2 == 'CUR_TYPE_USD')  & (first_data.ref_area == 'RUS') & (first_data.time > 2014)]
plt.figure(figsize=(10,6))
sns.set()
sns.relplot(
    x="time",
    y="obs_value",
    hue="classif1_label",
    data=first_data,
    kind='line',
    ci=None

);
plt.legend(loc='upper left', bbox_to_anchor=(0, -0.15),
           shadow=True, ncol=2,borderaxespad=0.)
plt.savefig('6.pdf')

first_data = first_data[(first_data.classif2 == 'CUR_TYPE_USD') & ((first_data.classif1 == 'OCU_ISCO08_1') | (first_data.classif1 == 'OCU_ISCO88_4')| (first_data.classif1 == 'OCU_ISCO88_1'))]
sns.set()
f = sns.relplot(
    x="time",
    y="obs_value",
    hue="classif1_label",
    data=first_data,
    kind = 'line',
    ci = None
);
f.fig.autofmt_xdate()
plt.savefig('5.pdf')

first_data = first_data[(first_data.classif2 == 'CUR_TYPE_USD') & ((first_data.classif1 == 'OCU_ISCO08_1') | (first_data.classif1 == 'OCU_ISCO88_4')| (first_data.classif1 == 'OCU_ISCO88_1'))]
sns.set()
f = sns.relplot(
    x="time",
    y="obs_value",
    hue="classif1_label",
    data=first_data,
    kind = 'line',
    ci = None
);
f.fig.autofmt_xdate()
plt.savefig('0.pdf')
'''''
