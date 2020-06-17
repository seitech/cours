class Car {
    nbWheels = 4;

    constructor(model) {
        this.model = model;
    }

    klaxon() {
        alert(`Ma voiture ${this.model} fait Tututtttttttt`);
    }
}

class PetrolCar extends Car {
    constructor(model) {
        super(model);
    }

    refuel() {
        console.log("Je mets de l'essence");
    }
}


class ElectricCar extends Car {
    constructor(model) {
        super(model);
    }

    reload() {
        console.log("Je recharge ma voiture");
    }
}




let mad = new PetrolCar("Audi");
mad.klaxon();
console.log(mad.nbWheels);
mad.refuel();

let max = new ElectricCar("Tesla");
max.klaxon();
max.reload();