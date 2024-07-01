import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";
import HeaderLogin from "../components/HeaderLogin";
import FormsRegistro from "../components/FormsRegistro";
import HalfImage from "../components/HalfImage";
import CryptoJS from 'crypto-js';

function Registro() {
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
    senha: "",
    confirmar_senha: "",
    entidade: "",
  });

  useEffect(() => {
    fetchCsrfToken();
  }, []);

  const fetchCsrfToken = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/csrf/', {
        credentials: 'include'
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Registro realizado com sucesso:', data);
      } else {
        console.error('Falha ao obter CSRF token');
      }
    } catch (error) {
      console.error('Erro durante a requisição CSRF:', error);
    }
  };

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const hashedPassword = CryptoJS.SHA256(formData.senha).toString(CryptoJS.enc.Hex);
    try {
      const response = await fetch('http://127.0.0.1:8000/api/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          senha: hashedPassword,
          entidade: formData.entidade,
        }),
        credentials: 'include'
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Registro realizado com sucesso:', data);
        window.location.href = '/';
      } else {
        const errorData = await response.json();
        console.error('Falha no registro:', errorData);
      }
    } catch (error) {
      console.error('Erro durante a requisição CSRF:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  return (
    <div className="main-login">
      <Helmet bodyAttributes={{ style: "background-color : #F8C401" }} />
      <HeaderLogin />
      <div className="card-principal-login">
        <div id="card" className="card-login">
          <div className="half1">
            <div className="title-login">
              <h1>CADASTRE-SE COM A PERMISSÃO DA AMVALI</h1>
            </div>
            <FormsRegistro
              showPassword={showPassword}
              handleTogglePassword={handleTogglePassword}
              handleChange={handleChange}
              formData={formData}
              setFormData={setFormData}
            />
            <div className="submit">
              <div className="enter-button">
                <button onClick={handleSubmit}>CADASTRAR-SE</button>
              </div>
              <div className="forgot-pass">
                <p id="account">
                  Já possui uma conta? <Link to="../Login">Entre agora.</Link>
                </p>
              </div>
            </div>
          </div>
          <HalfImage />
        </div>
      </div>
    </div>
  );
}

export default Registro;
