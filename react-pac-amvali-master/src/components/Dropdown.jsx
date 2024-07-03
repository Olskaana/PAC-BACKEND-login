import React, { useState } from "react";
import TerritorySvg from "./assets/TerritorySvg"; // SVG component for 'infra'
import TreeSvg from "./assets/TreeSvg"; // SVG component for 'ambient'
import TapSvg from "./assets/TapSvg"; // SVG component for 'hidro'
import RiverSvg from "./assets/RiverSvg"; // SVG component for 'hidro'
import BookSvg from "./assets/BookSvg"; // SVG component for 'education'
import AmvaliSvg from "./assets/AmvaliSvg"; // SVG component for 'amvali'
import Card from "./Card";

function Dropdown({ planName, planDescription }) {
  const [selected, setSelected] = useState("");

  const handleChange = (event) => {
    setSelected(event.target.value);
  };

  const SVG_MAP = {
    amvali: AmvaliSvg,
    infra: TerritorySvg,
    ambient: TreeSvg,
    hidro: TapSvg,
    river: RiverSvg,
    education: BookSvg,
  };

  return (
    <div>
      <p>Selecione a Categoria do seu Plano</p>
      <select className="dropdown" value={selected} onChange={handleChange}>
        <option value="">Categoria do Plano...</option>
        <option value="infra">Infraestrutura</option>
        <option value="ambient">Meio Ambiente</option>
        <option value="education">Educação</option>
        <option value="hidro">Hidro</option>
        <option value="river">Rio</option>
      </select>
      <Card planName={planName} selectedValue={selected} planDescription={planDescription}/>
    </div>
  );
}

export default Dropdown;