from flask import Flask, render_template
import apriori as api

app = Flask(__name__)

@app.route('/')
def index():
	products = api.get_products()
	return render_template('index.html', products=products)

if __name__ == "__main__":
	app.run(debug=True)


