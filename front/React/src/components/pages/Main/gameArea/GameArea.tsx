import { Screen } from "./screen/Screen";
import styles from "./GameArea.module.css";
import "react-simple-keyboard/build/css/index.css";
import Keyboard from "react-simple-keyboard";

type Props = {
  jaTerm: string;
  roTerm: string;
  insertTyping: (char?: string | undefined) => void;
  resetTyping: () => void;
  deleteTyping: (deleteWord?: boolean | undefined) => void;
  chars: string;
  charsState: any;
};

export const GameArea = (props: Props) => {
  return (
    <div className={styles.gameArea}>
      <Screen
        jaTerm={props.jaTerm}
        roTerm={props.roTerm}
        insertTyping={props.insertTyping}
        resetTyping={props.resetTyping}
        deleteTyping={props.deleteTyping}
        chars={props.chars}
        charsState={props.charsState}
      />
      <Keyboard
      // keyboardRef={(r) => (keyboard.current = r)}
      // layoutName={layout}
      // onChange={onChange}
      // onKeyPress={onKeyPress}
      />
    </div>
  );
};
