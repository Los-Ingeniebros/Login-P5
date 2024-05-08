function Usuario (props) {
    return (
        <div>
            <p>Nombre: {props.name.nombre}</p>
            <p>Contraseña: {props.name.contrasenia}</p>
        </div>
    );
}

export default Usuario;