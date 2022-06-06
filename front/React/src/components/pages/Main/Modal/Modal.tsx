import styles from "./Modal.module.css";
import { Results } from "./ResultsArea/Results";

export const Modal = () => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.modalContent}>
        <p className={styles.title}>Result</p>
        <Results />
      </div>
    </div>
  );
};
