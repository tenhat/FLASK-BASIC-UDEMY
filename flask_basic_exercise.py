from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Product Page</h1>"


@app.route("/product/<product_id>")
def product(product_id):
    product_list = [["1", "ノートパソコンA", "Core i5", "68000"],
                    ["2", "ノートパソコンB", "Core i7", "98000"],
                    ["3", "ノートパソコンC", "Core i9", "128000"]]
    for product in product_list:
        if product_id in product:
            break
    product_name = product[1]
    product_cpu = product[2]
    product_price = product[3]
    return "<h1>{0}</h1><p>CPU: {1}</p><p>価格: {2}</p>".format(product_name, product_cpu, product_price)


# debug mode
if __name__ == "__main__":
    app.run(debug=True)
