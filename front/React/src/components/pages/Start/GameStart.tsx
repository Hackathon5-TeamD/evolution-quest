import React from "react";
import styles from "./GameStart.module.css";
import { StartButton } from "./StartButton/StartButton";
import { SideBar } from "../SideBar/SideBar";

export const GameStart = () => {
  return (
    <div id="outer-container" className={styles.wrapper}>
      <div>
        <SideBar
          pageWrapId={"page-wrap"}
          outerContainerId={"outer-container"}
        />
        <div id="page-wrap">
          <div className={styles.container}>
            <StartButton />
          </div>
        </div>
      </div>
    </div>
  );
};
