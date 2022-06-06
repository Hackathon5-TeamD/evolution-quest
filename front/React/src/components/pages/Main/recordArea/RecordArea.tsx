import styles from "./RecordArea.module.css";
import { Accuracy } from "./accuracy/Accuracy";
import { Wpm } from "./wpm/Wpm";
import { Time } from "./time/Time";

export const RecordArea = () => {
  return (
    <div className={styles.recordArea}>
      <Accuracy />
      <Wpm />
      <Time />
    </div>
  );
};
