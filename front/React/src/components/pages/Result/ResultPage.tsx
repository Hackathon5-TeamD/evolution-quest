import { Container } from "semantic-ui-react";
import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { RankingTable } from "./ResultTable/ResultTable";
import { SideBar } from "../SideBar/SideBar";
import styles from "./ResultPage.module.css";

export const ResultPage = () => {
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
              <RankingTable />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
