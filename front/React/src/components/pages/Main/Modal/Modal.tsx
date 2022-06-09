import styles from "./Modal.module.css";
import { Results } from "./ResultsArea/Results";

type Props = {
  accuracy: number;
  wpm: number;
  durationTime: number;
};

export const Modal = (props: Props) => {
  const { accuracy, wpm, durationTime } = props;
  return (
    <div className={styles.wrapper}>
      <div className={styles.modalContent}>
        <p className={styles.title}>Result</p>
        <Results accuracy={accuracy} wpm={wpm} durationTime={durationTime} />
      </div>
    </div>
  );
};
