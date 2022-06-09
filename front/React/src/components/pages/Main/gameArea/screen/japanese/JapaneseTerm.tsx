import styles from "../screen.module.css";

type Props = {
  text: string;
};

export const JapaneseTerm = (props: Props) => {
  const { text } = props;
  return (
    <div>
      <p className={styles.typeTitle}>
        Web3層構造
        <span>{text}</span>
      </p>
    </div>
  );
};
