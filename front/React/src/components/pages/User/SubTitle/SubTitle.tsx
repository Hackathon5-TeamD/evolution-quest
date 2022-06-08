import styles from "./SubTitle.module.css";

type Props = {
  user_name: string;
};

export const SubTitle = (props: Props) => {
  const { user_name } = props;
  return <p className={styles.subtitle}>User name : {user_name}</p>;
};
