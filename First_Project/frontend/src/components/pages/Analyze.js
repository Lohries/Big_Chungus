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
      <input type="file" id="img-input-analyze" className={styles.input} />
      <Footer />
    </div>
  );
}

export default Analyze_page;
