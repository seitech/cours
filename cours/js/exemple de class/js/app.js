import Player from "./Player.js";
import Warrior from "./Warrior.js";
import Magician from "./Magician.js";

let jb = new Player(3,"Kirikou");
jb.hello();


let crom = new Warrior(123, "Crom");
console.log(crom);
crom.hello();
crom.kick();


let merlin = new Magician(10000, "Merlin, fils d'un démon et d'une pucelle");
merlin.hello();
merlin.spell();

// Créer un fichier par classe, et les instancier 
// Dans le fichier app.js