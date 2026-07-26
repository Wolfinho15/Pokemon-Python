type_effectiveness = {
    "Fogo": {
        "Planta": 2,
        "Água": 0.5,
        "Fogo": 0.5
    },

    "Água": {
        "Fogo": 2,
        "Planta": 0.5,
        "Água": 0.5
    },

    "Planta": {
        "Água": 2,
        "Fogo": 0.5,
        "Planta": 0.5
    },

    "Elétrico": {
        "Água": 2,
        "Elétrico": 0.5,
        "Fogo": 1
    },
    
    "Fantasma": {
        "Normal": 0,
        "Sombrio": 0.5
    }
}



vantagens = {
    "Fogo":type_effectiveness["Fogo"],
    "Planta":type_effectiveness["Planta"],
    "Água":type_effectiveness["Água"]
}

print(vantagens["Água"]["Água"])