import { Screen } from "./screen/Screen";
// import { KeyBoardArea } from "./keyBoard/KeyBoardArea";
import styles from "./GameArea.module.css";

import "react-simple-keyboard/build/css/index.css";

import Keyboard from "react-simple-keyboard";

export const GameArea = () => {
  return (
    <div className={styles.gameArea}>
      <Screen />
      {/* <KeyBoardArea /> */}

      <Keyboard

      // keyboardRef={(r) => (keyboard.current = r)}
      // layoutName={layout}
      // onChange={onChange}
      // onKeyPress={onKeyPress}
      />
    </div>
  );
};
