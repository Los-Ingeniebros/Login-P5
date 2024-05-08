import React, { useState } from "react";


function LogInForm (props) {
    const [enteredNombre, setNombre] = useState('');
    const [enteredContrasenia, setContrasenia] = useState('');

    const nombreChangeHandler = (event) => {
        setNombre(event.target.value);
    }

    const contraseniaChangeHandler = (event) => {
        setContrasenia(event.target.value);
    }    

    const submitHandler = (event) => {
        event.preventDefault();

        const user = {
            nombre:enteredNombre,
            contrasenia:enteredContrasenia
        }
        props.onSaveName(user);
        setNombre('');
        setContrasenia('');
    }

    return (                
        <form onSubmit={submitHandler}>                            
            <p>Inicio de sesión</p>    
            <div>
            <label>Nombre: </label>
                <input 
                    id="username"
                    name="username"
                    type='text'
                    value={enteredNombre}
                    onChange={nombreChangeHandler}
                />
            </div>
            <div>
                <label>Contraseña: </label>
                <input
                    id="password"
                    name="password"
                    type='password'
                    value={enteredContrasenia}
                    onChange={contraseniaChangeHandler}
                />
            </div>       
            <button type="submit">Iniciar sesión</button>
        </form>
    );
};

export default LogInForm;