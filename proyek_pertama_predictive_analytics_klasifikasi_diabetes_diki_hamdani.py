# -*- coding: utf-8 -*-
"""Proyek_Pertama_Predictive_Analytics_Klasifikasi_Diabetes_Diki Hamdani.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1209lMJBt0P7Z2-sKDei_maYG2E7zv0zT

# 1. Domain Proyek
Dilansir dari [Halodoc](https://www.halodoc.com/kesehatan/diabetes), diabetes adalah penyakit kronis atau yang berlangsung jangka panjang. Penyakit ini ditandai dengan meningkatnya kadar gula darah (glukosa) hingga di atas nilai normal. Diabetes terjadi ketika tubuh pengidapnya tidak lagi mampu mengambil gula (glukosa) ke dalam sel dan menggunakannya sebagai energi. Kondisi ini pada akhirnya menghasilkan penumpukan gula ekstra dalam aliran darah tubuh.

Salah satu faktor penyebab diabetes adalah karena adanya gangguan dalam tubuh, sehingga tubuh tidak mampu menggunakan glukosa dara ke dalam hati. Sehingga, glukosa menumpuk dalam darah. Oleh karena itu, salah satu cara yang dapat dilakukan untuk mencegah diabetes dengan mengembangkan model machine learning yang dapat memprediksi apakah seseorang terindikasi diabetes atau tidak berdsarkan parameter-paremeter tertentu [[1]](https://www.halodoc.com/kesehatan/diabetes).

# 2. Business Understanding
## 2.1 Problem statements
- Bagaimana membuat model yang memungkinkan untuk melakukan prediksi diabetes pada seseorang?
- Model machine learning manakah yang dapat menyelasikan permasalahan dengan baik?

## 2.2 Goals
- Mengetahui karakteristik yang berpengaruh terhadap diabetes.
- Mengetahui model yang terbaik untuk memprediksi diabetes pada seseorang.

## 2.3 Solution statements
Untuk mencapai tujuan, masalah ini dapat menggunakan perbangingan dari beberapa model, diantaranya adalah sebagai berikut.
- K-Nearest Neighbor
K-Nearest Neighbor (KNN) adalah algoritma yang digunakan untuk melakukan klasifikasi terhadap suatu objek, berdasarkan *k* buah data latih yang jaraknya saling berdekatan dengan objek tersebut. Syarat nilai *k* dan lebih dari satu. Dekat atau jauhnya jarak data latih yang paling dekat denan objek yang akan diklasifikasi dapat dihitung dengan metode cosine[[2]](https://jsi.cs.ui.ac.id/index.php/jsi/article/view/500).

- Random Forest
Algoritma Random forest merupakan salah satu metode yang digunakan untuk klasifikasi dan regresi. Metode ini merupakan sebuah ensemble (kumpulan) metode pembelajaran menggunakan pohon keputusan sebagai *base classifier* yang dibangun dan dikombinaskan. Ada tiga aspek penting dalam metode random forest, yaitu: melakukan bootstrap sampling untuk membangun pohon prediksi, masing-masing pohon keputusan memprediksi dengan prediktor acak, lalu random forest melakukan prediksi dengan mengombinasikan hasil dari setiap pohon keputusan dengan cara majority vote untuk klasifikasi atau rata-rata untuk regresi [[3]](hhttp://ejournal.uin-suska.ac.id/index.php/IJAIDM/article/view/4903/3023). 

- Boosting
Sama halnya seperti algoritma random forest, algortima Boosting juga merupakan salah satu algoritma machine learning yang termasuk ke dalam kategori ensembel. Algoritma yang menggunakan teknik boosting bekerja dengan membangun model dari data latih. Kemudian ia membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan [[4]](https://www.dicoding.com/academies/319/tutorials/18590?from=18585).

    Algoritma boosting bertujuan untuk meningkatkan performa akurasi prediksi dengan menggabungkan beberapa model sederhana dan dianggap lemah (weak learners) sehingga membentuk suatu model yang kuat (strong ensemble learner). Algoritma boosting muncul dari gagasan mengenai apakah algoritma yang sederhana seperti linear regression dan decision tree dapat dimodifikasi untuk dapat meningkatkan performa.

# 3. Data Understanding
Dataset yang digunakan adalah data [diabetes](https://www.kaggle.com/code/swetarajsinha/prediction-diabetes-logistic-regression/data) yang memiliki 2000 baris dan 9 kolom. Berikut adalah 9 kolom yang akan digunakan.

- **Pregnancies**: Kategori kehamilan
- **Glucose**: Kadar gula pada tubuh
- **BloodPressure**: Tekanan darah
- **SkinThickness**: Tingkat ketebalan kulit
- **Insulin**: Insulin
- **BMI**: Berat badan
- **DiabetesPedigreeFunction**: Fungsi silsilah diabetes
- **Age**: Usia
- **Outcome**: Indikasi apakah pasien terindikasi diabetes (1) atau tidak (0).

# 4. Data Loading
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = 'https://raw.githubusercontent.com/Dikihmd01/Applied-ML/main/dataset/diabetes2.csv'

# Melihat data training
diabetes = pd.read_csv(dataset)
diabetes

diabetes.shape

"""Pada hasil di atas, dapat kita ketahui bahwa pada data training terdapat 2000 baris data dan 9 kolom.

