import { Table } from "semantic-ui-react";
import styles from "./ResultTable.module.css";
import { TableHeader } from "./TableHeader/TableHeader";
import { TableRow } from "./TableRows/TableRow";
import { TableFooter } from "./TableFooter/TableFooter";
import { mockData } from "../../../../types/ResultType";

type Props = {
  rankingArr: mockData[];
  currentPage: number;
  setCurrentPage: React.Dispatch<React.SetStateAction<number>>;
  fetch: (page: number) => Promise<void>;
  setReady: React.Dispatch<React.SetStateAction<boolean>>;
  timesFetchedArr2: number;
  setTimesFetchedArr2: React.Dispatch<React.SetStateAction<number>>;
};

export const RankingTable = (props: Props) => {
  const {
    rankingArr,
    currentPage,
    setCurrentPage,
    fetch,
    setReady,
    timesFetchedArr2,
    setTimesFetchedArr2,
  } = props;

  return (
    <div className={styles.tableContainer}>
      <Table singleLine className={styles.table}>
        <TableHeader />
        <Table.Body>
          {rankingArr.map((row, idx) => {
            return (
              <TableRow
                key={row.id}
                idx={idx}
                currentPage={currentPage}
                data={row}
              />
            );
          })}
        </Table.Body>
        <TableFooter
          currentPage={currentPage}
          setCurrentPage={setCurrentPage}
          fetch={fetch}
          setReady={setReady}
          timesFetchedArr2={timesFetchedArr2}
          setTimesFetchedArr2={setTimesFetchedArr2}
        />
      </Table>
    </div>
  );
};
