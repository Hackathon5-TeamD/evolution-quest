import React from "react";
import { Table } from "semantic-ui-react";
import { TableHeader } from "./TableHeader/TableHeader";
import { TableRow } from "./TableRow/TableRow";
import styles from "./Table.module.css";

type Props = {
  recordArr: Array<{
    id: number;
    played_at: Date;
    accuracy: number;
    wpm: number;
  }>;
};

export const GameRecordTable = (props: Props) => {
  const { recordArr } = props;
  return (
    <div className={styles.tableContainer}>
      <Table singleLine>
        <TableHeader />
        <Table.Body>
          {recordArr.map((row, idx) => {
            return (
              <TableRow
                key={row.id}
                idx={idx}
                played_at={row.played_at}
                accuracy={row.accuracy}
                wpm={row.wpm}
              />
            );
          })}
        </Table.Body>
      </Table>
    </div>
  );
};
