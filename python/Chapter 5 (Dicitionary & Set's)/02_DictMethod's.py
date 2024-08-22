arks = {
   "omer": "60",
   "bujjbeen": "12",
   "majjbeen": "99"
}

print(arks.items()) # dict_items([('omer', '60'), ('bujjbeen', '12'), ('majjbeen', '99')])

lrks = {
    "House": "780,000,000",
    "QWERTY": "cva"
}

print(lrks.keys()) # dict_keys(['House', 'QWERTY'])



# This Is Most Usefull Method.{

urks = {
    "BachaBeen": "DarpookBeen",
    "PatliBeen": "Maaaw"
}

urks.update({"BachaBeen": "Hujjbeen"})

print(urks) # {'BachaBeen': 'Hujjbeen', 'PatliBeen': 'Maaaw'}


# }    




Turks = {
   "Turkey": "Ottoman Empire",
   "King": "Mehmed",
   "Now": "Bridge Of Europe"
}

print(Turks.get("King"))  # Mehmed


Bujjbeen_Soo_Rahi_Hau = {
    "Majjbeen": "Bujjbeen",
    "bujji": "mano || Gujjo"
}

print(Bujjbeen_Soo_Rahi_Hau.pop("Bujjbeen", "Darrbeen"))  # Darrbeen