# 5. Explaratory Data Analysis

## 5.1 Deskripsi Variabel
"""

cols = diabetes.columns
print('\n'.join(diabetes))

diabetes.info()

"""### Mengecek deskripsi statistik data."""

diabetes.describe()

"""Berdaarkan hasil di atas, insight yang diperoleh adalah sebagai berikut.
- Count  adalah jumlah sampel pada data.
- Mean adalah nilai rata-rata.
- Std adalah standar deviasi.
- Min yaitu nilai minimum setiap kolom. 
- 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama. 
- 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- 75% adalah kuartil ketiga.
- Max adalah nilai maksimum.
- Beberapa atribut pada data terdapat nilai 0
- Atribut Pregnancies, SkinThickness, dan Insulin memiliki
- Tidak terdapat atribut yang berisi NAN/Nilai null
- Tidak terdapat atribut dengan tipe object.

## 5.2 Menangani missing value
Dari hasil pengecekan deskripsi variabel, nilai minimum pada semua kolom adalah 0 kecuali kolom **DiabetesPedigreeFunction** dan **Age**. Selanjutnya adalah mengecek jumlah missing value. Pregnancies dan Outcome merupakan kolom numerik, sehingga tidak perlu dicek.
"""

# pregnancies = (diabetes.Pregnancies == 0).sum()
glucose = (diabetes.Glucose == 0).sum()
blood_pressure = (diabetes.BloodPressure == 0).sum()
skin_thickness = (diabetes.SkinThickness == 0).sum()
insulin = (diabetes.Insulin == 0).sum()
bmi = (diabetes.BMI == 0).sum()

# print(f'nilai 0 pada kolom Pregnanicies: {pregnancies}')
print(f'nilai 0 pada kolom Glucose: {glucose}')
print(f'nilai 0 pada kolom BloodPressure: {blood_pressure}')
print(f'nilai 0 pada kolom SkinThickness: {skin_thickness}')
print(f'nilai 0 pada kolom Insulin: {insulin}')
print(f'nilai 0 pada kolom BMI: {bmi}')

"""Selanjutnya cek apakah data bernilai 0 pada salah satu dimensi juga terdapat pada dimensi yang lain? Cek pada kolom dengan jumlah missing value terbanyak"""

# diabetes.loc[(diabetes['Insulin'] == 0)]

"""Bedasarkan hasil pengecekan di atas, seluruh data yang bernilai 0 pada dimensi lainnya juga memiliki nilai 0 pada dimensi Insulin"""

glucose_col = diabetes['Glucose']
blood_pressure_col = diabetes['BloodPressure']
skin_thickness_col = diabetes['SkinThickness']
insulin_col = diabetes['Insulin']
bmi_col = diabetes['BMI']

glucose_col.replace(to_replace=0, value=glucose_col.mean(), inplace=True)
blood_pressure_col.replace(to_replace=0, value=blood_pressure_col.mean(), inplace=True)
skin_thickness_col.replace(to_replace=0, value=skin_thickness_col.mean(), inplace=True)
insulin_col.replace(to_replace=0, value=insulin_col.mean(), inplace=True)
bmi_col.replace(to_replace=0, value=bmi_col.mean(), inplace=True)

