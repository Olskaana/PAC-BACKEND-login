import React, { useRef, useState } from "react";

const FileInput = () => {
  const [file, setFile] = useState();

  const inputRef = useRef();

  const [selectedFile, setSelectedFile] = useState(null);

  // Handle the change event when a file is selected
  const handleOnChange = (event) => {
    console.log(event.target.files);
    if (event.target.files && event.target.files.length > 0) {
      const selectedFile = event.target.files[0];
      const fileSizeInMB = selectedFile.size / (1024 * 1024);
      const limitInMB = 10;
  
      if (fileSizeInMB > limitInMB) {
        alert('File size exceeds 10MB limit');
      } else {
        setFile(selectedFile); // Store the File object in state
        setSelectedFile(selectedFile);
      }
    }
  };

  const onChooseFile = () => {
    inputRef.current.click();
  };

  const removeFile = () => {
    setSelectedFile(null);
    setFile(null); // Reset the file state variable
  };

  return (
    <div>
      <div className="image-visualizer">
        <input
          className="file-input"
          type="file"
          ref={inputRef}
          onChange={handleOnChange}
          style={{ display: "none" }}
        />
        {file ? (
          file.type === "application/pdf" ? (
            <object
              data={URL.createObjectURL(file)}
              width="1000"
              height="600"
              aria-label="PDF preview"
            />
          ) : (
            <img src={URL.createObjectURL(file)} alt="" width="800px" />
          )
        ) : null}
      </div>
      <button type="button" className="file-btn" onClick={onChooseFile}>
        <span class="material-symbols-outlined">upload</span> Inserir Arquivo
      </button>

      {selectedFile && (
        <div className="selected-file">
          <p>{selectedFile.name}</p>

          <button type="button" onClick={removeFile}>
            <span className="material-symbols-outlined">delete</span>
          </button>
        </div>
      )}
    </div>
  );
};

export default FileInput;
