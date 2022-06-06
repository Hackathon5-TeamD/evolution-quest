import styles from "./Button.module.css";

type Props = {
  buttonName: String;
  description: String;
};

export const Button = (props: Props) => {
  const { buttonName, description } = props;
  return (
    <>
      <button className={styles.button}>{buttonName}</button>
      <p className={styles.explanation}>{description}</p>
    </>
  );
};
