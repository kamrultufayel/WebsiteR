from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Placeholder for form submission handling
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        
        
        
        # For now, redirecting to the home page
        return redirect(url_for('home'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
