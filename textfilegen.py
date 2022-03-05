import json

with open("satsapi.json") as apijsondata:
    apidata = json.load(apijsondata)[0]["data"]

with open("menu.json") as menujsondata:
    menudata = json.load(menujsondata)
text = ""
for meal in menudata:
    text += str(meal["name"]) + "\n" + "\n"
    for dish in meal["setmeals"]:
        del dish["name"]
        dish.update(
            (list(filter(lambda x: (x["qrCode"] == dish["mealurls"]), apidata)))[0]
        )
        text += (
            str(dish["mealtype"])
            + "\n"
            + str(dish["name"])
            + "\n"
            + "Calories: "
            + str(dish["totalCalorie"])
            + str(dish["calorieUOM"])
            + "\n"
            + "Carbohydrate: "
            + str(dish["totalCarbohydrate"])
            + str(dish["carbohydrateUOM"])
            + "\n"
            + "Total Protein: "
            + str(dish["totalProtein"])
            + str(dish["proteinUOM"])
            + "\n"
            + "Total Fat: "
            + str(dish["totalFat"])
            + str(dish["fatUOM"])
            + "\n"
            + "\n"
        )

print(text)


with open("menu2.json", "w") as file:
    json.dump(menudata, file)

with open("summary.txt", "w") as file:
    file.write(text)
