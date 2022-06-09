import styles from "./Results.module.css";
import { ResultItem } from "./Resultem/ResultItem";
import { Button } from "./Buttons/Button";

type Props = {
  accuracy: number;
  wpm: number;
  durationTime: number;
};

export const Results = (props: Props) => {
  const { accuracy, wpm, durationTime } = props;
  return (
    <div className={styles.wrapper}>
      <div className={styles.resultArea}>
        <ResultItem name={"Time"} data={durationTime} notation={"seconds"} />
        <ResultItem name={"Accuracy"} data={accuracy} notation={"%"} />
        <ResultItem name={"Average WPM"} data={wpm} notation={"wpm"} />
      </div>
      <div className={styles.buttonArea}>
        <Button
          buttonName={"Another Game"}
          description={"or press Enter to restart"}
        />
        <Button buttonName={"Finish"} description={"to go back to main"} />
      </div>
    </div>
  );
};
