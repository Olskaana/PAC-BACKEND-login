import React, { useState } from "react";
import { Helmet } from "react-helmet";
import AddPlan from "./AddPlan.jsx";
import AddImage from "./AddImage.jsx";
import Dropdown from "./Dropdown.jsx";
import AddActions from "./AddActions.jsx";
import AddURL from "./AddURL.jsx";

function Tabs() {
  const [planName, setPlanName] = useState("");

  const handlePlanNameChange = (event) => {
    setPlanName(event.target.value);
  };

  const [planDescription, setPlanDescription] = useState("");

  const handlePlanDescriptionChange = (event) => {
    setPlanDescription(event.target.value);
  };

  var textareas = document.getElementsByTagName("textarea");
  var count = textareas.length;
  for (var i = 0; i < count; i++) {
    textareas[i].onkeydown = function (e) {
      if (e.keyCode === 9 || e.which === 9) {
        e.preventDefault();
        var s = this.selectionStart;
        this.value =
          this.value.substring(0, this.selectionStart) +
          "\t" +
          this.value.substring(this.selectionEnd);
        this.selectionEnd = s + 1;
      }
    };
  }

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
      <form method="post" className="tab-form">
        <input className="input-tab" name="tabs" type="radio" id="tab-1" />
        <label className="label-tab" for="tab-1">
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
                value={planName}
                onChange={handlePlanNameChange}
              />
            </div>
            <div>
              <p>Início do Prazo</p>
              <input type="date" className="date" />
            </div>
            <div>
              <p>Prazo de Vigência</p>
              <input type="date" className="date" />
            </div>
          </div>
          <p>Introdução</p>
          <textarea
            className="tab-plan"
            placeholder="Insira o texto..."
            value={planDescription}
            onChange={handlePlanDescriptionChange}
          />
          <Dropdown planName={planName} planDescription={planDescription} />
          <AddPlan />
          <AddImage />
        </div>
        <input className="input-tab" name="tabs" type="radio" id="tab-2" />
        <label className="label-tab" for="tab-2">
          {(planName || "NOME DO PLANO").toUpperCase()}
        </label>
        <div className="panel">
          <h1>{(planName || "NOME DO PLANO").toUpperCase()}</h1>
          <AddPlan />
          <AddImage />
        </div>
        <input className="input-tab" name="tabs" type="radio" id="tab-3" />
        <label className="label-tab" for="tab-3">
          AÇÕES
        </label>
        <div className="panel">
          <AddActions />
        </div>
        <input className="input-tab" name="tabs" type="radio" id="tab-4" />
        <label className="label-tab" for="tab-4">
          BIBLIOTECA
        </label>
        <div className="panel">
          <h1>BIBLIOTECA</h1>
          <AddImage />
          <AddURL />
          <div className="submit-tab">
            <input
              type="submit"
              value="ADICIONAR PLANO"
            />
          </div>
        </div>
      </form>
    </div>
  );
}

export default Tabs;
