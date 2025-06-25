pragma solidity ^0.8.0;

contract DefensaCriptoIA {
    address propietario;
    bool publico;

    constructor() {
        propietario = msg.sender;
        publico = false;
    }

    function alertaFraude() public {
        require(msg.sender != propietario, "🛡️ No autorizado");
        publico = true; // Cambia estado de seguridad
    }

    function estadoActual() public view returns (bool) {
        return publico;
    }
}
