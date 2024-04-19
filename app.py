from flask import Flask, render_template, request
import json
import random
from helper import get_card_info

app = Flask(__name__, template_folder="E:\\website\\Project\\templates", static_folder='E:\\website\\Project\\static')

janeeorakel = {
    "ja": [
        "Ja, absoluut.",
        "Zeker weten.",
        "Het ziet er goed uit.",
        "Alle tekenen wijzen op ja.",
        "Dat lijkt waarschijnlijk.",
        "Ja, dat is mogelijk.",
        "De omstandigheden zijn gunstig.",
        "Absoluut, zonder twijfel."
    ],
    "nee": [
        "Nee, helaas niet.",
        "Het lijkt er niet op.",
        "Dat ziet er niet goed uit.",
        "Alle tekenen wijzen op nee.",
        "Dat lijkt onwaarschijnlijk.",
        "Nee, dat is niet mogelijk.",
        "De omstandigheden zijn niet gunstig.",
        "Absoluut niet, zonder twijfel."
    ],
    "neutraal": [
        "Het is onduidelijk.",
        "Ik kan niet zeggen.",
        "Het antwoord is niet duidelijk.",
        "Het is niet zeker.",
        "Misschien later.",
        "Probeer het opnieuw later.",
        "Vraag het opnieuw."
    ]
}

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/index.html")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kaarten", methods=["GET"])
def kaarten():
    kaarten= []
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            kaarten.append(card)
        
        return render_template("kaarten.html", kaarten=kaarten)    
    
    
@app.route("/leggingen", methods=["GET"])
def leggingen():
    return render_template("/leggingen.html")

@app.route("/dagkaart", methods=["GET", "POST"])
def dagkaart():
    if request.method == "GET":
        return render_template("/dagkaart.html")
    if request.method == "POST":
        with open('card_data.json', 'r') as file:
            data = json.load(file)
            cards = data.get('cards', [])
            card = random.choice(cards)
            return render_template("/dagkaart.html", card=card)
        
        
@app.route("/driekaart", methods=["GET", "POST"])
def driekaart():
    if request.method == "GET":
        return render_template("/driekaart.html")
    if request.method == "POST":
        with open('card_data.json', 'r') as file:
            data = json.load(file)
            cards = data.get('cards', [])
            gekozen = random.sample(cards, 3)
            return render_template("/driekaart.html", gekozen=gekozen)
        
@app.route("/kruis", methods=["GET", "POST"])
def kruis():
    if request.method == "GET":
        return render_template("kruis.html")
    if request.method == "POST":
        with open('card_data.json', 'r') as file:
            data = json.load(file)
            cards = data.get('cards', [])
            gekozen = random.sample(cards, 10)
            return render_template("/kruis.html", gekozen=gekozen)
        
@app.route("/janee", methods=["GET", "POST"])
def janee():
    if request.method == "GET":
        return render_template("/janee.html")
    if request.method == "POST":
        antwoordtype = random.choice(list(janeeorakel.keys()))
        gekozen = random.choice(janeeorakel[antwoordtype])
        return render_template("/janee.html", gekozen=gekozen)


@app.route("/ar", methods=["GET"])
def ar():
    matching_cards = []
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            if card.get('type') == 'major':
                matching_cards.append(card)
    
        return render_template("/ar.html", matching_cards=matching_cards)
    
@app.route("/cu", methods=["GET"])
def cu():
    matching_cards = []
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            if card.get('suit') == 'bekers':
                matching_cards.append(card)
    
        return render_template("/cu.html", matching_cards=matching_cards)
    
@app.route("/wa", methods=["GET"])
def wa():
    matching_cards = []
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            if card.get('suit') == 'staven':
                matching_cards.append(card)
    
        return render_template("/cu.html", matching_cards=matching_cards)
    
@app.route("/pe", methods=["GET"])
def pe():
    matching_cards = []
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            if card.get('suit') == 'pentakels':
                matching_cards.append(card)
    
        return render_template("/cu.html", matching_cards=matching_cards)
    
@app.route("/sw", methods=["GET"])
def sw():
    matching_cards = []
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            if card.get('suit') == 'zwaarden':
                matching_cards.append(card)
    
        return render_template("/cu.html", matching_cards=matching_cards)
    


