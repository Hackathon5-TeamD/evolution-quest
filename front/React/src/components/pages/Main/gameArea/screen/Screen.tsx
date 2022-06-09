import styles from "./screen.module.css";
import { TypingGameComponent } from "./Typing/Typing";
import { JapaneseTerm } from "./japanese/JapaneseTerm";
import useTypingGame from "react-typing-game-hook";
import { useState, useEffect } from "react";
import { getTerminologie } from "../../../../../api/Terminologie";

type Props = {
  setModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

export const Screen = (props: Props) => {
  const { setModalOpen } = props;
  const [jaTerm, setJaTerm] = useState("");
  const [roTerm, setRoTerm] = useState("");
  // const [currentTerminologie, setCurrentTerminologie] = useState("");

  const fetch = async () => {
    const res = await getTerminologie();

    // サーバーから取ってきた問題をstate(配列)に入れる
    setRoTerm(res[0]["description_ro"]);
    setJaTerm(res[0]["description_ja"]);
  };

  useEffect(() => {
    fetch();
  }, []);

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

  // ミリ秒数： getDuration()
  // 正解数: correctChar
  // ミスタイプ: errorChar

  // accuracy計算
  let accuracy = (correctChar / (correctChar + errorChar)) * 100;
  let flooredAccuracy = Math.floor(accuracy * 10) / 10;

  if (phase === 2) {
    console.log(getDuration() + " : ミリ秒かかった");
    setModalOpen(true);
  }

  return (
    <div className={styles.screenArea}>
      <JapaneseTerm text={jaTerm} />
      <p className={styles.border}></p>
      <TypingGameComponent
        roTerm={roTerm}
        insertTyping={insertTyping}
        resetTyping={resetTyping}
        deleteTyping={deleteTyping}
        chars={chars}
        charsState={charsState}
      />
    </div>
  );
};
