import { Table } from "semantic-ui-react";
import { mockData } from "../../../../../types/ResultType";
import styles from "./TableRow.module.css";

type Props = {
  idx: number;
  currentPage: number;
  data: mockData;
};

export const TableRow = (props: Props) => {
  const { idx, currentPage, data } = props;
  const { id, user_name, played_at, accuracy, wpm } = data;

  return (
    <Table.Row>
      {currentPage === 1 ? (
        <Table.Cell className={styles.cell}>{idx + 1}</Table.Cell>
      ) : (
        <Table.Cell className={styles.cell}>{idx + 11}</Table.Cell>
      )}

      <Table.Cell className={styles.cell}>{user_name}</Table.Cell>
      <Table.Cell className={styles.cell}>{played_at}</Table.Cell>
      <Table.Cell className={styles.cell}>{accuracy} %</Table.Cell>
      <Table.Cell className={styles.cell}>{wpm} WPM</Table.Cell>
    </Table.Row>
  );
};
