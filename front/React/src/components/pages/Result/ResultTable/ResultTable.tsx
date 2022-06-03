import { Icon, Menu, Table } from "semantic-ui-react";
import styles from "./ResultTable.module.css";

export const RankingTable = () => (
  <div className={styles.tableContainer}>
    <Table singleLine className={styles.table}>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell width={2} className={styles.tableHeader}>
            順位
          </Table.HeaderCell>
          <Table.HeaderCell className={styles.tableHeader}>
            名前
          </Table.HeaderCell>
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
          <Table.Cell>terrelien</Table.Cell>
          <Table.Cell>2022-05-22</Table.Cell>
          <Table.Cell>89 %</Table.Cell>
          <Table.Cell>123 WPM</Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>2</Table.Cell>
          <Table.Cell>terrelien</Table.Cell>
          <Table.Cell>2022-05-22</Table.Cell>
          <Table.Cell>89 %</Table.Cell>
          <Table.Cell>123 WPM</Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>3</Table.Cell>
          <Table.Cell>terrelien</Table.Cell>
          <Table.Cell>2022-05-22</Table.Cell>
          <Table.Cell>89 %</Table.Cell>
          <Table.Cell>123 WPM</Table.Cell>
        </Table.Row>
      </Table.Body>

      <Table.Footer>
        <Table.Row>
          <Table.HeaderCell colSpan="6">
            <Menu floated="right" pagination>
              <Menu.Item as="a" icon className={styles.pagenation}>
                <Icon name="chevron left" />
              </Menu.Item>
              <Menu.Item as="a" className={styles.pagenation}>
                01-10
              </Menu.Item>
              <Menu.Item as="a" className={styles.pagenation}>
                11-20
              </Menu.Item>

              <Menu.Item as="a" icon className={styles.pagenation}>
                <Icon name="chevron right" />
              </Menu.Item>
            </Menu>
          </Table.HeaderCell>
        </Table.Row>
      </Table.Footer>
    </Table>
  </div>
);
