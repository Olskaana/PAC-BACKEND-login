import React from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import FooterBlack from "../components/FooterBlack";
import HeaderBlack from "../components/HeaderBlack";
import Card from "../components/Card";

export function Itaperiu() {
  return (
    <div className="main-page-city">
      <Helmet bodyAttributes={{ style: "background-color: #F8F8F8;" }} />
      <HeaderBlack />
      <div className="return">
        <Link to="/">
          <p>← VOLTAR</p>
        </Link>
      </div>
      <div className="title">
        <h1>ESCOLHA UM PLANO PARA CONTINUAR</h1>
      </div>
      <div className="card-area">
        <Card />
        <Card />
      </div>
      <div className="create">
        <Link to="./criar-plano">
          <p>CRIAR PLANO →</p>
        </Link>
      </div>
      <FooterBlack />
    </div>
  );
}