@app.route("/ar00",methods=["GET"])
def ar00():
    card_info = get_card_info("ar00")
    return render_template("/ar00.html", card_info=card_info)

@app.route("/ar01",methods=["GET"])
def ar01():
    card_info = get_card_info("ar01")
    return render_template("/ar01.html", card_info=card_info)

@app.route("/ar02",methods=["GET"])
def ar02():
    card_info = get_card_info("ar02")
    return render_template("/ar02.html", card_info=card_info)

@app.route("/ar03",methods=["GET"])
def ar03():
    card_info = get_card_info("ar03")
    return render_template("/ar03.html", card_info=card_info)

@app.route("/ar04",methods=["GET"])
def ar04():
    card_info = get_card_info("ar04")
    return render_template("/ar04.html", card_info=card_info)

@app.route("/ar05",methods=["GET"])
def ar05():
    card_info = get_card_info("ar05")
    return render_template("/ar05.html", card_info=card_info)

@app.route("/ar06",methods=["GET"])
def ar06():
    card_info = get_card_info("ar01")
    return render_template("/ar06.html", card_info=card_info)

@app.route("/ar07",methods=["GET"])
def ar07():
    card_info = get_card_info("ar07")
    return render_template("/ar07.html", card_info=card_info)

@app.route("/ar08",methods=["GET"])
def ar08():
    card_info = get_card_info("ar08")
    return render_template("/ar08.html", card_info=card_info)

@app.route("/ar09",methods=["GET"])
def ar09():
    card_info = get_card_info("ar09")
    return render_template("/ar09.html", card_info=card_info)

@app.route("/ar10",methods=["GET"])
def ar10():
    card_info = get_card_info("ar10")
    return render_template("/ar10.html", card_info=card_info)

@app.route("/ar11",methods=["GET"])
def ar11():
    card_info = get_card_info("ar11")
    return render_template("/ar11.html", card_info=card_info)

@app.route("/ar12",methods=["GET"])
def ar12():
    card_info = get_card_info("ar12")
    return render_template("/ar12.html", card_info=card_info)

@app.route("/ar13",methods=["GET"])
def ar13():
    card_info = get_card_info("ar13")
    return render_template("/ar13.html", card_info=card_info)

@app.route("/ar14",methods=["GET"])
def ar14():
    card_info = get_card_info("ar14")
    return render_template("/ar14.html", card_info=card_info)

@app.route("/ar15",methods=["GET"])
def ar15():
    card_info = get_card_info("ar15")
    return render_template("/ar15.html", card_info=card_info)

@app.route("/ar16",methods=["GET"])
def ar16():
    card_info = get_card_info("ar16")
    return render_template("/ar16.html", card_info=card_info)

@app.route("/ar17",methods=["GET"])
def ar17():
    card_info = get_card_info("ar17")
    return render_template("/ar17.html", card_info=card_info)

@app.route("/ar18",methods=["GET"])
def ar18():
    card_info = get_card_info("ar18")
    return render_template("/ar18.html", card_info=card_info)

@app.route("/ar19",methods=["GET"])
def ar19():
    card_info = get_card_info("ar19")
    return render_template("/ar19.html", card_info=card_info)

@app.route("/ar20",methods=["GET"])
def ar20():
    card_info = get_card_info("ar20")
    return render_template("/ar20.html", card_info=card_info)

@app.route("/ar21",methods=["GET"])
def ar21():
    card_info = get_card_info("ar21")
    return render_template("/ar21.html", card_info=card_info)

@app.route("/cuac",methods=["GET"])
def cuac():
    card_info = get_card_info("cuac")
    return render_template("/cuac.html", card_info=card_info)

@app.route("/cu02",methods=["GET"])
def cu02():
    card_info = get_card_info("cu02")
    return render_template("/cu02.html", card_info=card_info)

@app.route("/cu03",methods=["GET"])
def cu03():
    card_info = get_card_info("cu03")
    return render_template("/cu03.html", card_info=card_info)

@app.route("/cu04",methods=["GET"])
def cu04():
    card_info = get_card_info("cu04")
    return render_template("/cu04.html", card_info=card_info)

