from flask import Flask, render_template
import json



app = Flask(__name__)

@app.route('/')
def health():

    with open('C:/Users/rhill/Desktop/rhillx_projex/examfx_sim/qna-health.json') as f:
        data = json.load(f)

        pair = data.items()
           
    
        return render_template('health.html', pair=pair )

@app.route('/life')
def life():

    with open('C:/Users/rhill/Desktop/rhillx_projex/examfx_sim/qna-life.json') as f:
        data = json.load(f)

        pair = data.items()
           
    
        return render_template('life.html', pair=pair )




