import styles from "./Register.module.css";
import { Input, Button } from "semantic-ui-react";
import { Title } from "../Login/Title/Title";

export const Register = () => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.container}>
        <Title text="SIGN UP" />
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
        <Button className={styles.signupbutton} size="small">
          Sign up
        </Button>
      </div>
    </div>
  );
};
