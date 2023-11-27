
palavra1 = input()
palavra2 = input()
palavra3 = input()

tipos = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        },
    },
    "invertebrado": {
        "inseto": {
            "hematofogo": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofogo": "sanguessuga",
            "onivoro": "minhoca"
        },
    },
}
try:
    resultado = tipos[palavra1][palavra2][palavra3]
    print(resultado)
except KeyError:
    print("Tente novamente")