# pregnancies = (diabetes.Pregnancies == 0).sum()
glucose = (diabetes.Glucose == 0).sum()
blood_pressure = (diabetes.BloodPressure == 0).sum()
skin_thickness = (diabetes.SkinThickness == 0).sum()
insulin = (diabetes.Insulin == 0).sum()
bmi = (diabetes.BMI == 0).sum()

# print(f'nilai 0 pada kolom Pregnanicies: {pregnancies}')
print(f'nilai 0 pada kolom Glucose: {glucose}')
print(f'nilai 0 pada kolom BloodPressure: {blood_pressure}')
print(f'nilai 0 pada kolom SkinThickness: {skin_thickness}')
print(f'nilai 0 pada kolom Insulin: {insulin}')
print(f'nilai 0 pada kolom BMI: {bmi}')

"""Sekarang, semua nilai 0 telah diganti dengan rata-rata dari masing-masing kolom."""

# Cek deskripsi
diabetes.describe()

"""Berdasarkan dari deskripsi stastik, nilai 0 hanya terdapat pada kolom Outcome dan Pregnancies yang merupakan kolom ketegorikal. Sehingga tidak perlu diganti.

## 5.3 Menangani otliers

#### Pregnancies
"""

sns.boxplot(x=diabetes['Pregnancies'])

"""#### Glucose"""

sns.boxplot(x=diabetes['Glucose'])

"""#### BloodPressure"""

sns.boxplot(x=diabetes['BloodPressure'])

"""#### SkinThickness"""

sns.boxplot(x=diabetes['SkinThickness'])

"""#### Insulin"""

sns.boxplot(x=diabetes['Insulin'])

"""#### BMI"""

sns.boxplot(x=diabetes['BMI'])

"""#### Age"""

sns.boxplot(x=diabetes['Age'])

"""### Outcome"""

sns.boxplot(x=diabetes['Outcome'])

"""Jika kita perhatikan kembali, pada beberapa fitur numerik di atas terdapat outliers. Maka, langkah selanjutnya adalah mengatasi outliers tersebut dengan metode IQR."""

Q1 = diabetes.quantile(0.25)
Q3 = diabetes.quantile(0.75)
IQR = Q3 - Q1

diabetes = diabetes[~((diabetes < (Q1 - 1.5 * IQR)) | (diabetes > (Q3 + 1.5 * IQR))).any(axis=1)]

diabetes.shape

diabetes.info()

"""## 5.4 Univariate Analysis

#### Categorical Features
"""

# Pregnancies
count = diabetes['Pregnancies'].value_counts()
percent = 100 * diabetes['Pregnancies'].value_counts(normalize=True)
df = pd.DataFrame({
    'jumlah sampel': count,
    'persentase': percent.round(1)})
print(df)
count.plot(kind='bar', title='Pregnancies')

"""Terdapat 14 kategori pada kolom **Pregnancies**. Berdasarkan dari hasil di atas, dapat disimpulkan bahwa terdapat 13.8% pasien dengan usia kehamilan di atas 8."""

# Outcome
count = diabetes['Outcome'].value_counts()
percent = 100 * diabetes['Outcome'].value_counts(normalize=True)
df = pd.DataFrame({
    'jumlah sampel': count,
    'persentase': percent.round(1)})
print(df)
count.plot(kind='bar', title='Outcome')

"""Terdapat 2 kategori pada kolom target **Outcome**. Berdasarkan dari hasil di atas, dapat disimpulkan bahwa terdapat 69.6% pasien tidak terkena diabetes.

#### Numerical features
"""

diabetes[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].hist(bins=50, figsize=(20, 15))
plt.show()

"""## 5.5 Multivariate analysis
### Categorical features
mengecek rata-rata  terhadap masing-masing fitur untuk mengetahui pengaruh fitur kategori terhadap outcome
"""

fig = plt.figure(figsize=(15,5))
for i,col in enumerate(['Pregnancies','Outcome']):
    ax = fig.add_subplot(1, 2, i + 1)
    sns.countplot(diabetes[col])

"""Berdasarkan dari hasil analisis di atas
- Lebih dari 1000 pasien tidak memiliki diabetes
- Data maksimum berada di 0, 1, dan 2 kehamilan.
"""

