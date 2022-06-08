import { Table } from "semantic-ui-react";

type Props = {
  user_name: string;
  played_at: Date;
  accuracy: number;
  wpm: number;
};

export const TableRow = (props: Props) => {
  const { user_name, played_at, accuracy, wpm } = props;

  return (
    <Table.Row>
      <Table.Cell>1</Table.Cell>
      <Table.Cell>{user_name}</Table.Cell>
      <Table.Cell>{played_at}</Table.Cell>
      <Table.Cell>{accuracy}</Table.Cell>
      <Table.Cell>{wpm}</Table.Cell>
    </Table.Row>
  );
};
