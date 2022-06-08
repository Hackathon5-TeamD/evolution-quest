import { Container } from "semantic-ui-react";
import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { RankingTable } from "./ResultTable/ResultTable";
import { SideBar } from "../SideBar/SideBar";
import styles from "./ResultPage.module.css";

import { useEffect, useState } from "react";
import { getRanking } from "./GetDataAPI";

// type Ranking = {
//   userName: String;
//   playedAt: Date;
//   accuracy: Number;
//   wpm: Number;
// };

type mockData = {
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
  const isPage1Ready: boolean = rankingArr1.length === 0 ? false : true;
  const isPage2Ready: boolean = rankingArr2.length === 0 ? false : true;

  const fetch = async () => {
    const res = await getRanking(currentPage);
    if (currentPage === 1) {
      setRankingArr1(res);
    } else {
      setRankingArr2(res);
    }
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
          <div>
            <div className={styles.container}>
              <Header />
              <SubTitle />
              {currentPage === 1 && isPage1Ready ? (
                <RankingTable rankingArr={rankingArr1} />
              ) : (
                <>
                  <h1>Loading...</h1>
                </>
              )}
              {currentPage === 2 && isPage2Ready ? (
                <RankingTable rankingArr={rankingArr2} />
              ) : (
                <>
                  <h1>Loading...</h1>
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
