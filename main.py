
# Import the necessary modules.
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app.
app = Flask(__name__)

# Define the route for the index page.
@app.route('/index')
def index():
    # Render the index.html file.
    return render_template('index.html')

# Define the route for calculating the loyalty points.
@app.route('/calculate_points', methods=['POST'])
def calculate_points():
    # Get the customer's information from the request.
    years_of_membership = int(request.form['years_of_membership'])
    top_up_percentage = int(request.form['top_up_percentage'])
    ttr_transaction_value = int(request.form['ttr_transaction_value'])
    education_units_completed = int(request.form['education_units_completed'])
    points_spent_on_education_unit_discounts = int(request.form['points_spent_on_education_unit_discounts'])
    points_spent_on_education_grants = int(request.form['points_spent_on_education_grants'])
    points_spent_on_financial_advice = int(request.form['points_spent_on_financial_advice'])
    points_spent_on_micro_investments = int(request.form['points_spent_on_micro_investments'])
    points_spent_on_partner_programs = int(request.form['points_spent_on_partner_programs'])

    # Calculate the customer's loyalty points.
    loyalty_points = (
        years_of_membership * 10 +
        top_up_percentage * 5 +
        ttr_transaction_value * 2 +
        education_units_completed * 1
    ) - (
        points_spent_on_education_unit_discounts +
        points_spent_on_education_grants +
        points_spent_on_financial_advice +
        points_spent_on_micro_investments +
        points_spent_on_partner_programs
    )

    # Redirect the user to the results page.
    return redirect(url_for('results', loyalty_points=loyalty_points))

# Define the route for the results page.
@app.route('/results')
def results():
    # Get the loyalty points from the request.
    loyalty_points = int(request.args.get('loyalty_points'))

    # Render the results.html file.
    return render_template('results.html', loyalty_points=loyalty_points)

# Run the app.
if __name__ == '__main__':
    app.run(debug=True)
