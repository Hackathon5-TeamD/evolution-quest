import { useState, useEffect } from "react";
import styles from "./MainPage.module.css";
import "react-simple-keyboard/build/css/index.css";
import { GameArea } from "./gameArea/GameArea";
import { RecordArea } from "./recordArea/RecordArea";
import { Modal } from "./Modal/Modal";

// import { getTerminologie } from "../../../api/Terminologie";

export const MainPage = () => {
  const [isModalOpen, setModalOpen] = useState(false);
  // const [currentTerminologie, setCurrentTerminologie] = useState("");

  // const fetch = async (page: number) => {
  //   const res = await getTerminologie();

  //   // サーバーから取ってきた問題をstate(配列)に入れる
  //   setCurrentTerminologie(res);
  // };

  // useEffect(() => {
  //   fetch(1);
  // }, []);

  return (
    <div className={styles.gamePageWrapper}>
      <GameArea setModalOpen={setModalOpen} />
      <RecordArea />
      {isModalOpen && <Modal />}
    </div>
  );
};
