from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


@app.route("/generate", methods=["POST"])
def generate_menu():
    restaurant_name = request.form.get("nome_ristorante", "").strip()
    template_style = request.form.get("template_stile", "classic").strip()

    category_names = request.form.getlist("categoria_nome[]")
    menu = []

    for index, category_name in enumerate(category_names):
        clean_category_name = category_name.strip()

        dish_names = request.form.getlist(f"nome_piatto_{index}[]")
        dish_prices = request.form.getlist(f"prezzo_piatto_{index}[]")

        dishes = []

        for dish_name, dish_price in zip(dish_names, dish_prices):
            clean_dish_name = dish_name.strip()
            clean_dish_price = dish_price.strip()

            if clean_dish_name and clean_dish_price:
                dishes.append({
                    "nome": clean_dish_name,
                    "prezzo": clean_dish_price
                })

        if clean_category_name and dishes:
            menu.append({
                "nome": clean_category_name,
                "piatti": dishes
            })

    return render_template(
        "menu_preview.html",
        nome_ristorante=restaurant_name,
        template_stile=template_style,
        menu=menu
    )


if __name__ == "__main__":
    app.run(debug=True)