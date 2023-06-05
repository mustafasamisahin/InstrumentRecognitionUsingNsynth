# Music Instrument Recognition Using Machine Learning

Author: Mustafa Sami Şahin

## Introduction
In this project, I attempted to recognize musical instruments within the Nsynth dataset using audio recordings of 11 different instruments provided in the dataset.

## Literature Review
During my research on similar topics, I came across several related works. One of them is "Music Instrument Detection Using LSTMs and the Nsynth Dataset" [1]. In this work, the author proposed processing the Nsynth dataset using Long Short-Term Memory (LSTM) algorithms but did not implement the processing steps, leaving them for future work. Another study I found is titled "Can We Guess Musical Instruments With Machine Learning?" [2]. In this study, the author applied the Nsynth dataset to the Librosa library, extracting five different features for each audio file. These features were then tested using four different algorithms, and the success rates were reported. Among these four algorithms, Naive Bayes and Support Vector Machines had success rates below 15% and were eliminated. The Random Forest algorithm was chosen over the Convolutional Neural Networks algorithm because it was significantly faster. However, even the Random Forest algorithm, which had the highest success rate among the four algorithms, achieved only 65% accuracy after various adjustments and modifications.

Based on the second study, I attempted to achieve similar success rates by using different features in my work.

## Methods
I chose the K-Nearest Neighbors (KNN) algorithm for my approach. To run the algorithm, I used Python along with the Pandas, Numpy, and Scikit-learn libraries. I used Python version 3.8.5. Before starting the project, I used Jupyter Notebook to examine the dataset and explore its contents and potential features that could be used in the project.

## Implementation
The "Train" portion of the dataset consists of 289,205 audio files, each consisting of a single note lasting 4 seconds. It also includes one JSON file associated with these audio files. The "Test" portion contains 4,096 files following the same structure. These files may include acoustic, electronic, and synthetic versions of 11 different instruments. 

To reduce unnecessary complexity in the dataset, I needed to remove unused information. To do this, I used Jupyter Notebook to analyze the minimum, maximum, mean, and total values of each field in the dataset. Since the sampling rate was the same for all files, I removed the sampling rate. Additionally, I needed to remove certain information related to the class attribute, which is the instrument we are trying to classify. Some information was stored both as numeric and string values, and I removed those stored as strings.

Next, I had to separate the "Qualities" data within the dataset into individual variables. This allowed me to use these data in the algorithm. The data provided to the algorithm included:
- Note
- Fret
- Velocity
- Heights of frequencies
- Distortion
- Quick decay
- Long release
- Polyphony
- Strike
- Echo
- Tempo consistency

I then passed these data to the KNeighborsClassifier function provided by the Scikit-learn library, along with various parameters. After training the model, I tested it using the test files and compared the results to determine the percentage of correct classifications.

## Results
In my initial attempts, I achieved success rates of around 20% by running the algorithm with 3 neighbors. With different arguments, I was able to increase this rate to a maximum of 36.89%. Finally, I achieved this rate with 13 neighbors. In the next steps, I plan to remove some of the data headers mentioned under the "Implementation" section to create a more meaningful dataset and improve

 the success rate to an acceptable level. Similarly, I plan to exclude some instruments from the dataset if I believe they have insufficient data for accurate classification. As a further development, I will attempt to make the program listen to a music file and count the number of instruments present.

## References
[1] Brandi Frisbie, Stanford University, USA. "Music Instrument Detection Using LSTMs And The Nsynth Dataset." [Link](https://ccrma.stanford.edu/groups/meri/assets/pdf/frisbie2017ISMIR_LBD.pdf)

[2] Nadim Kawwa, Udacity Machine Learning Engineer Nanodegree. "Can We Guess Musical Instruments With Machine Learning?" [Link](https://medium.com/@nadimkawwa/can-we-guess-musical-instruments-with-machine-learning-afc8790590b8)
