import logo from './logo.svg';
import './App.css';
import HelloWorld from './components/HelloWorld'
import Frase from './components/Frase';
import SayMyName from './components/SayMyName';


const url = 'https://pypi-camo.freetls.fastly.net/de66dd808c5fb44ea531fb78fc56ddfb2e0505bc/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f736572656e67696c2f64656570666163652f6d61737465722f69636f6e2f64656570666163652d69636f6e2e706e67'

function App() {
  return (
    <div className="App">
      <h1>Bem-Vindo</h1>
      <p>Primeiro projeto</p>
      <HelloWorld/>
      <Frase/>
      <SayMyName nome="Luis"/>
    </div>
  );
}

export default App;
