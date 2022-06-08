import { Table } from "semantic-ui-react";
import styles from "./TableRow.module.css";

type Props = {
  idx: number;
  played_at: Date;
  accuracy: number;
  wpm: number;
};

export const TableRow = (props: Props) => {
  const { idx, played_at, accuracy, wpm } = props;
  return (
    <Table.Row>
      <Table.Cell className={styles.cell}>{idx + 1}</Table.Cell>
      <Table.Cell className={styles.cell}>{played_at}</Table.Cell>
      <Table.Cell className={styles.cell}>{accuracy} %</Table.Cell>
      <Table.Cell className={styles.cell}>{wpm} WPM</Table.Cell>
    </Table.Row>
  );
};
