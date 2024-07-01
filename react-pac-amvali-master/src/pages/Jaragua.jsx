//import React from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import FooterBlack from "../components/FooterBlack";
import HeaderBlack from "../components/HeaderBlack";
import Card from "../components/Card";
import axios from 'axios';
import React, { useState, useEffect } from 'react';


export function Jaragua() {

  const [jg, setJg] = useState([]);

  const GetJaragua = () => {
      axios.get('http://127.0.0.1:8000/jaragua/')
        .then((res) => {
          setJg(res.data);
        })
  }

  useEffect(() => {
    GetJaragua();
  })

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
        <Card maxDescriptionLength={200} />
        <Card maxDescriptionLength={200} />
        <Card maxDescriptionLength={200} />
        <Card maxDescriptionLength={200} />
        <Card maxDescriptionLength={200} />
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
