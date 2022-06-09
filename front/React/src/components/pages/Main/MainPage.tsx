import styles from "./MainPage.module.css";
import "react-simple-keyboard/build/css/index.css";
import { GameArea } from "./gameArea/GameArea";
import { RecordArea } from "./recordArea/RecordArea";
import { Modal } from "./Modal/Modal";
import useTypingGame from "react-typing-game-hook";
import { useTimer } from "../../../hooks/useTimer";
import { useGame } from "../../../hooks/useGame";
import { useState, useEffect } from "react";
import { StartAlert } from "./StartAlert/StartAlert";

export const MainPage = () => {
  const [isModalOpen, setModalOpen] = useState(false);
  const [isAlertOn, setAlertOn] = useState(true);
  const { jaTerm, roTerm, fetchGame } = useGame();
  const fetchGameData = () => fetchGame();
  const { time } = useTimer();
  // console.log(time);

  const fetch = async () => {
    const res = await fetchGameData();
    insertTyping();
  };

  // Call the hook
  const {
    // phase : {0:ミスタート,　1:　入力中,　2:終わり}
    states: { chars, charsState, correctChar, errorChar, phase },
    // getDuration() : スタートから現在打ってる文字までにかかった秒数(ミリ秒)
    actions: { insertTyping, resetTyping, deleteTyping, getDuration },
  } = useTypingGame(roTerm, {
    skipCurrentWordOnSpace: true,
    pauseOnError: true,
    countErrors: "everytime",
  });

  useEffect(() => {
    fetchGameData();
  }, []);

  // ミリ秒数： getDuration()
  // 正解数: correctChar
  // ミスタイプ: errorChar

  // accuracy計算
  let accuracy = (correctChar / (correctChar + errorChar)) * 100;
  let flooredAccuracy = Math.floor(accuracy * 10) / 10;

  // WPM計算
  const sec = parseFloat((getDuration() / 1000).toFixed(2));
  let wpm = Math.floor(((correctChar + errorChar) / sec) * 60);

  useEffect(() => {
    if (phase === 2) {
      console.log(getDuration() + " : ミリ秒かかった");
      setModalOpen(true);
    }
  }, [phase]);

  return (
    <div className={styles.gamePageWrapper}>
      <GameArea
        jaTerm={jaTerm}
        roTerm={roTerm}
        insertTyping={insertTyping}
        resetTyping={resetTyping}
        deleteTyping={deleteTyping}
        chars={chars}
        charsState={charsState}
      />
      <RecordArea accuracy={flooredAccuracy} wpm={wpm} />
      {isModalOpen && (
        <Modal accuracy={flooredAccuracy} wpm={wpm} durationTime={sec} />
      )}
      {isAlertOn && <StartAlert setAlertOn={setAlertOn} />}
    </div>
  );
};