@app.route("/cu05",methods=["GET"])
def cu05():
    card_info = get_card_info("cu05")
    return render_template("/cu05.html", card_info=card_info)

@app.route("/cu06",methods=["GET"])
def cu06():
    card_info = get_card_info("cu06")
    return render_template("/cu06.html", card_info=card_info)

@app.route("/cu07",methods=["GET"])
def cu07():
    card_info = get_card_info("cu07")
    return render_template("/cu07.html", card_info=card_info)

@app.route("/cu08",methods=["GET"])
def cu08():
    card_info = get_card_info("cu08")
    return render_template("/cu08.html", card_info=card_info)

@app.route("/cu09",methods=["GET"])
def cu09():
    card_info = get_card_info("cu09")
    return render_template("/cu09.html", card_info=card_info)

@app.route("/cu10",methods=["GET"])
def cu10():
    card_info = get_card_info("cu10")
    return render_template("/cu10.html", card_info=card_info)

@app.route("/cupa",methods=["GET"])
def cupa():
    card_info = get_card_info("cupa")
    return render_template("/cupa.html", card_info=card_info)

@app.route("/cukn",methods=["GET"])
def cukn():
    card_info = get_card_info("cukn")
    return render_template("/cukn.html", card_info=card_info)

@app.route("/cuqu",methods=["GET"])
def cuqu():
    card_info = get_card_info("cuqu")
    return render_template("/cuqu.html", card_info=card_info)

@app.route("/cuki",methods=["GET"])
def cuki():
    card_info = get_card_info("cuki")
    return render_template("/cuki.html", card_info=card_info)

@app.route("/peac",methods=["GET"])
def peac():
    card_info = get_card_info("peac")
    return render_template("/peac.html", card_info=card_info)

@app.route("/pe02",methods=["GET"])
def pe02():
    card_info = get_card_info("pe02")
    return render_template("/pe02.html", card_info=card_info)

@app.route("/pe03",methods=["GET"])
def pe03():
    card_info = get_card_info("pe03")
    return render_template("/pe03.html", card_info=card_info)

@app.route("/pe04",methods=["GET"])
def pe04():
    card_info = get_card_info("pe04")
    return render_template("/pe04.html", card_info=card_info)

@app.route("/pe05",methods=["GET"])
def pe05():
    card_info = get_card_info("pe05")
    return render_template("/pe05.html", card_info=card_info)

@app.route("/pe06",methods=["GET"])
def pe06():
    card_info = get_card_info("pe06")
    return render_template("/pe06.html", card_info=card_info)

@app.route("/pe07",methods=["GET"])
def pe07():
    card_info = get_card_info("pe07")
    return render_template("/pe07.html", card_info=card_info)

@app.route("/pe08",methods=["GET"])
def pe08():
    card_info = get_card_info("pe08")
    return render_template("/pe08.html", card_info=card_info)

@app.route("/pe09",methods=["GET"])
def pe09():
    card_info = get_card_info("pe09")
    return render_template("/pe09.html", card_info=card_info)

@app.route("/pe10",methods=["GET"])
def pe10():
    card_info = get_card_info("pe10")
    return render_template("/pe10.html", card_info=card_info)

@app.route("/pepa",methods=["GET"])
def pepa():
    card_info = get_card_info("pepa")
    return render_template("/pepa.html", card_info=card_info)

@app.route("/pequ",methods=["GET"])
def pequ():
    card_info = get_card_info("pequ")
    return render_template("/pequ.html", card_info=card_info)

@app.route("/pekn",methods=["GET"])
def pekn():
    card_info = get_card_info("pekn")
    return render_template("/pekn.html", card_info=card_info)

@app.route("/peki",methods=["GET"])
def peki():
    card_info = get_card_info("peki")
    return render_template("/peki.html", card_info=card_info)

@app.route("/waac",methods=["GET"])
def waac():
    card_info = get_card_info("waac")
    return render_template("/waac.html", card_info=card_info)

@app.route("/wa02",methods=["GET"])
def wa02():
    card_info = get_card_info("wa02")
    return render_template("/wa02.html", card_info=card_info)

