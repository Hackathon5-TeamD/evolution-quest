import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { GameRecord } from "./GameRecord/GameRecord";
import { SideBar } from "../SideBar/SideBar";
import styles from "./UserPage.module.css";

import { useEffect, useState } from "react";
import { getUserRecord } from "../../../api/GetDataAPI";

type mockData = {
  id: number;
  played_at: Date;
  accuracy: number;
  wpm: number;
};

export const UserPage = () => {
  const [recordArr, setRecordArr] = useState<mockData[]>([]);
  // const [isReady, setReady] = useState<boolean>(false);

  // サーバーにユーザーデータ配列を取りに行く関数
  const fetch = async () => {
    const res = await getUserRecord();
    // サーバーから取ってきたリザルトデータ配列をページごとに違うstate(配列)に入れる
    setRecordArr(res);
    // setReady(true);
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
            <SubTitle />
            {recordArr.length !== 0 ? (
              <GameRecord recordArr={recordArr} />
            ) : (
              <h1>Loading...</h1>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
