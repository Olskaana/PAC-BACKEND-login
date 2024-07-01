import React from "react";
import { Link } from "react-router-dom";
import BookSvg from "./assets/BookSvg";
import TreeSvg from "./assets/TreeSvg";
import RiverSvg from "./assets/RiverSvg";
import TapSvg from "./assets/TapSvg";
import TerritorySvg from "./assets/TerritorySvg";
import AmvaliSvg from "./assets/AmvaliSvg";

function Card({
  selectedValue,
  planName,
  planDescription = "",
  maxDescriptionLength = 80,
}) {
  const SVG_MAP = {
    amvali: AmvaliSvg,
    infra: TerritorySvg,
    ambient: TreeSvg,
    hidro: TapSvg,
    river: RiverSvg,
    education: BookSvg,
  };

  const SvgComponent = SVG_MAP[selectedValue] || AmvaliSvg;

  const defaultDescription =
    "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor, consectetur adipiscing elit, sed do eiusmod tempor, consectetur adipiscing elit, sed do eiusmod tempor, consectetur adipiscing elit, sed do eiusmod tempor";
  const description = planDescription || defaultDescription;

  const truncatedDescription =
    description.length > maxDescriptionLength
      ? description.substring(0, maxDescriptionLength) + "..."
      : description;

  return (
    <div className="card">
      <Link to="">
        {SvgComponent && <SvgComponent />}
        <div className="text">
          <div className="card-title">
            <h2>{(planName || "NOME DO PLANO").toUpperCase()}</h2>
          </div>
          <div className="card-text">
            <p>
              {(
                truncatedDescription ||
                description.substring(0, maxDescriptionLength)
              ).toLowerCase()}
            </p>
          </div>
        </div>
        <div className="see-more">
          <div>
            <p>
              Leia mais <b id="arrow">→</b>
            </p>
          </div>
          <div className="date-card"><p>2024 - 2034</p></div>
        </div>
      </Link>
    </div>
  );
}

export default Card;
