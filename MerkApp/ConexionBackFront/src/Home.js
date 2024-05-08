import React from "react";
import { useNavigate } from 'react-router-dom';

function Home(name){    
    const navigate = useNavigate();

    const submitHandler = (event) => {
        navigate('/');
    }

    return (
        <form onSubmit={submitHandler}>  
            <div> 
                Hola {name}
                <div>
                <button type="submit">Cerrar sesión</button>
                </div>
            </div>
        </form>);
};

export default Home;