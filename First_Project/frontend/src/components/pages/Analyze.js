import Footer from "../Footer";
import Header from "../Header";

import styles from "../CamDisplay.module.css";

function Analyze_page() {
  return (
    <div>
      <Header />
     
      <div className={styles.Display_out}>
        <p>Resultados</p>
      </div>
      <button onclick="">Click Here to analyze</button>
      
      <Footer />
    </div>
  );
}

export default Analyze_page;
