import styles from './Footer.module.css'


function Footer() {
    return (
      <footer className={styles.footer}>
       
        <a href='https://ipfacens.com.br/ecossistema/brain-facens/'>
          <img className={styles.left_image} src='img/brain.png' alt="Brain" />
        </a>
        <a href='https://pypi.org/project/deepface/'>
          <img className={styles.right_image}src='img/brain.png' alt="DeepFace" />
        </a>

      </footer>
    );
  }
  
  export default Footer;
  