// StarTigo ShieldNet - Activación por nación
pragma solidity ^0.8.0;

contract DefensaPais {
    mapping(string => string) public niveles;

    function actualizarEstado(string memory pais, string memory nivel) public {
        niveles[pais] = nivel;
    }

    function verEstado(string memory pais) public view returns (string memory) {
        return niveles[pais];
    }
}
