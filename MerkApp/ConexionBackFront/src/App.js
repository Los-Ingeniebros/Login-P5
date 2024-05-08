import React, { useState } from 'react';
import './App.css';
import LogInForm from './Login';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './Home';
import { useNavigate } from 'react-router-dom';

function App() {

  const [user, setUser] = useState('');
  const navigate = useNavigate();

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
      console.log(name['nombre'])
      setUser(name['nombre']); 
      navigate('/home');
    }      
  };

  return (
    <div className="App">
      <header className="App-header">  
        <h1>MerkApp</h1>                 
        <Routes>
          <Route path="/" element={<LogInForm onSaveName={ingresar}/>} />  
          <Route path="/home" element={Home(user)} />  
        </Routes>        
      </header>      
    </div>
  );
}

export default App;
