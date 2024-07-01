import React, { useState } from "react";
import { Helmet } from "react-helmet";
import axios from "axios";
import AddPlan from "./AddPlan.jsx";
import AddImage from "./AddImage.jsx";
import Dropdown from "./Dropdown.jsx";
import AddActions from "./AddActions.jsx";
import AddURL from "./AddURL.jsx";

function Tabs({ municipio }) {
  const [estadoDaApp, setEstadoDaApp] = useState({
    nome: "",
    inicio_prazo: "",
    final_prazo: "",
    introducao: "",
    categoria: ""
  });
  const handleEstados = (evento) =>{
    const {value, name} = evento.target
    setEstadoDaApp({...estadoDaApp, [name]: value})
  }


  const handleCriarPlano = async (e) => {
    e.preventDefault();
    municipio = "schroeder";
    try {
      await fetchCsrfToken();
      debugger
      const response = await axios.post(
        `http://127.0.0.1:8000/api/${municipio}/criar-plano/`,
        estadoDaApp,
        {
          withCredentials: true,
        }
      );

      if (response.status === 200) {
        console.log("Plano criado com sucesso:", response.data);
        
      } else {
        console.error("Falha na criação do plano:", response.data);
        
      }
    } catch (error) {
      console.error("Erro durante a requisição:", error);
      
    }
  };

  const fetchCsrfToken = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/csrf/", {
        withCredentials: true,
      });
      if (response.status === 200) {
        console.log("CSRF token obtido com sucesso:", response.data);
        return response.data;
      } else {
        console.error("Falha ao obter CSRF token");
      }
    } catch (error) {
      console.error("Erro durante a requisição CSRF:", error);
      throw error;
    }
  };

  return (
    <div className="tabs">
      <Helmet
        bodyAttributes={{
          style: {
            display: "flex",
            justifyContent: "center",
            padding: "10px",
            background: "#efefef",
            color: "#333",
          },
        }}
      />
      <form onSubmit={handleCriarPlano} className="tab-form">
        <input className="input-tab" name="tabs" type="radio" id="tab-1" />
        <label className="label-tab" htmlFor="tab-1">
          APRESENTAÇÃO
        </label>
        <div className="panel">
          <h1>APRESENTAÇÃO</h1>
          <div className="tab-principals">
            <div className="tab-name">
              <p>Nome do Plano</p>
              <input
                type="text"
                className="tab-plan-name"
                placeholder="Insira o nome..."
                name="nome"
                onChange={handleEstados}
              />
            </div>
            <div>
              <p>Início do Prazo</p>
              <input type="date" className="date"  name="inicio_prazo" onChange={handleEstados}/>
            </div>
            <div>
              <p>Prazo de Vigência</p>
              <input type="date" className="date" name="final_prazo" onChange={handleEstados} />
            </div>
          </div>
          <p>Introdução</p>
          <textarea
            className="tab-plan"
            placeholder="Insira o texto..."
            name="introducao" onChange={handleEstados}
          />
          <Dropdown callback={handleEstados} planName={estadoDaApp.nome} planDescription={estadoDaApp.introducao} />
          <AddPlan />
          <AddImage />
        </div>
        <input className="input-tab" name="tabs" type="radio" id="tab-2" />
        <label className="label-tab" htmlFor="tab-2">
          {(estadoDaApp.nome || "NOME DO PLANO").toUpperCase()}
        </label>
        <div className="panel">
          <h1>{(estadoDaApp.introducao || "NOME DO PLANO").toUpperCase()}</h1>
          <AddPlan />
          <AddImage />
        </div>
        <input className="input-tab" name="tabs" type="radio" id="tab-3" />
        <label className="label-tab" htmlFor="tab-3">
          AÇÕES
        </label>
        <div className="panel">
          <AddActions />
        </div>
        <input className="input-tab" name="tabs" type="radio" id="tab-4" />
        <label className="label-tab" htmlFor="tab-4">
          BIBLIOTECA
        </label>
        <div className="panel">
          <h1>BIBLIOTECA</h1>
          <AddImage />
          <AddURL />
          <div className="submit-tab">
            <input type="submit" value="ADICIONAR PLANO" />
          </div>
        </div>
      </form>
    </div>
  );
}

export default Tabs;
