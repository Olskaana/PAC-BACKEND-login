import React from "react";
import { Link } from "react-router-dom";
import { Helmet } from "react-helmet";
import HeaderLogin from "../components/HeaderLogin";

function Info() {
  return (
    <div className="main-info">
      <Helmet bodyAttributes={{ style: "background-color: #F8C401;" }} />
      <HeaderLogin />
      <div className="card-info">
        <div id="card" className="primary-card-info">
          <div className="text-info">
            <h3>Por que criar uma conta?</h3>
            <p>
              A criação de contas serve para a inserção dos
              <strong> PLANOS </strong> que, assim que inseridos, passarão pela
              <strong> APROVAÇÃO </strong> da Amvali e, em seguida, publicados
              ao site.
            </p>
          </div>
          <div className="text-info">
            <h3>Consigo visualizar tudo sem uma conta?</h3>
            <p>
              Sim! Tudo que disponibilizamos é de
              <strong> DOMÍNIO PÚBLICO </strong> e compartilhado para toda a
              população, temos como objetivo <strong>TRANSPARECER </strong>, de
              forma simples, intuitiva e criativa, os <strong>PLANOS </strong>
              criados por <strong>TODOS </strong>
              os municípios do Vale do Itapocu.
            </p>
          </div>
          <div className="submit-info">
            <h3>Ainda precisa de uma conta?</h3>
            <Link to="../registro">
              <button>CADASTRE-SE</button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Info;
