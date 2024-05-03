import React, { useState } from 'react';
// import ReactDOM from 'react-dom/client';
import './App.css';
// import Name from './Name';
import LogInForm from './Login';
// import Usuario from './Usuario';
//import NewNameForm from './NewNameForm';

function App() {

  async function ingresar (name) {
    console.log(name);
    const response = await fetch('http://127.0.0.1:5000/login', {
      method:'POST',
      body: JSON.stringify(name),
      headers: {
        'Content-Type':'application/json'
      }
    });
    const data = await response.json();
    console.log(data);
    if (data.error !== undefined) {
      alert("ERROR! " + data.error);
    } else {
      alert("Usuario encontrado!");
    }
  }

  // <Name name={name} />
  // <button onClick={fetchNameHandler}>New Name</button>
  return (
    <div className="App">
      <header className="App-header"> 
        <h1>MerkApp</h1>
        <p>Inicio de sesión:</p>    
        <LogInForm onSaveName={ingresar}/>
        {/* <Usuario name={name} />               */}
        <div>--- Hola ---</div>
      </header>
    </div>
  );
}

export default App;
