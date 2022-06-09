import { useEffect } from "react";
import styles from "./StartAlert.module.css";

type Props = {
  setAlertOn: React.Dispatch<React.SetStateAction<boolean>>;
};

export const StartAlert = (props: Props) => {
  const { setAlertOn } = props;
  const handleKeyDown = (event: KeyboardEvent) => {
    if (event.key === "Tab") {
      setAlertOn(false);
    }
  };
  useEffect(() => {
    document.addEventListener("keydown", handleKeyDown, false);
  }, []);

  return (
    <div className={styles.alertWrapper}>
      <h1 className={styles.alert}>Press Tab Button to start</h1>
    </div>
  );
};
