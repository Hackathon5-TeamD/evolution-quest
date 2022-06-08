import { Container } from "semantic-ui-react";
import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { RankingTable } from "./ResultTable/ResultTable";
import { SideBar } from "../SideBar/SideBar";
import styles from "./ResultPage.module.css";

import { useEffect, useState } from "react";
import { getRanking } from "./GetDataAPI";

type mockData = {
  id: number;
  user_id: number;
  user_name: string;
  played_at: Date;
  accuracy: number;
  wpm: number;
};

export const ResultPage = () => {
  const [rankingArr1, setRankingArr1] = useState<mockData[]>([]);
  const [rankingArr2, setRankingArr2] = useState<mockData[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [isReady, setReady] = useState<boolean>(false);

  console.log(rankingArr2.length + " : rankingArr2.length");

  const fetch = async (page: number) => {
    const res = await getRanking(page);
    console.log("レスポンス: " + res);

    console.log(page + " : page");
    if (page === 1) {
      setRankingArr1(res);
      setReady(true);
    } else {
      setRankingArr2(res);
      setReady(true);
    }
  };

  // 1回目のローディングは1-10位のデータを何もしなくても取ってくる
  useEffect(() => {
    fetch(1);
  }, []);

  const page1 =
    currentPage === 1 && isReady && rankingArr1.length !== 0 ? (
      <RankingTable
        rankingArr={rankingArr1}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        fetch={fetch}
        setReady={setReady}
      />
    ) : (
      <>
        <h1>Loading...</h1>
      </>
    );

  const page2 =
    currentPage === 2 && isReady && rankingArr2.length !== 0 ? (
      <RankingTable
        rankingArr={rankingArr2}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        fetch={fetch}
        setReady={setReady}
      />
    ) : (
      <>
        <h1>Loading...その２</h1>
      </>
    );

  return (
    <div id="outer-container" className={styles.wrapper}>
      <div>
        <SideBar
          pageWrapId={"page-wrap"}
          outerContainerId={"outer-container"}
        />
        <div id="page-wrap">
          <div>
            <div className={styles.container}>
              <Header />
              <SubTitle />
              {currentPage === 1 ? page1 : page2}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
