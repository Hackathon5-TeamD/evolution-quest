import { Table } from "semantic-ui-react";
import styles from "./ResultTable.module.css";
import { TableHeader } from "./TableHeader/TableHeader";
import { TableRow } from "./TableRows/TableRow";
import { TableFooter } from "./TableFooter/TableFooter";
import { memo } from "react";

type Props = {
  rankingArr: Array<{
    id: number;
    user_name: string;
    played_at: Date;
    accuracy: number;
    wpm: number;
  }>;
};

export const RankingTable = memo((props: Props) => {
  const { rankingArr } = props;

  return (
    <div className={styles.tableContainer}>
      <Table singleLine className={styles.table}>
        <TableHeader />
        <Table.Body>
          {rankingArr.map((row) => {
            return (
              <TableRow
                key={row.id}
                user_name={row.user_name}
                played_at={row.played_at}
                accuracy={row.accuracy}
                wpm={row.wpm}
              />
            );
          })}
        </Table.Body>
        <TableFooter />
      </Table>
    </div>
  );
});
