import Player from "./Player.js";

// Créer une classe Guerrière (Warrior) qui hérite de player
// Créer une méthode kick() qui affiche "Ouïlle!" dans la console

export default class Warrior extends Player {
    constructor(hearts,name) {
        super(hearts,name);
    }
    
    kick() {
        console.log(`${this.pseudo} tabasse, et l'ennemi crie Ouïlle!`);
    }
}