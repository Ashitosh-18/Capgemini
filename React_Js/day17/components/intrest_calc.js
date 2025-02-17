import React, { useState } from 'react';

function InterestCalculator() {
  // State declarations for principle, rate, time, interest type, and result
  const [principle, setPrinciple] = useState('');
  const [rate, setRate] = useState('');
  const [time, setTime] = useState('');
  const [type, setType] = useState('simple'); // Default interest type is simple
  const [result, setResult] = useState(null);

  // Function to handle the interest calculation
  const calculateInterest = () => {
    let P = parseFloat(principle); // Principle amount (converted to number)
    let R = parseFloat(rate); // Rate (converted to number)
    let T = parseFloat(time); // Time (converted to number)

    // Validation to ensure all inputs are filled
    if (!P || !R || !T) {
      alert("Please provide all required values (Principle, Rate, Time).");
      return;
    }

    let interest;
    if (type === 'simple') {
      // Simple Interest Formula: SI = (P * R * T) / 100
      interest = (P * R * T) / 100;
    } else {
      // Compound Interest Formula: CI = P * (1 + R/100)^T - P
      interest = P * Math.pow(1 + R / 100, T) - P;
    }

    // Set the result after calculation
    setResult(interest);
  };

  // Return JSX to render the component
  return (
    <div>
      <h2>Interest Calculator</h2>

      {/* Input fields for principle, rate, and time */}
      <div>
        <label>Principle (P): </label>
        <input
          type="number"
          value={principle}
          onChange={(e) => setPrinciple(e.target.value)}
          style={styles.input}
          placeholder="Enter principal amount"
        />
      </div>
      <div>
        <label>Rate (R): </label>
        <input
          type="number"
          value={rate}
          onChange={(e) => setRate(e.target.value)}
          style={styles.input}
          placeholder="Enter interest rate"
        />
      </div>
      <div>
        <label>Time (T): </label>
        <input
          type="number"
          value={time}
          onChange={(e) => setTime(e.target.value)}
          style={styles.input}
          placeholder="Enter time (in years)"
        />
      </div>

      {/* Dropdown to choose interest type */}
      <div>
        <label>Interest Type: </label>
        <select value={type} onChange={(e) => setType(e.target.value)} style={styles.input}>
          <option value="simple">Simple Interest</option>
          <option value="compound">Compound Interest</option>
        </select>
      </div>

      {/* Button to calculate interest */}
      <div>
        <button onClick={calculateInterest} style={styles.button}>Calculate</button>
      </div>

      {/* Display the result */}
      {result !== null && (
        <div>
          <h3>Calculated Interest: {result}</h3>
        </div>
      )}
    </div>
  );
}

// Inline styles
const styles = {
  input: {
    margin: '10px',
    padding: '8px',
    fontSize: '16px',
  },
  button: {
    padding: '10px 20px',
    backgroundColor: '#333',
    color: 'white',
    border: 'none',
    cursor: 'pointer',
  },
};

export default InterestCalculator;
