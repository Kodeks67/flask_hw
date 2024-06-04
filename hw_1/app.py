from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/category/<category>')
def category(category):
    categories = {
        'clothes': ['Jacket', 'T-shirt', 'Jeans'],
        'shoes': ['Sneakers', 'Boots', 'Sandals']
    }
    return render_template('category.html', category_name=category.capitalize(), products=categories.get(category, []))


@app.route('/product/<product_name>')
def product(product_name):
    return render_template('product.html', product_name=product_name)


if __name__ == '__main__':
    app.run(debug=True)
