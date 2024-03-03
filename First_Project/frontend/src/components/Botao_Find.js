import styles from './Botao.module.css';


function Botao_Find() {
    return (
        <div className={styles.BotaoContainer}>
            <button className={styles.BotaoContent}>Find</button>
        </div>
    )
}

export default Botao_Find