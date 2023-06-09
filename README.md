#  Diabetes Predictors 
Machine Learning model for predicting diabetes based on personal and health-related features with a simple GUI.<br>
<p style="text-align: center;">
<img src="pictures/image-ui.png" width="400"/>
</p>


## Demo
Here is a sample of using our model:<br>
<br>
<img src="pictures/demo.jpg" width="400"/>

## Project Structure

The project is structured as follows:

- You can find all used dataset in "Datasets" directory.
- EDA on data, classic models and UI implementation are in ml_model.ipynb notebook and MLP implementation is in MLP_Model.ipynb notebook.
- You can find saved models with .sav file type for classic models and .pth file type for MLP model.
- The Code for creating .exe application is stored in app.py file and you can find the created executable file in "App" directory.

## Getting Started
To get started with this project as a developer, please follow these steps:

- First, clone the repository.
- You can change the UI and reproduce the result of classic models using ml_model.ipynb notebook. Also, you can reproduce MLP model results using MLP_Model.ipynb notebook.
- At the end, to change .exe file you can apply your changes to app.py file and run the last cells of ml_model.ipynb notebook.

If you just need the application, you can download it from [here](https://github.com/AmBadAl/Diabetes/dist).

## Implemented Models
we have implemented the following models on our dataset:

- LSTM Model
- Classic Models
  - Linear Regression
  - Random Forest
  - SVM
  - Logistic Regression
- MLP Model

After evaluation, we found out that the Random Forest model outperforms the other models and we use this model for our prediction system.

## Results 
| Model | Accuracy on test set |
| :---: |     :---:      |
|  LSTM  |  72.38 %  |
| Linear Regression   |  73.51 %  |
| Random Forest  |  73.78 %  |
| Linear Regression   |  73.36 %  |
| SVM |  73.71 %  |
| MLP |  73.37 %  |

### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 



## Team

[![Ali Mehrabani](https://github.com/AmBadAl/Diabetes/blob/main/pictures/DALL%C2%B7E%202023-06-13%2023.11.47%20-%20cute%20high%20quality%20animationary%20robots%20images%20colorful.png)](https://github.com/AliMehrabani) | [![Amirreza Bagheri](https://github.com/AmBadAl/Diabetes/blob/main/pictures/DALL%C2%B7E%202023-06-13%2023.11.56%20-%20cute%20high%20quality%20animationary%20robots%20images%20colorful.png)](https://github.com/AmBadAl) | [![Amirhossein Nedaeipour](https://github.com/AmBadAl/Diabetes/blob/main/pictures/DALL%C2%B7E%202023-06-13%2023.38.03%20-%20cute%20high%20quality%20animationary%20robots%20images%20colorful.png)](https://github.com/nedaei79)|[![Paniz Halvachi](https://github.com/AmBadAl/Diabetes/blob/main/pictures/DALL%C2%B7E%202023-06-13%2023.11.53%20-%20cute%20high%20quality%20animationary%20robots%20images%20colorful.png)](https://github.com/panizhalvachi)
---|---|---|---
[Ali Mehrabani](https://github.com/AliMehrabani) |[Amirreza Bagheri](https://github.com/AmBadAl) |[Amirhossein Nedaeipour](https://github.com/nedaei79)|[Paniz Halvachi](https://github.com/panizhalvachi)

Thanks DALL·E for generating the above picture profiles!

## License
MIT


