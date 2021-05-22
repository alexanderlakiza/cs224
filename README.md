# Computational Linguistics
###### The course is taught by Chernysheva Anastasiia Vladimirovna [(ISU)](https://isu.ifmo.ru/pls/apex/f?p=2143:PERSON:102085728817403::NO:RP:PID:182049)
---
### This repo is intended for posting my solutions of the course's tasks
###### Check [1sem branch](https://github.com/alexanderlakiza/cs224/tree/1sem) in order to see the final task of the 1st semester
###### Whole course is in russian
---
## Homeworks Status Table

| № | Title | Files | Status | Points |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Collecting Data | [task1.py](https://github.com/alexanderlakiza/cs224/blob/main/task1/task1.py) | Verified | 10/10 |
| 2 | Regular Expressions | [task2.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task2/task2.ipynb) | Verified | 10/10 |
| 3 | Lev. Distance | [task3.py](https://github.com/alexanderlakiza/cs224/blob/main/task3/task3.py) and [task3_ui.py](https://github.com/alexanderlakiza/cs224/blob/main/task3/task3_ui.py)  | Verified | 10/10 |
| 4 | POS Tagging | [task4.py](https://github.com/alexanderlakiza/cs224/blob/main/task4/task4.py) and [task4_stat.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task4/task4_stat.ipynb) | Verified | 10/10 |
| 5-6 | Text Vectorization | [task5-6.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task5-6/task5-6.ipynb) | Is being checked |  |
| 7 | Word2Vec |  | In progress |  |
| 8 | Key Words Graph | [task8.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task8/task8.ipynb) | Is being checked |  |
| 9 | Document Clustering | [task9.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task9/task9.ipynb) | Is being checked |  |
| 10 | Topic Modeling (LDA) | [task10.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task10/task10.ipynb) | Is being checked |  |

---
## Full description of each task
###### All the comments inside the files are in russian, as the course is taight in russian.
1. __Collecting Data__ 
    The aim of the task is to collect more than 200 documents (totally volumed of more than 10000 words) using Python from diferent sources, for example, vk.com groups, wikipedia, etc. I decided to use wikipedia API as it was my first experience of using it.  
    The files of this task are:
    * [task1.py](https://github.com/alexanderlakiza/cs224/blob/main/task1/task1.py)
    In the file you can check comments in order to understand what I did step by step.
    
2. __Regular Expressions__ 
    The aim of this task is to get familiar with Python regular expressions. The task is divided into 2 parts. The first part includes 10 mini tasks in order to get used to the syntax of regular expressions. The second part includes the process of cleaning the data collected in the 1st task.  
    The files of this task are:
    * [task2.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task2/task2.ipynb)
    In the file you can check comments in order to understand what I did step by step.
     
3. __Levenshtein Distance__ 
    The aim of this task is to get familiar with Levenshtein Distance. The task is to write a function that will show ids of documents where the word entered by user appears. A function must have exceptions in case of misspellings or absence of entered word. In order to check how the function works you need to run task3_ui.py and follow instructions.  
    The files of this task are:
    * [task3.py](https://github.com/alexanderlakiza/cs224/blob/main/task3/task3.py) 
    * [task3_ui.py](https://github.com/alexanderlakiza/cs224/blob/main/task3/task3_ui.py)

4. __POS Tagging__ 
    The aim of this task is to tag parts of speech in the corpus, then find unusual documents where a ratio of any part of speech differs by a value greater than two standard deviations. Unusual documents are introduced in task4_stat.ipynb.  
    The files of this task are:
    * [task4.py](https://github.com/alexanderlakiza/cs224/blob/main/task4/task4.py)
    * [task4_stat.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task4/task4_stat.ipynb)

5. __Text Vecorization__
    In this task you had to choose a dataset with classified texts and then build and train the MultinomialNB() model by first vectorizing the texts. The following vectorizers were used in this task: n-grams, n-char-grams and TF-IDF.  
    The task was completed jointly with Darya Plotskaya and Emina Iskhakova (both K3242)  
    The files of this task are:
    * [task5-6.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task5-6/task5-6.ipynb)

6. __Text Vecorization__
    Tasks №5 and №6 are combined.

7. __Word2Vec__

8. __Key Words Graph__
    The aim of this task is to plot a pgrap of key words of our corpus. Key words are nouns that were used most. I used networkx library in this task.  
    The files of this task are:
    * [task8.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task8/task8.ipynb)

9. __Document Clustering__    
    The aim of this task is to clusterize documents of our corpus based on NER (Named-Entity-Recognition).  
    The files of this task are:
    * [task9.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task9/task9.ipynb)

10. __LDA Topic Modeling__
    The aim of this task is to make topic modeling (based on LDA) of documents of our corpus. Gensim and pyLDAvis are our friends in this task.  
    The files of this task are:
    * [task10.ipynb](https://github.com/alexanderlakiza/cs224/blob/main/task10/task10.ipynb) 
---

# Who am I?
My name is Alexander Lakiza. I am an undergraduated [ITMO University](https://itmo.ru/ru/) student studying 45.03.04 bachelor [Intelligent systems in the humanities](https://abit.itmo.ru/program/14533/) (the group id is K3242).
## Where you can find me?
* [VK](https://vk.com/alexanderlakiza)
* [Instagram](https://www.instagram.com/alexlakiza/)
* [Twitter](https://twitter.com/alexlakiza)
* [ISU](https://isu.ifmo.ru/pls/apex/f?p=2143:PERSON:102085728817403::NO:RP:PID:285469) (ITMO Web-system)