import React, { useState } from "react";
import view_eye from "./assets/view.png";
import hide_eye from "./assets/hide.png";

function FormsRegistro({ setFormData }) {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [entidade, setEntidade] = useState('');
  const [email, setEmail] = useState('');

  const handleEntidadeChange = (e) => {
    setEntidade(e.target.value);
    setFormData(prevData => ({ ...prevData, entidade: e.target.value }));
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    setFormData(prevData => ({ ...prevData, email: e.target.value }));
  };

  const handlePasswordChange = (e) => {
    setFormData(prevData => ({ ...prevData, senha: e.target.value }));
  };

  const handleConfirmPasswordChange = (e) => {
    setFormData(prevData => ({ ...prevData, confirmar_senha: e.target.value }));
  };

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleToggleConfirmPassword = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };

  return (
    <form className="form" action="POST">
      <label>
        <input 
          className="input"
          type="text"
          placeholder=""
          value={entidade}
          onChange={handleEntidadeChange}
        />
        <span>Entidade...</span>
      </label>

      <label>
        <input 
          className="input" 
          type="email"
          placeholder=""
          value={email}
          onChange={handleEmailChange}
        />
        <span>E-Mail...</span>
      </label>

      <label className="password-label">
        <input
          className="input"
          type={showPassword ? "text" : "password"}
          placeholder=""
          required
          id="senha"
          onChange={handlePasswordChange}
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

      <label className="password-label">
        <input
          className="input"
          type={showConfirmPassword ? "text" : "password"}
          placeholder=""
          required
          id="confirmar_senha"
          onChange={handleConfirmPasswordChange}
        />
        <span>Confirmar Senha...</span>
        <img
          src={showConfirmPassword ? view_eye : hide_eye}
          alt="Esconder Senha"
          id="toggleConfirmPassword"
          style={{ width: "30px", cursor: "pointer" }}
          onClick={handleToggleConfirmPassword}
        />
      </label>
    </form>
  );
}

export default FormsRegistro;
