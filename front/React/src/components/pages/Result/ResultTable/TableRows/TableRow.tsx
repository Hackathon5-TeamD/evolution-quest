import { Table } from "semantic-ui-react";

type Props = {
  idx: number;
  user_name: string;
  played_at: Date;
  accuracy: number;
  wpm: number;
  currentPage: number;
};

export const TableRow = (props: Props) => {
  const { idx, user_name, played_at, accuracy, wpm, currentPage } = props;

  return (
    <Table.Row>
      {currentPage === 1 ? (
        <Table.Cell>{idx + 1}</Table.Cell>
      ) : (
        <Table.Cell>{idx + 11}</Table.Cell>
      )}

      <Table.Cell>{user_name}</Table.Cell>
      <Table.Cell>{played_at}</Table.Cell>
      <Table.Cell>{accuracy} %</Table.Cell>
      <Table.Cell>{wpm} WPM</Table.Cell>
    </Table.Row>
  );
};
