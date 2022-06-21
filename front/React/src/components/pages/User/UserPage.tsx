import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { GameRecord } from "./GameRecord/GameRecord";
import { SideBar } from "../SideBar/SideBar";
import styles from "./UserPage.module.css";

import { useEffect, useState } from "react";
import { getUserRecord } from "../../../api/GetDataAPI";
import { recordData } from "../../../types/UserType";
import { useRecoilValue } from "recoil";
import { userLoginState } from "../Register/Register";

export const UserPage = () => {
  const [recordArr, setRecordArr] = useState<recordData[]>([]);

  // ログイン情報を使う
  const data = useRecoilValue(userLoginState);
  // サーバーにユーザーデータ配列を取りに行く関数
  const fetch = async () => {
    const res = await getUserRecord();
    // サーバーから取ってきたユーザーデータ配列をページごとに違うstate(配列)に入れる
    setRecordArr(res);
  };

  useEffect(() => {
    fetch();
  }, []);

  return (
    <div id="outer-container" className={styles.wrapper}>
      <div>
        <SideBar
          pageWrapId={"page-wrap"}
          outerContainerId={"outer-container"}
        />
        <div id="page-wrap">
          <div className={styles.container}>
            <Header />

            {recordArr.length !== 0 ? (
              <>
                <SubTitle>User name : {data.user_name}</SubTitle>
                <GameRecord recordArr={recordArr} />
              </>
            ) : (
              <h1>Loading...</h1>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
