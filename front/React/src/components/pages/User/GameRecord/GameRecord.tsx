import styles from "./GameRecord.module.css";
import { GameRecordTable } from "./Table/Table";

export const GameRecord = () => {
  return (
    <div className={styles.container}>
      <p className={styles.title}>Games History</p>
      <GameRecordTable />
    </div>
  );
};
