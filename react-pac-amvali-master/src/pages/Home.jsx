import React from "react";
import { Helmet } from "react-helmet";
import HeaderWhite from "../components/HeaderWhite";
import Map from "../components/Map";
import FooterWhite from "../components/FooterWhite";

export function Home() {
  return (
    <div className="main-page">
      <Helmet
        bodyAttributes={{
          style: "background-image: linear-gradient(#1480c0, #00801A);",
        }}
      />
      <HeaderWhite />
      <div className="map">
        <div className="map-title">
          <h1>ESCOLHA UM MUNICÍPIO</h1>
        </div>
        <Map />
      </div>
      <FooterWhite />
    </div>
  );
}
