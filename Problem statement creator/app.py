
from flask import Flask, render_template, request
import openai
app = Flask(__name__)
# Route for handling form submission and retrieving data
@app.route('/')    
def indexPage():
    return render_template('sample.html')
@app.route('/collect', methods=['GET', 'POST'])
def get_details():
    if request.method == 'GET':
        try:
            x1 = request.args.get('concept')
            x2 = request.args.get('difficulty')
            x3 = request.args.get('optionalText')
            if x3:
                openai.api_key = "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" 
                prompt = f'You have to generate the Problem statement for coding tests based on the given requirments. They will give Concept which you want to choose, Level of the question you want to generate and if possible they will also provide optional text.If they provide any optional text then you have to create the problem statement based on the optional text.Your output should follow some Rules and regulations, Those are, First container should contains heading as "Problem Statement: ",You have to generate good problem statement and have to print below to "Problem statemet".Second Container should contains heading as "Problem Description: ",You have to generate good problem description and have to print below to "Problem Description" heading.Third Container should contains heading as "Sample Input",You have to generate sample input for problem description and have to print below to "sample input".Fourth Container should contains heading as "Sample Output",You have to generate sample output for sample input according to the problem Description and have to print below to "sample output".So note down the requirments Concept is {x1},Level is {x2},optional text is {x3}. Try to generate a good Probelm statement.'
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt,
                max_tokens=400,  
                n=1,
                )
                generated_text = response.choices[0].text.strip()
                print(generated_text)
                s = generated_text
                i = s.find("Problem Description")
                ps = s[:i]
                print(ps)   
                print()
                s = s[i:]
                i = s.find("Sample Input")
                pd = s[:i]
                print(pd)
                print()
                s = s[i:]
                i = s.find("Sample Output")
                si = s[:i]
                print(si)
                print()
                s = s[i:]
                print(s)
                
                return render_template('sample2.html', x1=ps,x2=pd,x3=si,x4=s,r=1)
            else:
                openai.api_key = "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" 
                prompt = f'You have to generate the Problem statement for coding tests based on the given requirments. They will give Concept which you want to choose, Level of the question you want to generate and if possible they will also provide optional text.If they provide any optional text then you have to create the problem statement based on the optional text, otherwise generate the problem statement based on your own assumptions.Your output should follow some Rules and regulations, Those are, First container should contains heading as "Problem Statement",You have to generate good problem statement and have to print below to "Problem statemet" in .Second Container should contains heading as "Problem Description" ,You have to generate good problem description and have to print below to "Problem Description" .Third Container should contains heading as "Sample Input" ,You have to generate sample input for problem description and have to print below to "sample input" .Fourth Container should contains heading as "Sample Output",You have to generate sample output for sample input according to the problem Description and have to print below to "sample output".So note down the requirments Concept is {x1},Level is {x2}. Try to generate a good Probelm statement.'
                print(prompt)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt,
                max_tokens=400,  
                n=1,
                )
                generated_text = response.choices[0].text.strip()
                return render_template('sample2.html', x1=generated_text,r="None")
        except Exception as e:
            return render_template('sample.html')
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, request
import openai
app = Flask(__name__)
# Route for handling form submission and retrieving data
@app.route('/')    
def indexPage():
    return render_template('sample.html')
@app.route('/collect', methods=['GET', 'POST'])
def get_details():
    if request.method == 'GET':
        try:
            x1 = request.args.get('concept')
            x2 = request.args.get('difficulty')
            x3 = request.args.get('optionalText')
            openai.api_key = "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" 
            #prompt = f'You have to generate the Problem statement for coding tests based on the given requirments. They will give Concept which you want to choose, Level of the question you want to generate and if possible they will also provide optional text.If they provide any optional text then you have to create the problem statement based on the optional text.Your output should follow some Rules and regulations, Those are, First container should contains heading as "Problem Statement",You have to generate good problem statement and have to print below to "Problem statemet".Second Container should contains heading as "Problem Description",You have to generate good problem description and have to print below to "Problem Description" heading.Third Container should contains heading as "Sample Input",You have to generate sample input for problem description and have to print below to "sample input".Fourth Container should contains heading as "Sample Output",You have to generate sample output for sample input according to the problem Description and have to print below to "sample output".So note down the requirments Concept is {x1},Level is {x2},optional text is {x3}. Try to generate a good Probelm statement.'
            prompt1 = f'You have to Generate the Problem statement for coding tests based on the given requirments. Generate the problem statement heading based on {x1} concept.You have to generate good problem statement.Give the content in the format <Problem statement>. Eg: Maximum number'
            print(prompt1)
            response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  
            prompt=prompt1,
            max_tokens=10,  
            n=1,
            )
            generated_text1 = response.choices[0].text.strip()
            if x3:
                prompt2 = f'You have to Generate the Problem description for coding test based on {generated_text1} choosen as {x1} concept. The most important thing is, Choose {x2} as difficulty level. Example:Try to find the maximum number in the given list'
                print(prompt2)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt2,
                max_tokens=400,  
                n=1,
                )
                generated_text2 = response.choices[0].text.strip()
                prompt3 = f'You have to Generate only Sample input for coding test based on {generated_text2} problem description,choosen as {x1} concept, Create problem desription by using {x3}. Example- 1 2 3 4 5'
                print(prompt3)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt2,
                max_tokens=100,  
                n=1,
                )
                generated_text3 = response.choices[0].text.strip()
                prompt4 = f'You have to Generate only Sample output for {generated_text3} . Example: 5'
                print(prompt4)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt2,
                max_tokens=100,  
                n=1,
                )
                generated_text4 = response.choices[0].text.strip()
                return render_template('sample2.html', x1=generated_text1,x2=generated_text2,x3=generated_text3,x4=generated_text4,r=1)
            else:
                prompt2 = f'You have to Generate the Problem description for coding test based on {generated_text1} choosen as {x1} concept. The most important thing is, Choose {x2} as difficulty level. Example: Print the Maximum number in the given list'
                print(prompt2)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt2,
                max_tokens=400,  
                n=1,
                )
                generated_text2 = response.choices[0].text.strip()
                prompt3 = f'You have to Generate only Sample input for coding test based on {generated_text2} problem description. Example: 1 2 3 4 5'
                print(prompt3)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt2,
                max_tokens=100,  
                n=1,
                )
                generated_text3 = response.choices[0].text.strip()
                prompt4 = f'You have to Generate only Sample output for {generated_text3} based on {generated_text2},choosen as {x1} concept.Example: 5'
                print(prompt4)
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  
                prompt=prompt2,
                max_tokens=100,  
                n=1,
                )
                generated_text4 = response.choices[0].text.strip()
                return render_template('sample2.html', x1=generated_text1,x2=generated_text2,x3=generated_text3,x4=generated_text4,r="None")
        except Exception as e:
            return render_template('sample.html')
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(debug=True)
'''

