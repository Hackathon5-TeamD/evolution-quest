import styles from "./ResultItem.module.css";

type Props = {
  name: String;
  data: Number;
  notation: String;
};

export const ResultItem = (props: Props) => {
  const { name, data, notation } = props;
  return (
    <p className={styles.item}>
      {name} <span className={styles.span}>{data}</span>
      {notation}
    </p>
  );
};
