from flask import Flask, request, render_template
from py_flights_delays import flight_delay

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_delay/', methods=['GET', 'POST'])

def render_message():

    # user-entered ingredients
    ingredients = ['flightnum','originairportid','depdelay', 'destairportid',
                   'month','dayofweek', 'distance']

    # error messages to ensure correct units of measure
    messages = ["Invalid Flight Number",
                "Invalid Departure City",
                "The delay at departure must be a number without comma.",
                "Invalid Destination City",
                "Month is a number between 1(Jan) and 12(Dec)",
                "Day of the week is between 1(Sunday) and 7(Saturday)",
                "distance must be a number without comma"]

    # hold all amounts as floats

    lesdonnees = []
    render_template('index.html', message=" ")
    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(ingredients):
        user_input = request.form[ing]
        try:
#            print("aaa",user_input)
            data_entered = str(user_input)
        except:
            return render_template('index.html', message=messages[i])
        lesdonnees.append(data_entered)
#        print("amounts",amounts)
    # show user final message
#    print("before final_message")
    final_message = flight_delay(lesdonnees)
#    print("after final_message")
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)
