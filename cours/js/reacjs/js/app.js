// EXO1. Créer un bouton "compteur"
// Ce bouton affichera le nombre de clics dessus

// ex:
// Cliqué 0 fois
// puis après clic: "Cliqué 1 fois, Cliqué 2 fois, etc..."

/*
class App extends React.Component {
    state={
        number: 0
    }

    click = e => {
        this.setState({
            number: this.state.number+1
        })
    }

    render() {
        return(
            <div>
                <button onClick={this.click}>
                    nombre de fois cliqué :{this.state.number}
                </button>
            </div>

        );
        
    }
}

ReactDOM.render(<App/>,document.getElementById("app"));

*/
// Exo2. Créer un formulaire, avec un champ nom/prénom/age
// Au clic du bouton Envoyer, afficher dans la console le contenu 
// tapé par l'utilisateur

// Doit afficher quelque chose du style
// { firstname: "Jean-Baptiste", lastname: "Lavisse", age: 29}
// Ajouter ce contenu dans une liste de formateurs hyper cools

class App extends React.Component {
    state = {
        firstname: "Jean-Baptiste",
        lastname: "Lavisse",
        age: 0
    }

    handleLastname = event => {
        this.setState({
            lastname: event.target.value
        })
    }

    handleFirstname = event => {
        this.setState({
            firstname: event.target.value
        })
    }

    handleAge = event => {
        this.setState({
            age: event.target.value
        })
    }

    handleSubmit = event => {
        event.preventDefault();
        console.log(this.state);
    }

    render() {
        return (
             <form onSubmit={this.handleSubmit}>
                 <label>
                    Nom
                    <input type="text" name="lastname" id="" 
                    placeholder="Entrez votre nom" 
                    value={this.state.lastname} 
                    onChange={this.handleLastname} />
                 </label>
                 <label>
                    Prénom
                    <input type="text" name="firstname" id="" 
                    placeholder="Entrez votre prénom" 
                    value={this.state.firstname}
                    onChange={this.handleFirstname}
                     />
                 </label>
                 <label>
                    Age
                    <input type="text" name="age" id="" 
                    placeholder="Entrez votre age" 
                    value={this.state.age} 
                    onChange={this.handleAge}/>
                 </label>
                 <input type="submit" value="Envoyer"/>
             </form>
        );
    }
}

ReactDOM.render(<App/>,document.getElementById("app"));