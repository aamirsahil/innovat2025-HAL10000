from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('message', '').strip()
        
        if user_input == '1':
            message = 'Hello'
        elif user_input == '2':
            message = 'Hi'
        elif user_input == '3':
            message = 'Gello'
        else:
            message = 'Invalid input'
            
        return render_template('result.html', message=message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)