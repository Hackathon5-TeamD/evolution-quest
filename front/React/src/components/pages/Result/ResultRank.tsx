import { Container } from "semantic-ui-react";
import { Header } from "./Header/Header";
import { SubTitle } from "./SubTitle/SubTitle";
import { RankingTable } from "./ResultTable/ResultTable";
import styles from "./ResultPage.module.css";

export const ResultRank = () => {
  return (
    <div className={styles.wrapper}>
      <Container className={styles.container}>
        <Header />
        <SubTitle />
        <RankingTable />
      </Container>
    </div>
  );
};
