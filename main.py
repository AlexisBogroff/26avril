def salutations():
    return "coucou"

def salutations_personalise(prenom):
    return f"Coucou {prenom}"

def salutations_personalise_default(prenom, nom='piu'):
    return f"Coucou {prenom} {nom}"


message = salutations()
print(message)

message = salutations_personalise("alexis")
print(message)
