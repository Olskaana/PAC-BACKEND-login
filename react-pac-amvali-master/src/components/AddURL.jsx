import React, { useState } from "react";

const AddURL = () => {
  const [urlFields, setUrlFields] = useState([{ id: Math.random(), url: "" }]);

  const handleAddUrlFields = () => {
    setUrlFields([...urlFields, { id: Math.random(), url: "" }]);
  };

  const handleRemoveUrlFields = (id) => {
    const values = [...urlFields];
    const newValues = values.filter((value) => value.id !== id);
    setUrlFields(newValues);
  };

  const handleUrlChange = (id, event) => {
    const newUrlFields = [...urlFields];
    const index = newUrlFields.findIndex((x) => x.id === id);
    newUrlFields[index].url = event.target.value;
    setUrlFields(newUrlFields);
  };

  return (
    <div className="container-action">
      {urlFields.map((urlField) => (
        <div key={urlField.id}>
          <input
            type="url"
            className="tab-plan-url"
            placeholder="Inserir URL..."
            value={urlField.url}
            onChange={(e) => handleUrlChange(urlField.id, e)}
          />
          <button
            type="button"
            className="delete-btn-img"
            onClick={() => handleRemoveUrlFields(urlField.id)}
          >
            <span className="material-symbols-outlined">delete</span>
          </button>
        </div>
      ))}
      <button type="button" className="add-btn" onClick={handleAddUrlFields}>
        <span class="material-symbols-outlined">link</span>ADICIONAR URL
      </button>
    </div>
  );
};

export default AddURL;
