import styles from "./MainPage.module.css";
import "react-simple-keyboard/build/css/index.css";
import { GameArea } from "./gameArea/GameArea";
import { RecordArea } from "./recordArea/RecordArea";
import { Modal } from "./Modal/Modal";

export const MainPage = () => {
  return (
    <div className={styles.gamePageWrapper}>
      <GameArea />
      <RecordArea />
      <Modal />
    </div>
  );
};
