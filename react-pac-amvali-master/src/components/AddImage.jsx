import React, { useState } from "react";
import FileInput from "./FileInput";

function AddImage() {
  const [inputFields, setInputFields] = useState([
    { id: Math.random(), value: null },
  ]);

  const handleAddFields = () => {
    setInputFields([...inputFields, { id: Math.random(), value: null }]);
  };

  const handleRemoveFields = (id) => {
    const values = [...inputFields];
    const newValues = values.filter((value) => value.id !== id);
    setInputFields(newValues);
  };

  const handleValueChange = (id, event) => {
    const newInputFields = [...inputFields];
    const index = newInputFields.findIndex((x) => x.id === id);
    newInputFields[index].value = URL.createObjectURL(event.target.files[0]);
    setInputFields(newInputFields);
  };

  return (
    <div className="container">
      {inputFields.map((inputField) => (
        <div className="input-container" key={inputField.id}>
          <FileInput />
          {inputField.value && <img src={inputField.value} alt="preview" />}
          <button
            type="button"
            className="delete-btn-img"
            onClick={() => handleRemoveFields(inputField.id)}
          >
            <span className="material-symbols-outlined">delete</span>
          </button>
        </div>
      ))}
      <div className="display-button">
      <button type="button" className="add-btn-img" onClick={handleAddFields}>
        <span className="material-symbols-outlined">upload_file</span>
        ADICIONAR IMAGEM
      </button>
      </div>
    </div>
  );
}

export default AddImage;
