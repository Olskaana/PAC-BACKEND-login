import React, { useState } from "react";

function DropdownAction({ onValueChange }) {
  const [selected, setSelected] = useState("");

  const handleChange = (event) => {
    setSelected(event.target.value);
    if (onValueChange) {
      onValueChange(event.target.value);
    }
  };

  return (
    <div>
      <p>Selecione a Categoria da sua Ação</p>
      <select className="dropdown" value={selected} onChange={handleChange}>
        <option value="Ação">Categoria da Ação...</option>
        <option value="Ação">Ação</option>
        <option value="Meta">Meta</option>
        <option value="Diretriz">Diretriz</option>
        <option value="Objetivo">Objetivo</option>
        <option value="Recomendação">Recomendação</option>
      </select>
    </div>
  );
}

export default DropdownAction;