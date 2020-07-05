import React, { Component } from 'react';
import axios from 'axios';

import "./WeatherSystem.css";

import Period from "./Period";

class WeatherSystem extends Component {
    state = {
        periods: [], 
        ville: 'Lens'
     }

    componentDidMount() {
        axios.get('https://api.openweathermap.org/data/2.5/forecast?q=' + this.state.ville +'&lang=fr&units=metric&appid=8c3a54c385c9c9d874d88f2cd6b3dda8')
        .then(res => {;
            this.setState({
                periods: res.data.list
            })
        })
    }
    
    handleSubmit = (event) => {
        event.preventDefault();
        axios.get('https://api.openweathermap.org/data/2.5/forecast?q=' + this.state.ville +'&lang=fr&units=metric&appid=8c3a54c385c9c9d874d88f2cd6b3dda8')
        .then(res => {;
            this.setState({
                periods: res.data.list
            })
        })
    }

    villeChange = (event) => {
        this.setState({ville: event.target.value})
        
    }

    render() { 
        
        

        let periodsList = this.state.periods.map(period => {
            return <Period period={period} />
        })

        return ( 
            <div className="weathersystem">
                <form onSubmit={this.handleSubmit}>
                    <input value={this.state.ville} onChange={this.villeChange} type="text" placeholder="ville"/>
                </form>
                <h1>{this.state.ville}</h1><br/>
                {periodsList}
            </div>
         );
    }
}
 
export default WeatherSystem;