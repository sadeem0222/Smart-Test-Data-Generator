import React, { useState } from "react";

function App() {

  const [fieldType, setFieldType] = useState("email");
  const [result, setResult] = useState([]);

  const generateData = async () => {

    const response = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        field_type: fieldType
      })
    });

    const data = await response.json();
    setResult(data.test_cases);
  };

  return (
    <div style={{ padding: "30px" }}>

      <h2>Smart Test Data Generator</h2>

      <select onChange={(e) => setFieldType(e.target.value)}>
        <option value="email">Email</option>
        <option value="password">Password</option>
      </select>

      <br /><br />

      <button onClick={generateData}>
        Generate Test Data
      </button>

      <h3>Results:</h3>

      <ul>
        {result.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

    </div>
  );
}

export default App;