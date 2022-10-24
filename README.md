# Pneumonia Detection App - Data Camp project

## Created by Fatima-Zahra IBRAHIMI / Arthur GODINHO / Anne-Julie HOTTIN

### Presentation of the project
During this project, we were asked to design an application that received images from chest X-rays. Next, we needed to create a machine learning algorithm that would allow us to detect whether or not the patient has pneumonia. The final step is therefore to display the result of this prediction.


### Description of the folder
In this folder you will find different files. 
Model.ipynb is the notebook containing our machine learning model. 
Test_image.ipynb is a notebook to test our model on a single image. 
Model_test.h5 is our registered model in order to use it in our application, since the fitting of the model is very long, so we save it beforehand.
Requiremenrs.txt is used to see the depencies of the project.
The last file is final_version.py. It is a python file that we use to model our work on a Streamlit application.

### Requirements 
List of requirements on file "Requirements.txt".

### How to run our model ?
We couldn't put the "chest_xray" file on GitHub. To run the project you must therefore download it via this link: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
To create our model just run the cells of the notebook Model.ipynb. The fitting takes about 20 minutes, and then we save our model in the Test_model.h5 file.
Our website is https://streamlitdatacamp.azurewebsites.net.

### How to run our application ?
If you want to launch our application from our files, you just have to open an anaconda terminal on your environment, make sure that the dependencies are well installed. If you want to launch our application from our files, you just have to open an anaconda terminal on your environment, make sure that the dependencies are well installed. Then, you have to make a cd to move to the folder where you pasted our project. Then you enter the command:
`streamlit run final_version.py`
That's it ! 




