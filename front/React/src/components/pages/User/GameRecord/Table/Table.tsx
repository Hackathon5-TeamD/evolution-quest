import React from "react";
import { Table } from "semantic-ui-react";
import styles from "./Table.module.css";

export const GameRecordTable = () => (
  <div className={styles.tableContainer}>
    <Table singleLine>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell
            width={2}
            className={styles.tableHeader}
          ></Table.HeaderCell>
          <Table.HeaderCell className={styles.tableHeader}>
            プレイ日
          </Table.HeaderCell>
          <Table.HeaderCell className={styles.tableHeader}>
            正解率
          </Table.HeaderCell>
          <Table.HeaderCell className={styles.tableHeader}>
            1分あたりの文字数
          </Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        <Table.Row>
          <Table.Cell>1</Table.Cell>

          <Table.Cell>2022-05-22</Table.Cell>
          <Table.Cell>89 %</Table.Cell>
          <Table.Cell>123 WPM</Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>2</Table.Cell>

          <Table.Cell>2022-05-22</Table.Cell>
          <Table.Cell>89 %</Table.Cell>
          <Table.Cell>123 WPM</Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>3</Table.Cell>

          <Table.Cell>2022-05-22</Table.Cell>
          <Table.Cell>89 %</Table.Cell>
          <Table.Cell>123 WPM</Table.Cell>
        </Table.Row>
      </Table.Body>
    </Table>
  </div>
);
