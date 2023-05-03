from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' 

@app.route('/dojo') 
def dojo():
    return 'Dojo!'  
                   
@app.route('/say/<string:name>') 
def name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>') 
def hi(num, word):
    return f"{word * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run 