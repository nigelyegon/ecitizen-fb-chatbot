import React, { useState, useEffect } from "react";  // Importing necessary hooks from React
import "./Card.css";  // Importing the CSS file for styling the Card component
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';  // Importing required modules from chart.js
import { Pie } from 'react-chartjs-2';  // Importing the Pie component from react-chartjs-2

// Registering chart elements and components for use
ChartJS.register(ArcElement, Tooltip, Legend);

const Card = ({ title, description, type }) => {  // Card component accepting title, description, and type as props
  const [count, setCount] = useState(0);  // State for the counter, initialized to 0
  const [chartData, setChartData] = useState({  // State for the chart data
    labels: ['Positive', 'Negative', 'Neutral'],  // Labels for the pie chart segments
    datasets: [{
      data: [33, 33, 34],  // Initial data for the pie chart
      backgroundColor: ['#36A2EB', '#FF6384', '#FFCE56']  // Colors for the pie chart segments
    }]
  });

  useEffect(() => {  // useEffect hook for handling side effects
    if (type === 'counter') {  // If the type prop is 'counter'
      const interval = setInterval(() => {  // Set up an interval to update the counter every 5 seconds
        setCount(prevCount => prevCount + Math.floor(Math.random() * 5));  // Increment counter by a random number between 0 and 4
      }, 5000);
      return () => clearInterval(interval);  // Clean up the interval on component unmount
    }

    if (type === 'chart') {  // If the type prop is 'chart'
      const interval = setInterval(() => {  // Set up an interval to update the chart data every 5 seconds
        setChartData(prevData => ({  // Update the chart data
          ...prevData,
          datasets: [{
            ...prevData.datasets[0],
            data: [
              Math.floor(Math.random() * 100),  // Generate random number for 'Positive'
              Math.floor(Math.random() * 100),  // Generate random number for 'Negative'
              Math.floor(Math.random() * 100)   // Generate random number for 'Neutral'
            ]
          }]
        }));
      }, 5000);
      return () => clearInterval(interval);  // Clean up the interval on component unmount
    }
  }, [type]);  // Dependency array for useEffect, runs when 'type' changes

  return (  // JSX to render the component
    <div className="card">  
      <h3>{title}</h3> 
      {type === 'counter' && <p>{count}</p>}  
      {type === 'chart' && <Pie data={chartData} />} 
      {!type && <p>{description}</p>} 
    </div>
  );
};

export default Card;  // Exporting the Card component as the default export
