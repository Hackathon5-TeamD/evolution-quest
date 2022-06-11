import { ChangeEvent, memo, useContext, useState, VFC } from "react";
import styles from "./Register.module.css";
import { Input, Button } from "semantic-ui-react";
import { Title } from "../Login/Title/Title";
import { useNavigate } from "react-router-dom";

// サインアップとは、会員登録のこと。このページでは会員登録のロジックを書く。

export const Register: VFC = memo(() => {
  const navigate = useNavigate();
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  // グローバルなstate
  const { setUserData } = useContext(UserContext);

  // ローディングフラグ 今回は必要ない？？？
  // const [isLoading, setIsLoading] = useState(false);

  // ユーザーネームを保存する関数
  const onChangeUserNameInput = (e: ChangeEvent<HTMLInputElement>) => {
    setUserName(e.target.value);
  };

  // パスワードを保存する関数
  const onChangePasswordInput = (e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
  };

  // 確認用パスワードの値を保存する関数
  const onChangeConfirmPasswordInput = (e: ChangeEvent<HTMLInputElement>) => {
    setConfirmPassword(e.target.value);
  };

  // Sign Upボタンを押した時に発火する関数　登録処理
  const onClickCreateAccount = async () => {
    if (!userName || !password || !confirmPassword) {
      setErrorMessage("未入力の項目があります");
      return;
    } else if (password !== confirmPassword) {
      setErrorMessage("パスワードが一致しません");
      return;
    }
    // setIsLoading(true);
    try {
      const signinResult = await postRegisterUser(userName, password);
      if (signinResult) {
        const signupResult = await postLoginUser(
          signinResult.userName,
          password
        );
        if (signupResult) {
          setUserData(signupResult);
          localStorage.setItem("token", signupResult.token);
          navigate("/");
        }
      }
    } catch {
      setErrorMessage("サインインできませんでした");
      // } finally {
      //   // setIsLoading(false);
      // }
    }

    return (
      <div className={styles.wrapper}>
        <div className={styles.container}>
          <Title text="SIGN UP" />
          {/* username欄 */}
          <Input
            className={styles.form}
            type="text"
            focus
            fluid
            placeholder="UserName"
            onChange={onChangeUserNameInput}
          />
          {/* password欄 */}
          <Input
            className={styles.form}
            type="password"
            focus
            fluid
            placeholder="Password"
            onChange={onChangePasswordInput}
            value={password}
          />
          {/* 確認用password欄 */}
          <Input
            className={styles.form}
            type="password"
            focus
            fluid
            placeholder="Confirm Password"
            onChange={onChangeConfirmPasswordInput}
            value={confirmPassword}
          />
          <Button
            className={styles.signupbutton}
            size="small"
            onClick={onClickCreateAccount}
          >
            Sign up
          </Button>
        </div>
        {errorMessage ? (
          <p className={styles.errorMessage}>{errorMessage}</p>
        ) : null}
      </div>
    );
  };
});
