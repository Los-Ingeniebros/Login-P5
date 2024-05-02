import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import Name from './Name';
import LogInForm from './Login';
import Usuario from './Usuario';
//import NewNameForm from './NewNameForm';

function App() {

  const [name, setName] = useState({
    name:undefined,
    contrasenia:undefined
  });

  function fetchNameHandler() {
    fetch('http://127.0.0.1:5000/login')
    .then((response) => {
      return response.json(); //Si aquí hay un error, quiere decir que el back-end está mal.
    })
    .then((data) => { //Lambda en JS
      setName(data);
    })
  }

  const cambiarVentana = () => {
    const contenidoNuevaVentana = (
      <div>
        <Usuario name={name} />       
      </div>
    )
  };

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

      const nuevaVentana = window.open('', '_self');

      //ReactDOM.render(cambiarVentana.contenidoNuevaVentana, nuevaVentana.document.body);
      //const root = ReactDOM.createRoot(nuevaVentana.document.body);
      //root.render(cambiarVentana.contenidoNuevaVentana)

      const contenedor = nuevaVentana.document.createElement('div');
      nuevaVentana.document.body.appendChild(contenedor);
      const root = ReactDOM.createRoot(contenedor);
      root.render(cambiarVentana.contenidoNuevaVentana);
      setName(name);
    }
  }

  // <Name name={name} />
  // <button onClick={fetchNameHandler}>New Name</button>
  return (
    <div className="App">
      <header className="App-header">           
        <LogInForm onSaveName={ingresar}/>
        {/* <Usuario name={name} />               */}
        <div>--- Hola ---</div>
      </header>
    </div>
  );
}

export default App;
