import styles from "./Button.module.css";
import { useNavigate } from "react-router-dom";

type Props = {
  buttonName: String;
  description: String;
  linkTo: string;
};

export const Button = (props: Props) => {
  const { buttonName, description, linkTo } = props;
  const navigation = useNavigate();

  return (
    <>
      <button className={styles.button} onClick={() => navigation(linkTo)}>
        {buttonName}
      </button>
      <p className={styles.explanation}>{description}</p>
    </>
  );
};
