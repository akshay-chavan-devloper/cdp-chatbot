from flask import Flask, request, jsonify, render_template import spacy import os 
 
app = Flask(__name__) 
 
# Load the spaCy NLP model nlp = spacy.load("en_core_web_sm") # Load the documentation data from files def load_documentation(): 
docs = {} for filename in os.listdir("documentation"): with open(f"documentation/{filename}", "r") as f: 
docs[filename.split(".")[0]] = f.read() return docs 
 
documentation = load_documentation() 
 
@app.route('/') def home(): 
return render_template('index.html') 
 
@app.route('/ask', methods=['POST']) def ask(): 
question = request.json.get('question', '') doc = nlp(question) 
 
# Check keywords in the question and match them to documentation if "source" in question.lower(): 
answer = documentation["segment"] 
elif "profile" in question.lower(): answer = documentation["mparticle"] elif "audience" in question.lower(): answer = documentation["lytics"] elif "integrate" in question.lower(): answer = documentation["zeotap"] else: 
answer = "I'm sorry, I can only help with questions about Segment, mParticle, Lytics, and Zeotap." 
 
return jsonify({"answer": answer}) 
 
if __name__ == '__main__': 
app.run(debug=True) 
