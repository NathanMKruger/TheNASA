import React, { useState, useEffect } from 'react';
// Import react-circular-progressbar module and styles
import {
  CircularProgressbar,
  buildStyles
} from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import logo from './logo.svg';
import './App.css';

function App() {
  const [prediction, getPrediction] = useState(0);

  useEffect(() => {
    fetch('/predict').then(res => res.json()).then(data => {
      getPrediction(data.prediction);
    });
  }, []);


  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div class="form">
                <form action="http://localhost:5000/predict" method="get">
                    <input type="text" name="url"/>
                    <input type="submit" value="Submit"/>
                </form>
        </div>
        <p>The current time is {currentTime}.</p>
        <div style={{ padding: "40px 540px 540px 540px" }}>
          <CircularProgressbar
              value={prediction}
              text={`${prediction}%`}
              styles={buildStyles({
                // Rotation of path and trail, in number of turns (0-1)
                rotation: 0.25,
             
                // Whether to use rounded or flat corners on the ends - can use 'butt' or 'round'
                strokeLinecap: 'butt',
             
                // Text size
                textSize: '16px',
             
                // How long animation takes to go from one percentage to another, in seconds
                pathTransitionDuration: 0.5,
             
                // Can specify path transition in more detail, or remove it entirely
                // pathTransition: 'none',
             
                // Colors
                pathColor: `rgba(62, 152, 199, ${prediction / 100})`,
                trailColor: '#d6d6d6',
                backgroundColor: '#3e98c7',
              })}
          />
        </div>
      </header>
    </div>
  );
}

export default App;
