
# Proje Açıklaması

Bu proje CENG625 Advanced Topics in Artificial Intelligence (Dr. Tuncay Bayrak) dersi için yapılmaktadır ve onun repository'sidir.


# Data Generator

Data Generator, https://physionet.org/content/big-ideas-glycemic-wearable/1.1.0/ linkinde bulunan raw datayı pre-processing approachtan geçirerek belirli feature'lar üretmektedir.
Bu folderın altında her time series database kullanılarak feature üretilmesi planlanmaktadır. Şu ana kadar yapılan geliştirmenin çalışması için, linkte bulunan datasetin indirilmesi gerekmektedir. Ardından örnek bir yapı olarak indirilen datanın aşağıdaki şekilde her bir csv dosyası için konulması gerekmektedir;

* Participants/Participant_1/ACC_001.csv
* Participants/Participant_2/ACC_002.csv
* Participants/Participant_3/ACC_003.csv

Yukarıda bahsedilen structure, her participant ve her csv dosyası için yapılmalıdır. Data Generator bu pathteki dosyaları loop ile gezerek, her participant için gerekli featureları üretecektir.

# Models
Modeller dosyasının altında, classification için kullanılan her model bulunmaktadır.

Seçilen modeller;
* Logistic Regression
* SVM
* Decision Tree
* KNN
* Naive Bayes

Bu modelleri, aşağıdaki her feature extraction yöntemi ile geliştirilmiştir;
* Principal Component Analysis (PCA)
* Linear Discriminant Analysis (LDA)
* Factor Analysis (FA)