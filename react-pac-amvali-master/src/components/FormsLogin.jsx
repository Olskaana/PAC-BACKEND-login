import React, { useState } from "react";
import view_eye from "./assets/view.png";
import hide_eye from "./assets/hide.png";

function FormsLogin({ handleChange, formData }) {
  const [showPassword, setShowPassword] = useState(false);

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  return (
    <form className="form">
      <label>
        <input
          className="input"
          type="email"
          placeholder=""
          required
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        <span>E-Mail...</span>
      </label>

      <label>
        <input
          className="input"
          type="text"
          placeholder=""
          required
          name="entidade"
          value={formData.entidade}
          onChange={handleChange}
        />
        <span>Entidade...</span>
      </label>

      <label className="password-label">
        <input
          className="input"
          type={showPassword ? "text" : "password"}
          placeholder=""
          required
          name="senha"
          value={formData.senha}
          onChange={handleChange}
        />
        <span>Senha...</span>
        <img
          src={showPassword ? view_eye : hide_eye}
          alt="Esconder Senha"
          id="togglePassword"
          style={{ width: "30px", cursor: "pointer" }}
          onClick={handleTogglePassword}
        />
      </label>
    </form>
  );
}

export default FormsLogin;
