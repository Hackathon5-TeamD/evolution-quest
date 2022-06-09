import { Container } from "semantic-ui-react";
import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { RankingTable } from "./ResultTable/ResultTable";
import { SideBar } from "../SideBar/SideBar";
import styles from "./ResultPage.module.css";

import { useEffect, useState } from "react";
import { getRanking } from "../../../api/GetDataAPI";
import { mockData } from "../../../types/ResultType";

export const ResultPage = () => {
  const [rankingArr1, setRankingArr1] = useState<mockData[]>([]);
  const [rankingArr2, setRankingArr2] = useState<mockData[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [isReady, setReady] = useState<boolean>(false);
  const [timesFetchedArr2, setTimesFetchedArr2] = useState<number>(0);

  // サーバーにリザルトデータ配列を取りに行く関数
  const fetch = async (page: number) => {
    const res = await getRanking(page);
    // サーバーから取ってきたリザルトデータ配列をページごとに違うstate(配列)に入れる
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

  /**
   * ページ１、ページ２のテーブルを変数に入れる
   */
  const page1 =
    currentPage === 1 && isReady && rankingArr1.length !== 0 ? (
      <RankingTable
        rankingArr={rankingArr1}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        fetch={fetch}
        setReady={setReady}
        timesFetchedArr2={timesFetchedArr2}
        setTimesFetchedArr2={setTimesFetchedArr2}
      />
    ) : (
      <h1>Loading...</h1>
    );

  const page2 =
    currentPage === 2 && isReady && rankingArr2.length !== 0 ? (
      <RankingTable
        rankingArr={rankingArr2}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
        fetch={fetch}
        setReady={setReady}
        timesFetchedArr2={timesFetchedArr2}
        setTimesFetchedArr2={setTimesFetchedArr2}
      />
    ) : (
      <h1>Loading...その２</h1>
    );

  return (
    <div id="outer-container" className={styles.wrapper}>
      <SideBar pageWrapId={"page-wrap"} outerContainerId={"outer-container"} />
      <div id="page-wrap">
        <div className={styles.container}>
          <Header />
          <SubTitle currentPage={currentPage} />
          {currentPage === 1 ? page1 : page2}
        </div>
      </div>
    </div>
  );
};
