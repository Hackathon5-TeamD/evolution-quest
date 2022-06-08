import React from "react";
import styles from "./TableFooter.module.css";
import { Table, Menu, Icon } from "semantic-ui-react";

type Props = {
  setCurrentPage: React.Dispatch<React.SetStateAction<number>>;
};

export const TableFooter = (props: Props) => {
  const { setCurrentPage } = props;

  const onClickNext = () => {
    setCurrentPage((prev) => {
      console.log("押された");
      return prev + 1;
    });
  };

  const onClickPrev = () => {
    setCurrentPage((prev) => {
      return prev - 1;
    });
  };

  return (
    <Table.Footer>
      <Table.Row>
        <Table.HeaderCell colSpan="6">
          <Menu floated="right" pagination>
            <Menu.Item as="a" icon className={styles.pagenationBtn}>
              <Icon name="chevron left" />
            </Menu.Item>
            <Menu.Item as="a" className={styles.pagenation}>
              01-10
            </Menu.Item>
            <Menu.Item as="a" className={styles.pagenation}>
              11-20
            </Menu.Item>

            <Menu.Item
              as="a"
              icon
              className={styles.pagenationBtn}
              onClick={onClickNext}
            >
              <Icon name="chevron right" />
            </Menu.Item>
          </Menu>
        </Table.HeaderCell>
      </Table.Row>
    </Table.Footer>
  );
};
