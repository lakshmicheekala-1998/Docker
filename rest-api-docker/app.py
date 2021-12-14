from flask import Flask,jsonify, render_template, request, redirect,url_for,escape
import json


app = Flask(__name__)
jData = json.loads(open('./foods.json').read())
data=jData["Foods"]

@app.route('/')
def food_main():
    return render_template("index.html")

@app.route('/foodList/')
def getAllFoods():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)


@app.route('/foodList/<string:Calories>/')
def getcalories(Calories=''):
    myList=[]
    for element in data:
        if element["Calories"] == Calories:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)




@app.route('/foodList/<string:Calories>/<string:Protein>/')
def getprotein(Calories, Protein):
    myList=[]
    for element in data:
        if element["Calories"]== Calories:
            if element ["Protein"] == Protein:
                myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)



@app.route('/foodList/<string:Calories>/<string:Protein>/<string:Carbs>')
def getcarbs(Calories, Protein, Carbs):
    myList=[]
    for element in data:
        if element["Calories"]== Calories:
            if element ["Protein"] == Protein:
                if element ['Carbs'] == Carbs:
                    myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')