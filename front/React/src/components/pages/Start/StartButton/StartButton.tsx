import styles from "./StartButton.module.css";

export const StartButton = () => {
  return (
    <div>
      <button className={styles.button}>Game Start</button>
      <p className={styles.text}>or press Enter to start a game</p>
    </div>
  );
};
