import { useState } from "react";


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
            <div>
                <label>Name: </label>
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
                    type='text'
                    value={enteredContrasenia}
                    onChange={contraseniaChangeHandler}
                />
            </div>
            <div>
                <button type="submit">Log in</button>
            </div>
        </form>
    )
}

export default LogInForm;