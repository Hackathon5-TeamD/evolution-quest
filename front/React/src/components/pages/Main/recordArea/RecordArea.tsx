import styles from "./RecordArea.module.css";
import { Accuracy } from "./accuracy/Accuracy";
import { Wpm } from "./wpm/Wpm";
import { Time } from "./time/Time";

type Props = {
  accuracy: number;
  wpm: number;
};

export const RecordArea = (props: Props) => {
  const { accuracy, wpm } = props;
  return (
    <div className={styles.recordArea}>
      <Accuracy accuracy={accuracy} />
      <Wpm wpm={wpm} />
      <Time />
    </div>
  );
};
