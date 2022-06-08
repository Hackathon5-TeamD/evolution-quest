import styles from "./Header.module.css";

type Props = {
  user_name: string;
};

export const Header = (props: Props) => {
  const { user_name } = props;
  return <h1 className={styles.title}>Your Account</h1>;
};
