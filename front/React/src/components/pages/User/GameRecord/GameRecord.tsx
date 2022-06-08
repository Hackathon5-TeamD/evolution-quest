import styles from "./GameRecord.module.css";
import { GameRecordTable } from "./Table/Table";

type Props = {
  recordArr: Array<{
    id: number;
    played_at: Date;
    accuracy: number;
    wpm: number;
  }>;
};

export const GameRecord = (props: Props) => {
  const { recordArr } = props;
  return (
    <div className={styles.container}>
      <p className={styles.title}>Games History</p>
      <GameRecordTable recordArr={recordArr} />
    </div>
  );
};
