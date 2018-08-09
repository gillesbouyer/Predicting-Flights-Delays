### Running the Delay App
Go to the directory where main.py is(cd '05 DelayApp').
Type 'python main.py' at a terminal 
Copy paste the ip which is returned on the terminal in a browser, press enter
Enter your data and click on the yellow button 

**Step 1: The model in pickle format**
* The model was created in: 03 Airlines Delay Prediction Models.ipynb
It is a logistic regression with 27 features predicting if there is a delay
The "talking" features are delay at departure and distance.

**Step 2: The files**
Four files are needed for this to work: 3 are in the '05 Delay app' directory, 1 in 'templates' subdirectory of '05 Delay app'.
1. `main.py` - This is the main Python code that uses Flask and calls py_flights_delays.py to use the model
2. `py_flights_delays.py` - This is a separate Python script that reads in the pickled model and also preps the data for the model
3. `savelogpreg.p` - The pickled model
4. `index.html` (in a templates folder)-!!important!! - This is the webpage that will be able to take inputs for the model and output a result on the webpage