fig = plt.figure(figsize=(20,20))
for i, col in enumerate(diabetes.drop(['Pregnancies','Outcome'],axis=1)):
    ax = fig.add_subplot(4, 2, i + 1)
    ax1 = sns.distplot(diabetes[col][diabetes['Outcome']==1],label='Positive')
    sns.distplot(diabetes[col][diabetes['Outcome']==0],label='Negative',ax=ax1)
    plt.legend()

"""Berdasarkan hasil dari analisis di atas, dapat disimpulkan
- Pasien yang memiliki Glukosa pada rentang 125-200 berpeluang tinggi terkena diabetes.
- Pasien yang memiliki teknan darah pad arentang 40-70 berada pada posisi aman dari diabetes.
- Pasien yang memiliki Ketebalan kulit pada rentang 28-45 berpeluang tinggi terkena diabetes.
- Pasien dengan insulin yang rendah ataupun tinggi berpeluang terkena diabetes.
- Pasien yang memiliki BMI pada rentang 30-50 berpeluang terkana diabetes.
- Pasien yang memiliki usia di atas 30 berpeluang tinggi terkena diabetes.
"""

sns.barplot(x='Pregnancies', y='Outcome', data=diabetes, ci=None)

"""Dari graph di atas, dapat diambil kesimpulan bahwa tidak semua peasien dengan kehamilan tinggi berppeluang terkena diabetes, namun peluangnya masih tinggi."""

plt.figure(figsize=(10, 8))
correlation_matrix = diabetes.corr().round(2)
 
# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

"""Pada grafik koreasi di atas, kolom SkinThickness, Insulin, BMI, dan DiabetesPedigreeFuncition memiliki koreasi yang rendah, sehingga kolom tersbut dapat di drop."""

# drop_cols = ['SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction']
# diabetes.drop(columns=drop_cols, inplace=True, axis=1)

"""# 6. Data Preparation

## 6.1 Split Dataset
"""

from sklearn.model_selection import train_test_split

train, test = train_test_split(diabetes)

# train set
x_train = train.iloc[:, 0:8]
y_train = train.iloc[:, 8:9]

# test set
x_test = test.iloc[:, 0:8]
y_test = test.iloc[:, 8:9]

print(f'train: {len(x_train)}')
print(f'test: {len(x_test)}')

"""# 7. Modelling"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import metrics

models = pd.DataFrame(index=['train', 'test'],
                      columns=['KNN', 'DecisionTree', 'RandomForest'])

key = ['KNeighborsClassifier',
       'RandomForestClassifier',
       'AdaBoostClassifier']

value = [KNeighborsClassifier(n_neighbors=17), 
         RandomForestClassifier(n_estimators=20, random_state=12), 
         AdaBoostClassifier()]

models = dict(zip(key,value))

accuracy = pd.DataFrame(columns=['Accuracy'], index=key)

for name, algorithm in models.items():
  model = algorithm
  model.fit(x_train,y_train)
  predict = model.predict(x_test)
  accuracy.loc[name] = accuracy_score(y_test, predict)

accuracy

"""# Evaluation
Beredasarjan hasil pengembangan model dengan menggunakan algoritma KNN, Random Forest, dan AdaBoosting di atas. Dapat disimpulkan bahwa model yang menggunakan algoritma Random Forest memiliki akurasi tertinggi, yaitu 78.7%. Sehingga model ini solusi terbaik untuk melakukan klasifikasi diabetes.
"""

rf_classifier = RandomForestClassifier()
rf_classifier.fit(x_train, y_train)
prediction = rf_classifier.predict(x_test)

confusion_matrix = confusion_matrix(y_test, prediction)

sns.heatmap(confusion_matrix / np.sum(confusion_matrix), annot=True, fmt='.2%')
plt.title('Confusion Matrix pada Random Forest Classifier', fontsize=12)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.show()

from sklearn.metrics import cohen_kappa_score, precision_score, recall_score

score = pd.DataFrame(columns=['Score'])

score.loc['Accuracy'] = accuracy_score(y_test, prediction)
score.loc['Precision'] = precision_score(y_test, prediction)
score.loc['Recall'] = recall_score(y_test, prediction)
score.loc['Kappa'] = cohen_kappa_score(y_test, prediction)

score