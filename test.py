from flask import Flask
import safygiphy
g = safygiphy.Giphy()
r = g.random(tag="macross")
# Will return a random GIF with the tag "success"

app = Flask(__name__)
 
@app.route("/")
def home():
    return '<body background="%s" no-repeat>' % (r['data']['image_original_url'])
    return 

print
 
app.run(debug=False)
