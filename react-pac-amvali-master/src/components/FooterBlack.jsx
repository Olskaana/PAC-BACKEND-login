import React from "react";
import black_logo from "./assets/Logo AMV Black.png";

function FooterBlack() {
  return (
    <footer>
      <div>
        <a
          href="https://amvali.org.br/"
          target="_blank"
          rel="noopener noreferrer"
        >
          <img src={black_logo} alt="Amvali Black Logo" />
        </a>
      </div>
      <div className="footer-text">
        <p>CNPJ 83.784.090/0001-86</p>
        <p>
          Endereço Rua Arthur Gumz, 88, Vila Nova, Jaraguá do Sul - SC,
          89259-340
        </p>
      </div>
      <div className="footer-text">
        <p>Telefone (47) 3370-7933</p>
        <p>Email planejamento@amvali.org.br</p>
      </div>
    </footer>
  );
}

export default FooterBlack;
