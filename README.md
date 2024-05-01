## Flask Application Design

### HTML Files

**index.html:**

- The main page of the application, containing an input form for the customer's details and a button to calculate their loyalty points.

**results.html:**

- Displays the calculated loyalty point balance of the customer based on their input.

### Routes

**@app.route('/index')**

- The route for the index page, serving the `index.html` file.

**@app.route('/calculate_points', methods=['POST'])**

- The route for calculating the customer's loyalty points based on their submitted details.
  - This route handles the POST request, collects the customer's information, and performs the necessary calculations.
  - After processing, it redirects the user to the `results.html` page with the calculated point balance.

### Functionality

The application calculates a customer's loyalty points based on their years of membership, top-up percentage, TTR transaction value, and education units completed. It also takes into account the points spent on various services and discounts. This calculation is performed in the backend using Flask's form handling capabilities. The result, i.e., the customer's loyalty point balance, is displayed on the `results.html` page.