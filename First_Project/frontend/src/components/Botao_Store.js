import styles from './Botao.module.css';


function Botao_Store() {
    return (
        <div className={styles.BotaoContainer}>
            <button className={styles.BotaoContent}>Store</button>
        </div>
    )
}

export default Botao_Store