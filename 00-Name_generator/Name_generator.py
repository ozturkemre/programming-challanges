def name_generator():
    import random
    name=["William","John","Eren","Joseph","Lucas"]
    lastname=["Jones","Jeager","Joseph","Ospina","Carlos"]
    random_name=random.randrange(0,len(name))
    random_lastname=random.randrange(0,len(lastname))
    full=name[random_name]+" "+lastname[random_lastname]
    print(full)

name_generator()