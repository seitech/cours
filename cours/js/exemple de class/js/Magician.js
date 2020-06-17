import Player from "./Player.js";

// Créer une classe Magician qui hérite de player
// Créer une méthode spell() qui affiche "Foudre!" dans la console

class Magician extends Player {
    constructor(hearts,name) {
        super(hearts,name);
    }

    spell() {
        console.log(`Foudre! Mais ça aide qu'il y ait déjà
        de l'orage`);
    }
}