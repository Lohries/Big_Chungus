import './App.css';

import SayMyName from './components/SayMyName';
import Botao_Analise from './components/Botao_Analise';
import Botao_Find from './components/Botao_Find';
import Botao_Store from './components/Botao_Store';


const url = 'https://img.freepik.com/vetores-premium/abstrato-azul-moderno-design-de-ilustracao-vetorial-para-apresentacao-banner-capa-web-flyer-cartao-poster-papel-de-parede-textura-slide-revista-e-powerpoint_181182-19679.jpg';

function App() {
  return (
    <div className="App">
      <h1>Bem-Vindo</h1>
      <SayMyName nome="Luis"/>
      <Botao_Store/>
      <Botao_Find/>
      <Botao_Analise/>
      
    </div>
  );
}

export default App;
