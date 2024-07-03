import React from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";
import HeaderLogin from "../components/HeaderLogin";
import FormsLogin from "../components/FormsLogin";
import HalfImage from "../components/HalfImage";

function Login() {
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
            <FormsLogin />
            <div className="submit">
              <div className="enter-button">
                <button>ENTRAR</button>
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
    </div>
  );
}

export default Login;
