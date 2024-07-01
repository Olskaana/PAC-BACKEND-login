import { useLocation } from "react-router-dom";

function CountyData() {
  const location = useLocation();

  let pageTitle;
  let pageLink;
  let countyShield;
  let pageReturn;
  switch (location.pathname) {
    case "/corupa":
      pageTitle = "CORUPÁ";
      pageLink = "https://corupa.atende.net/cidadao";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/6/60/Bras%C3%A3o_do_munic%C3%ADpio_de_Corup%C3%A1_%28SC%29.png";
      break;
    case "/jaragua-do-sul":
      pageTitle = "JARAGUÁ DO SUL";
      pageLink = "https://www.jaraguadosul.sc.gov.br/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/0/04/Brasao_JaraguadoSul_SantaCatarina_Brasil.svg";
      break;
    case "/schroeder":
      pageTitle = "SCHROEDER";
      pageLink = "https://schroeder.sc.gov.br/";
      countyShield =
        "https://www.energiaconcursos.com.br/wp-content/uploads/2016/05/schoreder.png";
      break;
    case "/guaramirim":
      pageTitle = "GUARAMIRIM";
      pageLink = "https://guaramirim.atende.net/cidadao";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bras%C3%A3o_do_munic%C3%ADpio_de_Guaramirim_%28SC%29.svg/989px-Bras%C3%A3o_do_munic%C3%ADpio_de_Guaramirim_%28SC%29.svg.png";
      break;
    case "/massaranduba":
      pageTitle = "MASSARANDUBA";
      pageLink = "https://massaranduba.atende.net/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/2/22/Bras%C3%A3o_do_munic%C3%ADpio_de_Massaranduba_%28SC%29.png";
      break;
    case "/sao-joao-do-itaperiu":
      pageTitle = "SÃO JOÃO DO ITAPERIÚ";
      pageLink = "https://servicos.pmsji.sc.gov.br/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Bras%C3%A3o_do_munic%C3%ADpio_de_S%C3%A3o_Jo%C3%A3o_do_Itaperi%C3%BA_%28SC%29.svg/1200px-Bras%C3%A3o_do_munic%C3%ADpio_de_S%C3%A3o_Jo%C3%A3o_do_Itaperi%C3%BA_%28SC%29.svg.png";
      break;
    case "/barra-velha":
      pageTitle = "BARRA VELHA";
      pageLink = "https://barravelha.atende.net/cidadao";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Bras%C3%A3o_do_munic%C3%ADpio_de_Barra_Velha_%28SC%29.svg/1200px-Bras%C3%A3o_do_munic%C3%ADpio_de_Barra_Velha_%28SC%29.svg.png";
      break;
    case "/corupa/criar-plano":
      pageTitle = "CORUPÁ";
      pageLink = "https://servicos.corupa.sc.gov.br/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/6/60/Bras%C3%A3o_do_munic%C3%ADpio_de_Corup%C3%A1_%28SC%29.png";
      pageReturn = "../corupa";
      break;
    case "/jaragua-do-sul/criar-plano":
      pageTitle = "JARAGUÁ DO SUL";
      pageLink = "https://www.jaraguadosul.sc.gov.br/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/0/04/Brasao_JaraguadoSul_SantaCatarina_Brasil.svg";
      pageReturn = "../jaragua-do-sul";
      break;
    case "/schroeder/criar-plano":
      pageTitle = "SCHROEDER";
      pageLink = "https://schroeder.sc.gov.br/";
      countyShield =
        "https://www.energiaconcursos.com.br/wp-content/uploads/2016/05/schoreder.png";
      pageReturn = "../schroeder";
      break;
    case "/guaramirim/criar-plano":
      pageTitle = "GUARAMIRIM";
      pageLink = "https://guaramirim.atende.net/cidadao";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Bras%C3%A3o_do_munic%C3%ADpio_de_Guaramirim_%28SC%29.svg/989px-Bras%C3%A3o_do_munic%C3%ADpio_de_Guaramirim_%28SC%29.svg.png";
      pageReturn = "../guaramirim";
      break;
    case "/massaranduba/criar-plano":
      pageTitle = "MASSARANDUBA";
      pageLink = "https://massaranduba.atende.net/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/2/22/Bras%C3%A3o_do_munic%C3%ADpio_de_Massaranduba_%28SC%29.png";
      pageReturn = "../massaranduba";
      break;
    case "/sao-joao-do-itaperiu/criar-plano":
      pageTitle = "SÃO JOÃO DO ITAPERIÚ";
      pageLink = "https://servicos.pmsji.sc.gov.br/";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Bras%C3%A3o_do_munic%C3%ADpio_de_S%C3%A3o_Jo%C3%A3o_do_Itaperi%C3%BA_%28SC%29.svg/1200px-Bras%C3%A3o_do_munic%C3%ADpio_de_S%C3%A3o_Jo%C3%A3o_do_Itaperi%C3%BA_%28SC%29.svg.png";
      pageReturn = "../sao-joao-do-itaperiu";
      break;
    case "/barra-velha/criar-plano":
      pageTitle = "BARRA VELHA";
      pageLink = "https://barravelha.atende.net/cidadao";
      countyShield =
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Bras%C3%A3o_do_munic%C3%ADpio_de_Barra_Velha_%28SC%29.svg/1200px-Bras%C3%A3o_do_munic%C3%ADpio_de_Barra_Velha_%28SC%29.svg.png";
      pageReturn = "../barra-velha";
      break;
    default:
      pageTitle = "AMVALI";
      pageLink = "https://amvali.org.br/";
      countyShield = "";
  }

  return { pageTitle, pageLink, countyShield, pageReturn };
}

export default CountyData;
