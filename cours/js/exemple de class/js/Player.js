
// Créer une classe Player
// Cette classe a une propriété nbLifes que l'utilisateur peut préciser
// Et une propriété pseudo
// Ajouter une méthode hello à cette classe, et qui affiche
// "Bonjour, je suis pseudo et j'ai x vies"


export default class Player {
    constructor(hearts, name) {
        this.nbLifes = hearts;
        this.pseudo = name;
    }

    hello() {
        alert(`Booonjour, moi c'est ${this.pseudo} et j'ai ${this.nbLifes} vies`);
    }
}