import { Title } from "./Title/Title";
import styles from "./Login.module.css";
import { Input, Button } from "semantic-ui-react";
import { RegisterButton } from "./RegisterButton/RegisterButton";

export const Login = () => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.container}>
        <Title text="LOG IN" />
        <Input
          className={styles.form}
          type="text"
          focus
          fluid
          placeholder="UserName"
        />
        <Input
          className={styles.form}
          type="password"
          focus
          fluid
          placeholder="Password"
        />
        <Input
          className={styles.form}
          type="password"
          focus
          fluid
          placeholder="Confirm Password"
        />
        <Button className={styles.loginbutton} size="small">
          Log in
        </Button>
        <RegisterButton />
      </div>
    </div>
  );
};
