import { Title } from "./Title/Title";
import styles from "./Login.module.css";
import { Input, Button } from "semantic-ui-react";
import { RegisterButton } from "./RegisterButton/RegisterButton";

export const Login = () => {
  return (
    <div>
      <Title />
      <div className={styles.form}>
        <Input type="text" focus fluid placeholder="UserName" />
        <br />
        <br />
        <Input type="password" focus fluid placeholder="Password" />
        <br />
        <br />
        <Input type="password" focus fluid placeholder="Confirm Password" />
        <br />
        <br />
        <Button className={styles.button}>Log in</Button>
        <RegisterButton />
      </div>
    </div>
  );
};
