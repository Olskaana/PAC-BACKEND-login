import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";
import HeaderLogin from "../components/HeaderLogin";
import FormsLogin from "../components/FormsLogin";
import HalfImage from "../components/HalfImage";
import CryptoJS from 'crypto-js';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function Login() {
  const [formData, setFormData] = useState({
    email: "",
    senha: "",
    entidade: ""
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
        console.log('CSRF token obtido com sucesso:', data);
      } else {
        console.error('Falha ao obter CSRF token');
      }
    } catch (error) {
      console.error('Erro durante a requisição CSRF:', error);
    }
  };

  const handleLogin = async () => {
    const hashedPassword = CryptoJS.SHA256(formData.senha).toString(CryptoJS.enc.Hex);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email: formData.email,
          senha: hashedPassword,
          entidade: formData.entidade
        }),
        credentials: "include"
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Login successful:", data);
        toast.success("Usuário logado com sucesso!");
        setTimeout(() => {
          window.location.href = "/";
        }, 2000);
      } else {
        const errorData = await response.json();
        console.error("Falha no login:", errorData);
        toast.error("Falha no login! Verifique suas credenciais."); // Mostrar notificação de erro
      }
    } catch (error) {
      console.error("Erro durante a requisição:", error);
      toast.error("Erro durante a requisição!"); // Mostrar notificação de erro
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value
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
              <h1>BEM-VINDO DE VOLTA!</h1>
            </div>
            <FormsLogin handleChange={handleChange} formData={formData} />
            <div className="submit">
              <div className="enter-button">
                <button onClick={handleLogin}>ENTRAR</button>
              </div>
              <div className="forgot-pass">
                <Link to="">
                  <p>Esqueceu sua senha?</p>
                </Link>
                <p id="account">
                  Não possui uma conta?
                  <Link to="./info"> Leia os requisitos e cadastre-se.</Link>
                </p>
              </div>
            </div>
          </div>
          <HalfImage />
        </div>
      </div>
      <ToastContainer />
    </div>
  );
}

export default Login;
