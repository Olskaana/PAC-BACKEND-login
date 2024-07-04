import React, { useState } from "react";
import DropdownAction from "./DropdownAction";

function AddActions() {
  const [selectedValue, setSelectedValue] = useState("");
  const [inputFields, setInputFields] = useState([
    { id: Math.random(), value: "" },
  ]);

  const handleAddFields = () => {
    setInputFields([...inputFields, { id: Math.random(), value: "" }]);
  };

  const handleRemoveFields = (id) => {
    const values = [...inputFields];
    const newValues = values.filter((value) => value.id !== id);
    setInputFields(newValues);
  };

  const handleValueChange = (id, event) => {
    const newInputFields = [...inputFields];
    const index = newInputFields.findIndex((x) => x.id === id);
    newInputFields[index].value = event.target.value;
    setInputFields(newInputFields);
  };

  return (
    <div className="container-action">
      <h1>{(selectedValue || "Ação").toUpperCase()}</h1>
      <DropdownAction onValueChange={setSelectedValue} />
      {inputFields.map((inputField) => (
        <div className="input-container" key={inputField.id}>
          <input
            type="text"
            placeholder={`Insira a ${selectedValue || "Ação"}...`}
            className="tab-plan-title"
          />
          <textarea
            placeholder={`Descrição/Detalhe da ${selectedValue || "Ação"}...`}
            className="tab-plan"
            value={inputField.value}
            onChange={(e) => handleValueChange(inputField.id, e)}
          />
          <div className="tab-principals-action">
            <div>
              <p>Início do Prazo</p>
              <input type="date" className="date" />
            </div>
            <div>
              <p>Término do Prazo</p>
              <input type="date" className="date" />
            </div>
          </div>
          <button
            type="button"
            className="delete-btn"
            onClick={() => handleRemoveFields(inputField.id)}
          >
            <span className="material-symbols-outlined">delete</span>
          </button>
        </div>
      ))}
      <button type="button" className="add-btn" onClick={handleAddFields}>
        <span class="material-symbols-outlined">description</span>ADICIONAR{" "}
        {(selectedValue || "Ação").toUpperCase()}
      </button>
    </div>
  );
}

export default AddActions;
