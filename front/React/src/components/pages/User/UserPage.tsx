import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { GameRecord } from "./GameRecord/GameRecord";
import { SideBar } from "../SideBar/SideBar";
import styles from "./UserPage.module.css";

export const UserPage = () => {
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
            <GameRecord />
          </div>
        </div>
      </div>
    </div>
  );
};