@app.route("/wa03",methods=["GET"])
def wa03():
    card_info = get_card_info("wa03")
    return render_template("/wa03.html", card_info=card_info)

@app.route("/wa04",methods=["GET"])
def wa04():
    card_info = get_card_info("wa04")
    return render_template("/wa04.html", card_info=card_info)

@app.route("/wa05",methods=["GET"])
def wa05():
    card_info = get_card_info("wa05")
    return render_template("/wa05.html", card_info=card_info)

@app.route("/wa06",methods=["GET"])
def wa06():
    card_info = get_card_info("wa06")
    return render_template("/wa06.html", card_info=card_info)

@app.route("/wa07",methods=["GET"])
def wa07():
    card_info = get_card_info("wa07")
    return render_template("/wa07.html", card_info=card_info)

@app.route("/wa08",methods=["GET"])
def wa08():
    card_info = get_card_info("wa08")
    return render_template("/wa08.html", card_info=card_info)

@app.route("/wa09",methods=["GET"])
def wa09():
    card_info = get_card_info("wa09")
    return render_template("/wa09.html", card_info=card_info)

@app.route("/wa10",methods=["GET"])
def wa10():
    card_info = get_card_info("wa10")
    return render_template("/wa10.html", card_info=card_info)

@app.route("/wapa",methods=["GET"])
def wapa():
    card_info = get_card_info("wapa")
    return render_template("/wapa.html", card_info=card_info)

@app.route("/wakn",methods=["GET"])
def wakn():
    card_info = get_card_info("wakn")
    return render_template("/wakn.html", card_info=card_info)

@app.route("/waqu",methods=["GET"])
def waqu():
    card_info = get_card_info("waqu")
    return render_template("/waqu.html", card_info=card_info)

@app.route("/waki",methods=["GET"])
def waki():
    card_info = get_card_info("waki")
    return render_template("/waki.html", card_info=card_info)

@app.route("/swac",methods=["GET"])
def swac():
    card_info = get_card_info("swac")
    return render_template("/swac.html", card_info=card_info)

@app.route("/sw02",methods=["GET"])
def sw02():
    card_info = get_card_info("sw02")
    return render_template("/sw02.html", card_info=card_info)

@app.route("/sw03",methods=["GET"])
def sw03():
    card_info = get_card_info("sw03")
    return render_template("/sw03.html", card_info=card_info)

@app.route("/sw04",methods=["GET"])
def sw04():
    card_info = get_card_info("sw04")
    return render_template("/sw04.html", card_info=card_info)

@app.route("/sw05",methods=["GET"])
def sw05():
    card_info = get_card_info("sw05")
    return render_template("/sw05.html", card_info=card_info)

@app.route("/sw06",methods=["GET"])
def sw06():
    card_info = get_card_info("sw06")
    return render_template("/sw06.html", card_info=card_info)

@app.route("/sw07",methods=["GET"])
def sw07():
    card_info = get_card_info("sw07")
    return render_template("/sw07.html", card_info=card_info)

@app.route("/sw08",methods=["GET"])
def sw08():
    card_info = get_card_info("sw08")
    return render_template("/sw08.html", card_info=card_info)

@app.route("/sw09",methods=["GET"])
def sw09():
    card_info = get_card_info("sw09")
    return render_template("/sw09.html", card_info=card_info)

@app.route("/sw10",methods=["GET"])
def sw10():
    card_info = get_card_info("sw10")
    return render_template("/sw10.html", card_info=card_info)

@app.route("/swpa",methods=["GET"])
def swpa():
    card_info = get_card_info("swpa")
    return render_template("/swpa.html", card_info=card_info)

@app.route("/swkn",methods=["GET"])
def swkn():
    card_info = get_card_info("swkn")
    return render_template("/swkn.html", card_info=card_info)

@app.route("/swqu",methods=["GET"])
def swqu():
    card_info = get_card_info("swqu")
    return render_template("/swqu.html", card_info=card_info)

@app.route("/swki",methods=["GET"])
def swki():
    card_info = get_card_info("swki")
    return render_template("/swki.html", card_info=card_info)



if __name__ == "__main__":
    app.run(debug=True)