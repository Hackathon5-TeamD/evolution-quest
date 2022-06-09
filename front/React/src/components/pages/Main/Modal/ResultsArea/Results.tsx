import styles from "./Results.module.css";
import { ResultItem } from "./Resultem/ResultItem";
import { Button } from "./Buttons/Button";

export const Results = () => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.resultArea}>
        <ResultItem name={"Time"} data={52} notation={"seconds"} />
        <ResultItem name={"Accuracy"} data={87} notation={"%"} />
        <ResultItem name={"Average WPM"} data={124} notation={"wpm"} />
      </div>
      <div className={styles.buttonArea}>
        <Button
          buttonName={"Another Game"}
          description={"or press Enter to restart"}
          linkTo={"/main"}
        />
        <Button
          buttonName={"Finish"}
          description={"to go back to main"}
          linkTo={"/gamestart"}
        />
      </div>
    </div>
  );
};
