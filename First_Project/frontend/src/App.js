import './App.css';
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom'
import Home from './components/pages/Home'; 
import Analyze_page from './components/pages/Analyze'; 
import Store_page from './components/pages/Store'; 
import styles from './components/Button.module.css'
import Find_page from './components/pages/Find'; 



function App() {
  return (

    <Router>
      <div className="App">
        {/* <Link to="/"><button className={styles.button}></button></Link>*/}
        <h1>Welcome</h1>
        <Link to="/store"><button className={styles.button}>Store</button></Link>
        <Link to="/find"><button className={styles.button}>Find</button></Link>
        <Link to="/analyze"><button className={styles.button}>Analyze</button></Link>
      </div>
      <Routes>
        <Route exact path="/" element={<Home />}></Route>
        <Route exact path="/store" element={<Store_page />}></Route>
        <Route exact path="/find" element={<Find_page />}></Route>     
        <Route exact path="/analyze" element={<Analyze_page />}></Route>   
                
      </Routes>
    </Router>
  )
    
  
}

export default App;
