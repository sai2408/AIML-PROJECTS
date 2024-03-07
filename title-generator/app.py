
from flask import Flask, render_template, request
import openai
app = Flask(__name__)
# Route for handling form submission and retrieving data
@app.route('/')    
def indexPage():
    return render_template('appy.html')
@app.route('/collect', methods=['GET', 'POST'])
def get_details():
    if request.method == 'GET':
        try:
            x3 = request.args.get('optionalText')
            if x3:
                openai.api_key = "api" 
                prompt = f'Generte the Title for the given description. It should have deep meaning based on the description. The description is {x3}'
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt,
                max_tokens=100,  
                n=1,
                )
                generated_text = response.choices[0].text.strip()
                print(generated_text)
                return render_template('appy2.html', r = generated_text)
            else:
                return render_template('appy2.html', r = "Try Again, some Error Occured")
        except Exception as e:
            return render_template('appy.html')
    return render_template('appy.html')

if __name__ == '__main__':
    app.run(debug=True)

