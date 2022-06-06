import React from "react";
import { Button } from "semantic-ui-react";
import styles from "./RegisterButton.module.css";

export const RegisterButton = () => {
  return (
    <div className={styles.register}>
      <p>Not as member yet?</p>
      <Button basic size="mini" floated="right" color="youtube">
        Register
      </Button>
    </div>
  );
};
