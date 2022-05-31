import "../App.css";
import { Input, Button } from "semantic-ui-react";

export const Login = () => {
  return (
    <div>
      <h1 className="title">LOG IN</h1>
      <div className="form">
        <Input type="text" focus fluid placeholder="UserName" />
        <br />
        <br />
        <Input type="password" focus fluid placeholder="Password" />
        <br />
        <br />
        <Input type="password" focus fluid placeholder="Confirm Password" />
        <br />
        <br />
        <Button className="login">Log in</Button>
        <div className="resister">
          <p>Not as member yet?</p>
          <Button basic size="mini" floated="right" color="black">
            Resister
          </Button>
        </div>
      </div>
    </div>
  );
};
