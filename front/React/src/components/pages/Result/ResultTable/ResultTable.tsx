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
  currentPage: number;
  setCurrentPage: React.Dispatch<React.SetStateAction<number>>;
  fetch: (page: number) => Promise<void>;
  setReady: React.Dispatch<React.SetStateAction<boolean>>;
};

export const RankingTable = memo((props: Props) => {
  const { rankingArr, currentPage, setCurrentPage, fetch, setReady } = props;

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
        <TableFooter
          currentPage={currentPage}
          setCurrentPage={setCurrentPage}
          fetch={fetch}
          setReady={setReady}
        />
      </Table>
    </div>
  );
});
