import styles from './Footer.module.css'


function Footer() {
    return (
      <footer className={styles.footer}>
       
        <a href='https://ipfacens.com.br/ecossistema/brain-facens/'>
          <img className={styles.left_image} src="https://avatars.githubusercontent.com/u/67384594?s=280&v=4" alt="Brain" />
        </a>
        <a href='https://pypi.org/project/deepface/'>
          <img className={styles.right_image}src="https://pypi-camo.freetls.fastly.net/de66dd808c5fb44ea531fb78fc56ddfb2e0505bc/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f736572656e67696c2f64656570666163652f6d61737465722f69636f6e2f64656570666163652d69636f6e2e706e67" alt="DeepFace" />
        </a>

      </footer>
    );
  }
  
  export default Footer;
  