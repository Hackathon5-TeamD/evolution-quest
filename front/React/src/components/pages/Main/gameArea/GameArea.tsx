import { Screen } from "./screen/Screen";
import styles from "./GameArea.module.css";
import "react-simple-keyboard/build/css/index.css";
import Keyboard from "react-simple-keyboard";

type Props = {
  setModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

export const GameArea = (props: Props) => {
  const { setModalOpen } = props;
  return (
    <div className={styles.gameArea}>
      <Screen setModalOpen={setModalOpen} />
      <Keyboard
      // keyboardRef={(r) => (keyboard.current = r)}
      // layoutName={layout}
      // onChange={onChange}
      // onKeyPress={onKeyPress}
      />
    </div>
  );
};
