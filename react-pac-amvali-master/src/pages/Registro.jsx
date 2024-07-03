import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";
import HeaderLogin from "../components/HeaderLogin";
import FormsRegistro from "../components/FormsRegistro";
import HalfImage from "../components/HalfImage";

function Registro() {
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
    senha: "",
    entidade: "",
  }); // Assuming you'll collect form data

  const [csrfToken, setCsrfToken] = useState("");

  useEffect(() => {
    fetchCsrfToken();
  }, []);

  const fetchCsrfToken = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/csrf/', {
        credentials: 'include' // Garante que os cookies, incluindo o CSRF token, são enviados
      });
      if (response.ok) {
        const data = await response.json();
        setCsrfToken(data.csrfToken);
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
    e.preventDefault(); // Prevenir comportamento padrão de envio do formulário
    try {
      const response = await fetch('http://localhost:8000/login/api-register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken // Inclui o CSRF token no cabeçalho da requisição
        },
        body: JSON.stringify(formData),
        credentials: 'include' // Garante que os cookies, incluindo o CSRF token, são enviados
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log('Registro realizado com sucesso:', data.message);
        // Redirecionar para a página de login ou fazer outra ação após o registro bem-sucedido
      } else {
        const errorData = await response.json(); // Captura o corpo da resposta de erro
        console.error('Falha no registro:', errorData.errors);
        // Lógica para lidar com erros, como exibir mensagens de erro para o usuário
      }
    } catch (error) {
      console.error('Erro durante a requisição:', error);
      // Lógica para lidar com erros de rede ou outros erros não esperados
    }
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