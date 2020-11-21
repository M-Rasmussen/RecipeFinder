'''Contorler class'''
import os
import flask
from flask import request
import model as mod


app = flask.Flask(__name__)


@app.route("/", methods=["post", "get"])
def searchfood():
    '''Search for food and return items'''
    ingredients_sp = []
    instructions_sp = []
    if request.method == "POST":
        ### call request api function
        ans = request.form.get("search")
        food_id = mod.item_search(ans)
    else:
        food_id = mod.item_random()

    json_body2 = mod.get_recipe(food_id)
    for item in json_body2["extendedIngredients"]:
        ingredients_sp.append(item["original"])

    for instruct_out in json_body2["analyzedInstructions"]:
        for instruct_in in instruct_out["steps"]:
            instructions_sp.append(instruct_in["step"])

    name_sp = json_body2["title"]
    pic_sp = json_body2["image"]
    link_sp = json_body2["spoonacularSourceUrl"]
    serving_sizesp = json_body2["servings"]
    prep_timesp = json_body2["readyInMinutes"]

    tweeter = mod.twitter_call(name_sp)

    if tweeter != "error":
        return flask.render_template(
            "index.html",
            iName=name_sp,
            iPic=pic_sp,
            iServing=serving_sizesp,
            iMinutes=prep_timesp,
            iIngredients=ingredients_sp,
            iInstructions=instructions_sp,
            itweeterName=tweeter["tweetUserName"],
            itweeterText=tweeter["tweetText"],
            itweeterDate=tweeter["tweetDate"],
            iLink=link_sp,
        )
    return flask.render_template("failcase.html")


if __name__ == "__main__":
    app.run(
        port=int(os.getenv("PORT", 8080)),
        host=os.getenv("IP", "0.0.0.0"),
        debug=True,
        use_reloader=True,
    )
