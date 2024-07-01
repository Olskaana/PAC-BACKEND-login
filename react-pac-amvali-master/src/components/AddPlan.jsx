import React, { useState } from "react";

function AddPlan() {
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
    <div className="container">
      {inputFields.map((inputField) => (
        <div className="input-container" key={inputField.id}>
          <input
            type="text"
            className="tab-plan-title"
            placeholder="Insira o subtítulo..."
          />
          <textarea
            placeholder="Insira o texto..."
            className="tab-plan"
            value={inputField.value}
            onChange={(e) => handleValueChange(inputField.id, e)}
          />
          <button
            type="button"
            className="delete-btn"
            onClick={() => handleRemoveFields(inputField.id)}
          >
            <span className="material-symbols-outlined">delete</span>
          </button>
        </div>
      ))}
      <div className="display-button">
        <button type="button" className="add-btn" onClick={handleAddFields}>
          <span class="material-symbols-outlined">description</span>ADICIONAR
          TEXTO
        </button>
      </div>
    </div>
  );
}

export default AddPlan;
